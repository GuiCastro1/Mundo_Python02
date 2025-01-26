'''
Criado por: Gui Castro

21/01/2025

Crie um programa que leia varios números inteiros e só pare quando o usúario digitar 999. exiba a conta de todos os números sem o Flag(999)
'''
print('=====Soma=====')

stop = '9'

soma = 0
print('Digite 999 para mostrar a soma')
while stop != "999":

    stop= str(input('Digite quantos números quiser somar:'))

    soma += int(stop)

print(f'A soma de todos os numeros é :{soma - int(stop)}')