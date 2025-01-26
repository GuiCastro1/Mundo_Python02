'''
Criado por: Gui Castro

19/01/2025

Escreva um programa que leia dois números inteiros e os compare-os mostrando na tela uma mensagem:

-O primero valor é maior
-O segundo valor é maior 
-Não existe valor maior os dois são iguais
'''
print('=====Maior Menor & Igual=====')

print('Digite dois números')

num = int(input('Primeiro número:'))
ndois = int(input('Segundo número:'))

if ndois > num :

    print(f'O número {ndois} é maior que {num}')
    

elif num > ndois:

    print(f'O número {num} é maior que {ndois}')

else:

    print(f'O número {num} é igual a {ndois}')


