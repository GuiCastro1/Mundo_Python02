'''
Criado por: Gui Castro

19/01/2025

Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo pode ser criado:

-Equilátero = todos os lados iguais(A == B AND A == C)

-Isósceles = Dois lados iguais (A == B OR A == C)

-Escaleno = Todos os lados diferentes(A != B AND A != C)

'''
from time import sleep
print('=====Pode ser um triângulo? Qual?=====')

l1 = float(input('Digite o valor da primeira reta:'))
l2 = float(input('Digite o valor da segunda reta:'))
l3 = float(input('Digite o valor da terceira reta:'))

if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):

    print(f'AS Retas {l1}, {l2} e {l3} podem formar um triângulo')

    print('PROCESSANDO. . .')
    
    sleep(2)

    # if (l1 == l2) and (l1 == l3) and (l2 ==l3):
    if l1 == l2 == l3:

        print('Equilátero = todos os lados iguais')
    
    elif (l1 == l2) or (l1 == l3) or (l2 == l3):

        print('Isósceles = Dois lados iguais')

    # elif (l1 != l2) and (l1 != l3) and (l2 !=l3):
    elif l1 != l2 != l3 != l1:
        
        print('Escaleno = Todos os lados diferentes')

else: 
    print(f'As retas {l1},{l2} e {l3} NÃO PODEM formar um triângulo')
