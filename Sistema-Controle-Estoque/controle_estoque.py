import csv
import os
from datetime import datetime


def caminho(nome):
    """Devolve o caminho de um arquivo de dados na pasta do projeto."""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), nome)

# --------------------------------------------------------------------------
# Funcionalidade de controle de estoque
# --------------------------------------------------------------------------

class Produto:
    """Produto cadastrado no estoque."""

    def __init__(self, codigo, nome, estoque=0):
        self.codigo = codigo
        self.nome = nome
        self.estoque = estoque


class Movimentacao:
    """Entrada ou saída registrada com data e responsável."""

    def __init__(self, tipo, produto, quantidade, data, responsavel):
        self.tipo = tipo
        self.produto = produto
        self.quantidade = quantidade
        self.data = data
        self.responsavel = responsavel


class ControleEstoque:
    """Regras de negócio do controle de estoque."""

    def __init__(self):
        self.produtos = {}
        self.movimentacoes = []

    def cadastrar_produto(self, codigo, nome, estoque=0):
        """Inclui um produto no cadastro."""
        self.produtos[codigo] = Produto(codigo, nome, estoque)

    def buscar_produto(self, codigo):
        """Devolve o produto pelo código, ou None se não existir."""
        return self.produtos.get(codigo)

    def salvar_dados(self):
        """Grava os produtos e as movimentações nos arquivos CSV."""
        with open(caminho("produtos.csv"), "w", newline="",
                  encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["codigo", "nome", "estoque"])
            for produto in self.produtos.values():
                escritor.writerow(
                    [produto.codigo, produto.nome, produto.estoque])

        with open(caminho("movimentacoes.csv"), "w", newline="",
                  encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(
                ["tipo", "codigo", "quantidade", "data", "responsavel"])
            for mov in self.movimentacoes:
                escritor.writerow([mov.tipo, mov.produto.codigo,
                                   mov.quantidade, mov.data,
                                   mov.responsavel])

    def carregar_dados(self):
        """Lê os arquivos CSV, descartando as linhas inválidas."""
        if os.path.exists(caminho("produtos.csv")):
            with open(caminho("produtos.csv"), newline="",
                      encoding="utf-8") as arquivo:
                for linha in csv.DictReader(arquivo):
                    try:
                        codigo = linha["codigo"]
                        nome = linha["nome"]
                        estoque = int(linha["estoque"])
                    except (KeyError, TypeError, ValueError):
                        print(">> Linha inválida ignorada em produtos.csv.")
                        continue

                    if estoque < 0:
                        print(f">> Produto {codigo} ignorado: "
                              "o estoque não pode ser negativo.")
                        continue
                    if self.buscar_produto(codigo) is not None:
                        print(f">> Produto {codigo} ignorado: "
                              "código repetido no arquivo.")
                        continue

                    self.cadastrar_produto(codigo, nome, estoque)

        if os.path.exists(caminho("movimentacoes.csv")):
            with open(caminho("movimentacoes.csv"), newline="",
                      encoding="utf-8") as arquivo:
                for linha in csv.DictReader(arquivo):
                    produto = self.buscar_produto(linha.get("codigo"))
                    if produto is None:
                        continue
                    try:
                        quantidade = int(linha["quantidade"])
                    except (KeyError, TypeError, ValueError):
                        continue
                    self.movimentacoes.append(
                        Movimentacao(linha["tipo"], produto, quantidade,
                                     linha["data"], linha["responsavel"]))

    def registrar_entrada(self, codigo, quantidade, data, responsavel):
        """Registra a entrada e atualiza o estoque."""
        produto = self.buscar_produto(codigo)
        if produto is None:
            raise ValueError("produto não cadastrado.")
        if quantidade <= 0:
            raise ValueError("a quantidade deve ser maior que zero.")

        produto.estoque += quantidade
        self.movimentacoes.append(
            Movimentacao("ENTRADA", produto, quantidade, data, responsavel))
        return produto

    def registrar_saida(self, codigo, quantidade, data, responsavel):
        """Registra a saída se houver estoque suficiente."""
        produto = self.buscar_produto(codigo)
        if produto is None:
            raise ValueError("produto não cadastrado.")
        if quantidade <= 0:
            raise ValueError("a quantidade deve ser maior que zero.")
        if quantidade > produto.estoque:
            raise ValueError("estoque insuficiente, disponível apenas "
                             f"{produto.estoque} unidade(s).")

        produto.estoque -= quantidade
        self.movimentacoes.append(
            Movimentacao("SAÍDA", produto, quantidade, data, responsavel))
        return produto


# --------------------------------------------------------------------------
# Funções de leitura de dados
# --------------------------------------------------------------------------

def ler_texto(mensagem):
    """Lê um texto obrigatório, repetindo enquanto vier em branco."""
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print(">> O campo não pode ficar em branco.")


def ler_inteiro(mensagem, minimo=1, maximo=99999):
    """Lê um número inteiro dentro dos limites informados."""
    while True:
        valor = input(mensagem).strip()
        try:
            numero = int(valor)
        except ValueError:
            print(">> Valor inválido. Informe um número inteiro.")
            continue

        if minimo <= numero <= maximo:
            return numero
        print(f">> Valor inválido. Informe um número entre "
              f"{minimo} e {maximo}.")


def ler_data(mensagem):
    """Lê uma data no formato dd/mm/aaaa; ENTER assume a data de hoje."""
    while True:
        valor = input(mensagem).strip()
        if not valor:
            return datetime.now().strftime("%d/%m/%Y")
        try:
            data = datetime.strptime(valor, "%d/%m/%Y")
        except ValueError:
            print(">> Data inválida. Use o formato dd/mm/aaaa.")
            continue

        # A movimentação registra um fato já ocorrido, nunca uma previsão.
        if data.date() > datetime.now().date():
            print(">> A data não pode ser futura.")
            continue

        return data.strftime("%d/%m/%Y")


# --------------------------------------------------------------------------
# Funções de apresentação
# --------------------------------------------------------------------------

def listar_produtos(estoque):
    """Exibe os produtos cadastrados e a quantidade em estoque de cada um."""
    print("\n--- PRODUTOS CADASTRADOS ---")
    print(f"{'CÓDIGO':<8} {'PRODUTO':<34} {'ESTOQUE':>8}")
    for produto in estoque.produtos.values():
        print(f"{produto.codigo:<8} {produto.nome:<34} "
              f"{produto.estoque:>8}")


def listar_movimentacoes(estoque):
    """Exibe o histórico de entradas e saídas."""
    print("\n--- HISTÓRICO DE MOVIMENTAÇÕES ---")
    if not estoque.movimentacoes:
        print("Nenhuma movimentação registrada até o momento.")
        return

    print(f"{'TIPO':<9} {'PRODUTO':<28} {'QTDE':>5} "
          f"{'DATA':<12} {'RESPONSÁVEL'}")
    for mov in estoque.movimentacoes:
        print(f"{mov.tipo:<9} {mov.produto.nome:<28} "
              f"{mov.quantidade:>5} {mov.data:<12} {mov.responsavel}")


def movimentar(estoque, tipo):
    """Conduz o registro de uma entrada ou de uma saída de produto."""
    listar_produtos(estoque)
    codigo = ler_texto("\nCódigo do produto: ")
    if estoque.buscar_produto(codigo) is None:
        print(">> Operação cancelada: produto não cadastrado.")
        return

    quantidade = ler_inteiro("Quantidade: ")
    data = ler_data("Data (dd/mm/aaaa ou ENTER para hoje): ")
    responsavel = ler_texto("Responsável: ")

    try:
        if tipo == "ENTRADA":
            produto = estoque.registrar_entrada(
                codigo, quantidade, data, responsavel)
        else:
            produto = estoque.registrar_saida(
                codigo, quantidade, data, responsavel)
    except ValueError as erro:
        print(f">> Operação cancelada: {erro}")
        return

    estoque.salvar_dados()
    print(f">> {tipo} registrada com sucesso.")
    print(f">> Estoque atualizado de {produto.nome}: "
          f"{produto.estoque} unidade(s).")


def cadastrar(estoque):
    """Conduz o cadastro de um novo produto."""
    codigo = ler_texto("\nCódigo do produto: ")
    # Código maior que a coluna desalinha a listagem de produtos.
    if len(codigo) > 8:
        print(">> Operação cancelada: o código deve ter até 8 caracteres.")
        return
    if estoque.buscar_produto(codigo) is not None:
        print(">> Operação cancelada: já existe produto com esse código.")
        return

    nome = ler_texto("Nome do produto: ")
    # Nome maior que a coluna desalinha a listagem de produtos.
    if len(nome) > 34:
        print(">> Operação cancelada: o nome deve ter até 34 caracteres.")
        return

    quantidade = ler_inteiro("Quantidade inicial em estoque: ", minimo=0)
    estoque.cadastrar_produto(codigo, nome, quantidade)
    estoque.salvar_dados()
    print(f">> Produto {codigo} - {nome} cadastrado com sucesso.")


def exibir_menu():
    """Mostra as opções disponíveis ao usuário."""
    print("\n=========================================")
    print("   SISTEMA DE CONTROLE DE ESTOQUE")
    print("=========================================")
    print("1 - Consultar produtos e estoque")
    print("2 - Registrar entrada de produto")
    print("3 - Registrar saída de produto")
    print("4 - Consultar histórico de movimentações")
    print("5 - Cadastrar novo produto")
    print("0 - Sair")


def carregar_estoque():
    """Carrega os dados salvos, criando os arquivos CSV se não existirem."""
    estoque = ControleEstoque()
    estoque.carregar_dados()

    # Na primeira execução os arquivos nascem apenas com o cabeçalho.
    if not (os.path.exists(caminho("produtos.csv"))
            and os.path.exists(caminho("movimentacoes.csv"))):
        estoque.salvar_dados()

    return estoque


def main():
    """Laço principal do programa."""
    estoque = carregar_estoque()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_produtos(estoque)
        elif opcao == "2":
            movimentar(estoque, "ENTRADA")
        elif opcao == "3":
            movimentar(estoque, "SAÍDA")
        elif opcao == "4":
            listar_movimentacoes(estoque)
        elif opcao == "5":
            cadastrar(estoque)
        elif opcao == "0":
            print("\nSistema encerrado.")
            break
        else:
            print(">> Opção inválida. Escolha um número do menu.")


if __name__ == "__main__":
    main()
