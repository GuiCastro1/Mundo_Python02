'''
Criado por: Gui Castro

20/01/2025

Crie umprograma que leia o ano de  nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maior idade e quntas ja são maiores
'''
print('=====DMAIOR & DMENOR=====')

from datetime import date

ano = date.today().year

maior_de_idade = 0
menor_de_idade = 0

for i in range(1,8):

    data = int(input(f'Digite a data de nascimento da {i}º pessoa:'))

    if (ano - data) < 18:

         menor_de_idade += 1

    else:
        maior_de_idade += 1

print(f'{menor_de_idade}: são menores de idade')
print(f'{maior_de_idade}: são maiores de idade')
