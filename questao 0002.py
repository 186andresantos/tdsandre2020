#Questão 02
"""Escreva um programa que leia o raio de um círculo e faça duas funções:
uma função chamada área que calcula e retorna a área do círculo e outra função
chamada perímetro que calcula e retorna o perímetro do círculo.
Área = PI * r ^ 2 ; Perímetro = PI * 2 * r """

def area(r):
   area = 3.14 * r**2
   return area

def perímetro(r):
   perímetro = 3.14*2*r
   return perímetro

while True:
   try:
    raio = int(input("\n Digite o raio do círculo:"))
    print(f"\n A área do círculo é:{area(raio)}")
    print(f"\n O perímetro do círculo é: {perímetro(raio)}")
    break

   except:
    print("\n Valor inválido! Digite novamente!")
