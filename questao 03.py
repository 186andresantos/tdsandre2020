# Questão 3
""" Escreva um programa para ler uma temperatura em Fahrenheit.
Faça uma função chamada Celsius para calcular e retornar o valor 
correspondente em graus Celsius.
Fórmula C = ((F-32)/9)*5 """

def celsius(F):
    C = ((F-32)/9)*5
    return C

while True:
   try:
      Temperatura = float(input("\n Digite o valor de uma temperatura em (Fahrenheit):"))
      print(f"\n A temperatura em Celsius é: {celsius(temperatura): 5}")
      break

   except:
      print("\n Valor inválido! Digite novamente!")