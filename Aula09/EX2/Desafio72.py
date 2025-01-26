'''
Criado por: Gui Castro

23/01/2025

Crie um programa que simule um caixa eletrônico. No início, solicite o valor que o usúario quer sacar, e o programa deve informar deve informar qanatas cédulas decada valor serão entregues
  
considere notas de: 50, 20, 10, 1 
'''
print('=====Banco do GUILHERME=====')

valor = int(input('Valor de saque'))

total = valor

ced = 50

total_ced = 0

while True:

    if total >= ced:
        total -= ced
        total_ced += 1
    
    else:
        if total_ced > 0 :
            print(f'O total de {total_ced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced =10
        elif ced == 10:
            ced = 1
        total_ced =0
        if total == 0:
            break

'''
    milhar = valor // 1000

    centena = (valor // 100) % 10

    dezena = (valor // 10) % 10

    unidade = valor % 10


    # print(unidade  * 1)
    # print(dezena  * 10)
    # print(centena * 100)
    # print(milhar * 1000)

    # print((unidade  * 1) // 1)
    # print((dezena  * 10) // 10)
    # print((centena * 100) // 20)
    # print((milhar * 1000) // 50)

'''