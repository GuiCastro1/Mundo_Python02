'''
Criado por: Gui Castro

19/01/2025

Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento :

-À vista Dinheiro/Cheque/Pix 10% de desconto
-À vista no cartão 5 % de desconto
-Em até 2 vezes preço normal 
-3 vezes ou mais no cartão : 20% de desconto
'''
print('=====Desconto=====\n')


valor = float(input('Valor:'))

pagamento = int(input('''

1 - Dinheiro/Cheque/Pix
2 - À vista no cartão
3 - 2x no cartão
4 - 3x ou mais no cartão\n

Digite:'''))

if pagamento == 1:

    desconto = valor - (valor * 10 / 100)
    
    print(f'O valor do seu produto com desconto de 10% :RS {desconto :.2f}')

elif pagamento == 2:

    desconto = valor - (valor * 5 / 100)

    print(f'O valor do seu produto com desconto de 5% :RS {desconto :.2f}')

elif pagamento == 3:

    print(f'Para pagamentos em ate duas vezes não é atribuído nenhum desconto. O valor do seu produto dividido em duas vezes é de :R$ {valor / 2 :.2f}') 

elif pagamento == 4:

    juros = valor + (valor * 20 / 100) 

    parcela = int(input('Quantas parcelas:'))

    print(f'O valor do seu produto com parcelado em 3x ou mais tem u juros de 20%:RS {juros / parcela:.2f}')

else:

    print('OPÇÃO DE PAGAMENTO INVALIDA ! ! !')
