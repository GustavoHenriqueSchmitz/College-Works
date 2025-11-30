# Utiliza convenção que verifica se o código está sendo rodado de forma direta
if __name__ == "__main__":
  # Pega as informações do usuário
  print("Bem-vindo a Loja do Gustavo Henrique Schmitz")
  product_value = float(input("Entre com o valor do produto: "))
  product_quantity = int(input("Entre com a quantidade do produto: "))
  total_value = product_value * product_quantity

  # Lógica de validação de desconto
  final_value = total_value
  if total_value >= 2500 and total_value < 6000:
      final_value = total_value * (1 - 4 / 100)
  elif total_value >= 6000 and total_value < 10000:
      final_value = total_value * (1 - 7 / 100)
  elif total_value >= 10000:
      final_value = total_value * (1 - 11 / 100)
  else:
      pass
   # Retorna o resultado final
  print(f"O valor SEM desconto: {total_value:.2f}")
  print(f"O valor COM desconto: {final_value:.2f}")