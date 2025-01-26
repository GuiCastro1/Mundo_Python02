'''
Criado por: Gui Castro

19/01/2025

A Confederação Nacional De Natação precisa de um programa que leia o ano de nascimento de uma atleta e mostre sua categoria de acordo com sua idade:

-Até 9 Anos = Mirim
-Até 14 Anos = Infantil
-Até 19 Anos = Junior 
-Até 20 Anos = Sênior 
-Acima = Master

'''

from datetime import date

print('=====Categoria Atleta=====')

print('Digite o seu ano de Nascimento')

ano_user = int(input('Ano:'))

categoria = date.today().year - ano_user

print(f'O atleta tem {categoria} anos')
# if categoria >= 1 and categoria <= 9:
if categoria <= 9:

    print(f'Você e da categoria MIRIM')

# elif categoria >= 10 and categoria <=14:
elif categoria <=14:

    print(f'Você e da categoria INFANTIL')

# elif categoria >= 15 and categoria <= 19:
elif categoria <= 19:

    print(f'Você e da categoria JUNIOR')

#elif categoria == 20:
elif categoria <= 25:
    print(f'Você e da categoria SÊNIOR')

else:
    print(f'Você e da categoria MASTER')