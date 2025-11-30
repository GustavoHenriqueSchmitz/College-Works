# Definição de variáveis globais
lista_livro = []
id_global = 0


# Função responsável pela funcionalidade de cadastro de livro
def cadastrar_livro(id):
   # Recebe, pega as informações do usuário e adiciona um novo livro a listagem de livros
   print("---------------------------------------------")
   print("---------- MENU CADASTRAR LIVRO ----------")
   print(f"Id do livro: {id}")
   nome = str(input("Por favor entre com o nome do livro: "))
   autor = str(input("Por favor entre com o autor do livro: "))
   editora = str(input("Por favor entre com a editora do livro: "))


   lista_livro.append({'id': id, 'nome': nome, 'autor': autor, 'editora': editora})
   print("---------------------------------------------\n")


# Função responsável pelas funcionalidades de consula de livros cadastrados
def consultar_livro():
   while True:
       # Recepção ao usuário
       print("---------------------------------------------")
       print("---------- MENU CONSULTAR LIVRO ----------")
       print("Escolha a opção desejada:")
       print("1 - Consultar Todos os Livros")
       print("2 - Consultar Livro por id")
       print("3 - Consultar Livro(s) por autor")
       print("4 - Retornar ao menu")


       # Pede a opção desejada ao usuário
       try:
           consultar_opcao = int(input(">> "))
       except:
           print("Opção inválida. Tente novamente.\n")
           continue
      
       # Consultar todos os livros
       if consultar_opcao == 1:
           if not lista_livro:
               print("Não há livros cadastrados.")
           else:
               for livro in lista_livro:
                   print("---------------------------------------------")
                   print(f"id: {livro['id']}")
                   print(f"nome: {livro['nome']}")
                   print(f"autor: {livro['autor']}")
                   print(f"editora: {livro['editora']}")
                   print("---------------------------------------------")
      
       # Consultar um livro pelo seu id
       elif consultar_opcao == 2:
           try:
               id_consultar = int(input("Digite o id do livro: "))
               encontrar = False
               for livro in lista_livro:
                   if livro['id'] == id_consultar:
                       print("-" * 10)
                       print(f"id: {livro['id']}")
                       print(f"nome: {livro['nome']}")
                       print(f"autor: {livro['autor']}")
                       print(f"editora: {livro['editora']}")
                       print("-" * 10)
                       encontrar = True
                       break
               if not encontrar:
                   print("Id inválido. Livro não encontrado.")
           except:
               print("Entrada inválida. Por favor, digite um número para o Id.")


       # Consultar livros por um autor
       elif consultar_opcao == 3:
           consultar_autor = input("Digite o autor do(s) livro(s): ")
           encontrar = [livro for livro in lista_livro if livro['autor'].lower() == consultar_autor.lower()]


           if not encontrar:
               print(f"Nenhum livro encontrado para o autor '{consultar_autor}'.")
           else:
               for livro in encontrar:
                   print("---------------------------------------------")
                   print(f"id: {livro['id']}")
                   print(f"nome: {livro['nome']}")
                   print(f"autor: {livro['autor']}")
                   print(f"editora: {livro['editora']}")
                   print("---------------------------------------------")


       # Retorna ao menu principal, senão retorna error de opção inválida ao usuário
       elif consultar_opcao == 4:
           return
       else:
           print("Opção inválida. Tente novamente.")


# Função responsável pela funcionalidade de deleção de livros
def remover_livro():
   # Recebe o usuário
   print("---------------------------------------------")
   print("---------- MENU REMOVER LIVRO ----------")
   # Pede o id do livro a ser removido, e o remove da lista de livros
   try:
       id_livro = int(input("Digite o id do livro a ser removido: "))
       global lista_livro
       index_para_remover = -1
       for contador, livro in enumerate(lista_livro):
           if livro['id'] == id_livro:
               index_para_remover = contador
               break
       if index_para_remover != -1:
           lista_livro.pop(index_para_remover)
       else:
           print("Id inválido. Livro não encontrado para remoção.")
   except:
       print("Entrada inválida. Por favor, digite um número para o Id.")


# Utiliza convenção que verifica se o código está sendo rodado de forma direta
if __name__ == "__main__":
   # Recepção ao usuário
   print("Bem vindo a Livraria do Gustavo Henrique Schmitz")
   while True:
       print("---------------------------------------------")
       print("---------- MENU PRINCIPAL ----------")
       print("Escolha a opção desejada:")
       print("1 - Cadastrar Livro")
       print("2 - Consultar Livro(s)")
       print("3 - Remover Livro")
       print("4 - Encerrar Programa")


       # Verifica a opção desejada pelo usuário e chama a função responsável
       try:
           opcao_principal = int(input(">> "))
       except:
           print("Opção inválida. Tente novamente.\n")
           continue
       if opcao_principal == 1:
           id_global += 1
           cadastrar_livro(id_global)
       elif opcao_principal == 2:
           consultar_livro()
       elif opcao_principal == 3:
           remover_livro()
       elif opcao_principal == 4:
           break
       else:
           print("Opção inválida. Tente novamente.")


