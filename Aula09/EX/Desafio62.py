'''
Criado por: Gui Castro

21/01/2025

Refaça o desafio 51 lendo o primeiro termo de uma razão PA, mostrando os 10 primeiros termos da PA usando o while.
'''
print('=====Progressão Aritimética=====')

termo = int(input('Digite o termo:'))
razao = int(input('Valor da razão:'))

i = 1

while i <= 10 :

    conta = termo + (i - 1) * razao

    i +=1
    
    print(f'{conta} ', end=' ')
