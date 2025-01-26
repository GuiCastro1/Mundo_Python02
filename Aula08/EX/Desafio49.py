'''
Criado por: Gui Castro

20/01/2025

Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 e 500
'''
print('=====SOMA MULTIPLOS DE 3=====')

soma = 0 

contador= 0

for i in range(1,501,2):

    if i % 3 == 0:

        contador += 1

        soma += i

print(contador)

print(soma)
