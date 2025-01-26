'''
Criado por: Gui Castro

20/01/2025

Faça um programa que mostre na tela todos números pares que estão no intervalo de 1 a 50
'''
print('=====NÚMEROS PARES DE 1 A 50=====')
for i in range(1,51):
    if i % 2 == 0:
        print(f'\n{i}.',end=' ')

#nenos processamento
for i in range(2,50,2):

        print(f'\n{i}.',end=' ')