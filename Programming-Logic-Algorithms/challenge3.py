# Utiliza convenção que verifica se o código está sendo rodado de forma direta
if __name__ == "__main__":
   # Lida com a funcionalidade de escolha de serviço
   def escolha_servico():
       while True:
           print("Entre com o tipo de serviço desejado")
           print("DIG - Digitalização")
           print("ICO - Impressão Colorida")
           print("IPB - Impressão Preto e Branco")
           print("FOT - Fotocópia")


           # Pergunta o serviço desejado e retorna seu respectivo valor
           service = str(input(">> "))
           if service == "dig":
               return 1.10
           elif service == "ico":
               return 1
           elif service == "ipb":
               return 0.40
           elif service == "fot":
               return 0.20
           else:
               print("Escolha inválida, entre com o tipo de serviço novamente\n")
               continue
  
   # Lida com a funcionalidade de escolha da quantidade de páginas desejadas
   def num_pagina():
       while True:
           # Pergunta a quantidade desejada e retorna seu respectivo valor
           try:
               page_quantity = int(input("Entre com o número de páginas: "))
           except:
               print("Valor inválido.")
               print("Por favor, entre com o número de páginas novamente.\n")
               continue


           if page_quantity >= 20 and page_quantity < 200:
               return page_quantity * (1 - 0.15)
           elif page_quantity >= 200 and page_quantity < 2000:
               return page_quantity * (1 - 0.20)
           elif page_quantity >= 2000 and page_quantity < 20000:
               return page_quantity * (1 - 0.25)
           elif page_quantity >= 20000:
               print("Não aceitamos tantas páginas de uma vez.")
               print("Por favor, entre com o número de páginas novamente.\n")
               continue
           elif page_quantity < 0:
               print("Valor inválido.")
               print("Por favor, entre com o número de páginas novamente.\n")
               continue
           else:
               return page_quantity * (1 - 0)
      
   # Lida com a funcionalidade de escolha de serviço extra
   def servico_extra():
       while True:
           print("Deseja adicionar algum serviço?")
           print("1 - Encadernação Simples - R$ 15.00")
           print("2 - Encadernação Capa Dura - R$ 40.00")
           print("0 - Não desejo mais nada")


           # Pergunta o serviço desejado e retorna seu respectivo valor
           try:
               extra_service = int(input(">> "))
           except:
               print("Valor inválido.")
               print("Por favor, entre com o serviço extra desejado novamente.\n")
               continue


           if extra_service == 1:
               return 15.00
           elif extra_service == 2:
               return 40.00
           elif extra_service == 0:
               return 0.00
           else:
               print("Opção inválida.")
               print("Por favor, entre com o serviço extra desejado novamente.\n")


   # Mensagem de recepção ao cliente
   print("Bem-vindo a Copiadora do Gustavo Henrique Schmitz\n")
   # Executa as funcionalidades do programa
   service_price = escolha_servico()
   page_quantity = num_pagina()
   extra_service_price = servico_extra()
  
   # Retorna o valor final do pedido realizado pelo usuário
   total_price =  service_price * page_quantity + extra_service_price
   print(f"Total: R$ {total_price:.2f} (serviço: {service_price:.2f} * páginas: {page_quantity:.0f} + extra: {extra_service_price:.2f})")