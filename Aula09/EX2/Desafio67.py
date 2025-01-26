'''
Criado por: Gui Castro

23/01/2025

Crie um programa que leia vários números int pelo teclado. o programa só vai para quando o usúario digitar 999, que é a condição de parada no final mostre quantos números foram digitados mais a soma.
'''
print('=====Soma 3.0=====')
contador = soma = 0

while True:

    num = int(input('Digite um número [999 para parar]: '))

    if num == 999:
        break

    else:
        soma += num 
        contador +=1

print(f'Você digitou {contador}, e a soma deles é ={soma}')
