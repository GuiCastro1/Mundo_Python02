'''
Criado por: Gui Castro

20/01/2025

Desenvolva um programa que leia o Nome, Sexo e Idade de 5 pessoas. No final mostre ;

A media de idade do grupo

Qual e o nome do mais velho h

quantas pessoas tem menos de 20 m
'''
media = 0

mais_velho = 0
nome_mais_velho = ''

mais_novas = 0
for i  in range(1 , 6):  

    print(f'---{i}ª Pessoa---')
    nome = str(input('Digite seu nome:')).strip()
    idade = int(input('Sua idade:'))
    sexo = str(input('Sexo [ M / F ]:')).strip()

    media += idade

    if i == 1 and sexo in "Mm":
        mais_velho = idade
        nome_mais_velho = nome
    if sexo in "Mm" and idade >mais_velho:
        mais_velho = idade
        nome_mais_velho = nome
    if sexo in "Ff" and idade < 20:
        mais_novas += 1

print(f'A media de idade do grupo é{media / 5}')
print(f'O homem mais velho tem {mais_velho} e se chama {nome_mais_velho}')
print(f'{mais_novas} mulheres são menores de idade')