'''
Criado por: Gui Castro

19/01/2025

Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher que e a base de conversão:

binário
octal
hexadecimal
'''
from time import sleep 

print('=====Conversor de unidades=====')

print('''Digite o valor inteiro que deseja converter & Selecione qual é a unidade desejada\n\nDigite (Bin) para converter em binário\n\nDigite (Oct) para converter em Octal\n\nDigite (Hex) para converter em Hexadecimal''')

valor = float(input('Valor:'))

unidade = str(input('Unidade:')).strip().upper()

print('PROCESSANDO...')

sleep(1.5)

if unidade == 'BIN':

    binario = bin(int (valor))

    print(f'O valor {valor} em binário é:{binario[2:]}')

elif unidade == 'OCT':

    octal = oct(int(valor))

    print(f'O valor {valor} em Octal é:{octal[2:]}')

elif unidade == 'HEX':

    hexadecimal = hex(int(valor))

    print(f'O valor {valor} em Hexadecimal é:{hexadecimal[2:]}')

else:

    print('Unidade de conversão não encontrada')

print('O programa acabou ! ! !')
