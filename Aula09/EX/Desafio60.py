'''
Criado por: Gui Castro

21/01/2025

Crie um programa que leia dois números e mostre na tela uim menu:



Seu programa deverá realizar a operação solicitado pelo usuario.
'''
print('=====MINI CALCULADORA=====')


num = int(input('Digite o primeiro valor:'))
ndois = int(input('Digite o segundo valor:'))
operacao = 0

while operacao != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros 
    [5] sair do programa
    ''')
    operacao = int(input('Digite o valor da operação:'))

    if operacao == 1:

        print(f'A soma de {num} + {ndois} é = {num + ndois}')

    elif operacao == 2:

        print(f'A multiplicação de {num} * {ndois} é = {num * ndois}')
    
    elif operacao == 3: 

        if num > ndois:
            print(f'Maior {num} & Menor {ndois}')

        else:
            print(f'Maior {ndois} & Menor {num}')

    elif operacao == 4:
        for i in range(1, 6):

            print(f'LIMPANDO{i * '.'}')
        
        num = int(input('Digite o primeiro valor:'))
        ndois = int(input('Digite o segundo valor:'))
    
    elif operacao == 5:
        operacao = 5

    else:
        print('Opção inválida tente de novo')

    print('-=' * 15)

print('O Programa Acabou ! ! !')


'''

'''