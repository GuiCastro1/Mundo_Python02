'''
Criado por: Gui Castro

23/01/2025

    Crie um program aque leia o nome é o preço de vários produtos.o programa deverá perguntar ao usúario  vai continuar. No final mostre:

    Qual foi o total gasto na compra 

    Quantos protudos custam masis de 1000 reais.

    O nome do produto mais barato 
'''
print('====Loja da família Castro=====')

soma = 0
contador = 0 
cont_barato = 0
valor_mais_baixo =0
nome = ''

while True:

    produto = str(input('Nome do Produto:'))
    valor = float(input('Valor:'))

    soma += valor
    cont_barato += 1

    if valor > 1000:

        contador += 1
    
    if cont_barato == 1 or valor <  valor_mais_baixo:

        valor_mais_baixo = valor
        nome = produto

    continuar = ' '

    while continuar not in 'SN':

        continuar = str(input('Deseja continuar [S / N]')).upper().strip()[0]

    if continuar == 'N':
        break


print(f'O total gasto na compra {soma :.2f}R$')
print(f'{contador} Protudos custaram masis de 1000 reais.')
print(f'O produto mais barato é :{nome} que custou {valor_mais_baixo:.2f}R$')