# Sistema de Controle de Estoque

Atividade Prática da disciplina de **Engenharia de Software** — Uninter.
Autor: Gustavo Henrique Schmitz — RU 5127631

Sistema em Python para registrar a entrada e a saída de produtos do
almoxarifado, mantendo a quantidade atualizada e o histórico das movimentações.

## Persistência

Os dados ficam gravados em dois arquivos CSV, criados na pasta do projeto:

- `produtos.csv` — código, nome e quantidade em estoque de cada produto.
- `movimentacoes.csv` — tipo, produto, quantidade, data e responsável.

Os arquivos são lidos na abertura do programa e regravados a cada
operação confirmada, então o estoque continua de onde parou. Na primeira
execução, sem arquivos no disco, o sistema cria um cadastro inicial de
quatro produtos.

## Como executar

```bash
python3 controle_estoque.py
```

Não há dependências externas: apenas a biblioteca padrão do Python 3.

## Funcionalidades

| Requisito | Onde está implementado |
|---|---|
| RF01 — selecionar produto já cadastrado | `criar_estoque_inicial` e `ControleEstoque.buscar_produto` |
| RF02 — entrada com quantidade e data | `ControleEstoque.registrar_entrada` |
| RF03 — atualização automática do estoque | `ControleEstoque.registrar_entrada` |
| RF04 — saída com produto e quantidade | `ControleEstoque.registrar_saida` |
| RF05 — validar estoque antes da saída | `ControleEstoque.registrar_saida` |
| RF06 — histórico com data e responsável | `Movimentacao` e `listar_movimentacoes` |
| Persistência dos dados | `ControleEstoque.salvar_dados` e `carregar_dados` |

## Validações

- Quantidade precisa ser um número inteiro maior que zero.
- Saída maior que a quantidade disponível é recusada, e o estoque nunca fica negativo.
- Data aceita apenas o formato `dd/mm/aaaa`; ENTER assume a data atual.
- Código de produto inexistente cancela a operação.
- Campos de texto não podem ficar em branco.
- Código repetido é recusado no cadastro de produto.
- Linhas inválidas nos arquivos CSV são descartadas na leitura.
