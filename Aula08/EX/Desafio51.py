'''
Criado por: Gui Castro

20/01/2025

Faça um progarma que leia seis números inteiros e mostre a soma apenas daqueles que forem pare. Se o valor for ímpar desconsidere-o.
'''
print('=====SOMA DE PARES=====')
soma = 0
cont = 0
for i in range(1,7):

    usuario = int(input('Digite um número inteiro:'))

    if usuario % 2 == 0:
        cont += 1
        soma += usuario

print(soma)
print(cont)

