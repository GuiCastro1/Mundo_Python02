'''
Criado por: Gui Castro

19/01/2025

Escreva um programa para aprovar o empréstimo bancário para comprar uma casa. O programa o vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder o 30% do salário ou então o empréstimo sera negado.
'''

print('=====Empréstimo=====')

valor = float(input('Digite o valor da casa que deseja comprar:'))
salario = float(input('Digite o valor da sua renda mensal?salário:'))
ano = int(input('Em quantos anos você vai pagar'))

#ERREI A CONTA
prestacao = valor / (ano * 12)  

aprovacao = salario * 30 / 100

if prestacao > aprovacao :
    
   print(f'Empréstimo NEGADO, o valor da prestação:R${prestacao} excede 30% da sua renda mensal:R${aprovacao}')
    
else:
   
    print(f'Empréstimo APROVADO ! ! !.  o valor da sua prestação:R${prestacao}  não excede o valor de 30% do seu salário:{aprovacao}')
