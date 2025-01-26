'''
Criado por: Gui Castro

21/01/2025

Faça um programa que leia um número e mostre seu fatorial
'''
print('=====Fatorial=====')
from math import factorial
num = int(input('Digite um número:'))

# i = 1
# aux = 1

# while i <= num:

#     aux *=i

#     i += 1
#     print(aux)

c = num 
f = 1

while c > 0:

    f*=c

    c-=1

print(f)

print(f'{factorial(num)}')

