# Questão 10
""" Escreva um programa composto de uma função Max e o programa principal como segue:
a) A função Max recebe como parãmetros de entrada dois números inteiros e 
retorna o maior. Se forem iguai retorna qualquer um deles;
b) O programa principal lê 4 séries de 4 números a,b.
Para cada série lida imprima o maior dos quatro números usando a função Max """

def Max(n1,n2):
    if n1>n2:
       return n1
    else:
       return n2
       if n1==n1:
          maior = n1
          return maior

while True:
   try:
       num1 = int(input("\n Digite um número: "))   
       num2 = int(input("\n Digite outro número: "))  
       if num1==num2:
          print("\n Os números são iguais. ")    
          break
       else: 
          print("\n O maior número é {Max(num1,num2)}. ")
          break

   except:
       print("\n Valor inválido! Digite novamente!")

