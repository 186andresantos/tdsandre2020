# Questão 11
""" Faça uma função que recebe, por parãmetro um valor inteiro e positivo
e retorna o número de divisores desse valor."""

def divisores(n):
  qtd = 0
  for i in range (1,n+1):
      if n % i == 0:
         qtd += 1
  print(f"\n O número de divisores de {n} é {qtd}.")

while True:
  try:
     num = int(input("\n Digite um número positivo maior que ZERO:"))
     if num<0:
        print("\n O número informado é negativo. Digite novamente!")
     elif num== 0:
        print("\n O ZERO não é um número composto pois possui uma infinidade de divisores.")
        break
     else:
        divisores(num)
        break
  except:
     print("\n Número inválido! Digite novamente!")


