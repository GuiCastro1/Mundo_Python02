'''
Criado por: Gui Castro

23/01/2025

Crie um programa que mostre a tabuada de vários números, um de cada vez para cada valor digitado pelo usúario. O Programa será interrompido quando o número solicitado for negativo.
'''
print('=====Tabuada 3.0=====')

print('Digite um número NEGATIVO para sair')

while True:

    num = int(input('Digite um número para exibir a tabuada:'))
     
    if num < 0:
        break

    for i in range(1, 11):
        print(f'{num} x {i:2} = {i * num}')

print('O Programa Acabou ! ! !')
