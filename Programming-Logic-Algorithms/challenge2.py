# Utiliza convenção que verifica se o código está sendo rodado de forma direta
if __name__ == "__main__":
   # Mensagem de recepção ao cliente
   print("Bem-vindo a Loja de Gelados do Gustavo Henrique Schmitz")
   print("--------------------Cardápio--------------------")
   print("----|--------|--------------|------------|----")
   print("----| Tamanho | Cupuaçu (CP) | Açaí (AC) |----")
   print("----|--------|--------------|------------|----")
   print(f"----| {'P':<7}| {'R$ 9.00':<13}| {'R$ 11.00':<11}|----")
   print(f"----| {'M':<7}| {'R$ 14.00':<13}| {'R$ 16.00':<11}|----")
   print(f"----| {'G':<7}| {'R$ 18.00':<13}| {'R$ 20.00':<11}|----")
   print("----|--------|--------------|------------|----")
   print("----------------------------------------------")


   # Inicia o looping de compra de produtos, definindo o valor total final
   total_price = 0
   while True:
       # Pega as informações do usuário
       while True:
           flavor = str(input("Entre com o sabor desejado (CP/AC): ")).lower().strip()
           if flavor not in ("cp", "ac"):
               print("Sabor inválido. Tente novamente\n")
               continue
      
           size = str(input("Entre com o tamanho desejado (P/M/G): ")).lower().strip()
           if size not in ("p", "m", "g"):
               print("Tamanho inválido. Tente novamente\n")
               continue
           else:
               break
      
       # Listagem de produtos e seus valores. Imprime para o usuário o produto comprado e seu valor, adicionando o valor ao total
       flavors = {
           "cp": {"name": "Cupuaçu", "p": 9.00, "m": 14.00, "g": 18.00},
           "ac": {"name": "Açaí", "p": 11.00, "m": 16.00, "g": 20.00}
       }
       total_price += flavors[flavor][size]
       print(f"Você pediu um {flavors[flavor]["name"]} no tamanho {size.upper()}: R$ {flavors[flavor][size]:.2f}\n")


       # Válida se o usuário deseja continuar comprando mais produtos
       while True:
           answer = str(input("Deseja mais alguma coisa? (S/N): ")).lower().strip()
           if answer in ("s", "n"):
               break
           else:
               print("Resposta inválida. Tente novamente\n")
               continue
      
       # Validação final, finalizar ou não a compra
       if answer == "n":
           print(f"O valor total a ser pago: R$ {total_price:.2f}")
           break
       else:
           continue