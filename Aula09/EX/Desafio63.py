'''
Criado por: Gui Castro

21/01/2025

Refaça o desaio 61, pergunta se o usúario quer mostrar mais alguns termos.O programa encerra quando ele disser que quer mostrar 0 termos.

MELHORAR    
'''

print('=====PA PT02=====')

continua = 's'
num = 0
termo = int(input('Digite o termo:'))
razao = int(input('Digite a razão:'))

while continua == 's':

    if continua == 's':

        t = int(input('Quantos termos a mais quer exibir nº de termos:'))

        num += t

    i = 1
    
    while i <=  num:

        conta = termo + (i - 1) * razao

        i += 1
         
        print(conta)

    continua = str(input('continuar[N / S]:')).strip().lower()

print('O programa acabou ! ! !')
