'''
Criado por: Gui Castro

20/01/2025

Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
'''
print('=====PRIMOS=====')

num = int(input('Digite um número:'))

conta = 0
#meu
for i in range(1, num +1):
  
    if num %  i == 0:
        conta += 1

if conta == 2:
    print(f'O número : {num}. É PRIMO')
else:
     print(f'O número : {num}. NÃO É PRIMO')
    