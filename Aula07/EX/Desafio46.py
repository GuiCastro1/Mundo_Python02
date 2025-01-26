'''
Criado por: Gui Castro

19/01/2025

Crie um programa faça o computador jogar JOKENPÔ com voc~e

pedra = ganha T / Perde PP
papel = ganha P / perde T
tesoura = ganha PP / perde P
'''
from random import randint

from time import sleep

import emoji

print('=====JOKENPÔ=====')
        
start = str(input('Você quer jogar? (y/n) 😈😈😈\n')).strip().upper()

if start == 'Y':
    print('''
    0- PEDRA
    1- PAPEL
    2- TESOURA\n''')

    jogador = int(input(':'))

    escolhas = [
    emoji.emojize(":black_circle:"),# Pedra
    emoji.emojize(":page_facing_up:"), # Papel
    emoji.emojize(":scissors:")       # Tesoura
    ]
    
    computador = randint(0, len(escolhas) - 1)

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ ! ! !')

    if jogador == computador:

        print('-=' * 25)
        print('EMPATE')
        print('EMPATE')
        print(f'Computador: {escolhas[computador]}')
        print(f'Você: {escolhas[jogador]}')
        print('-=' * 25)

    elif (jogador == 0 and computador == 1) or (jogador == 1 and computador == 2) or (jogador == 2 and computador == 0):

        print('-=' * 25)
        print('PERDEU')
        print('PERDEU')
        print(f'Computador: {escolhas[computador]}')
        print(f'Você: {escolhas[jogador]}')
        print('-=' * 25)

    else:
        print('-=' * 25)
        print('GANHOU ! ! !')
        print('GANHOU ! ! !')
        print(f'Computador: {escolhas[computador]}')
        print(f'Você: {escolhas[jogador]}')
        print('-=' * 25)

else:
    print('O jogo acabou ! ! ! ! !')

'''if jogador and computador== 0 or jogador and computador == 1 or jogador and computador == 2:

        print('EMPATE')
        print(f'Computador: {escolhas[computador]}')
        print(f'Você: {escolhas[jogador]}')

    elif jogador == 0 and computador == 1:

        print('PERDEU')
        print(f'Computador: {escolhas[computador]}')
        print(f'Você: {escolhas[jogador]}')

    elif jogador == 0 and computador ==2:

        print('GANHOU ! ! !')
        print(f'Computador: {escolhas[computador]}')
        print(f'Você: {escolhas[jogador]}')

    elif jogador == 1 and computador == 2:

        print('PERDEU')
        print(f'Computador: {escolhas[computador]}')
        print(f'Você: {escolhas[jogador]}')

    elif jogador == 1 and computador == 0:

        print('GANHOU ! ! !')
        print(f'Computador: {escolhas[computador]}')
        print(f'Você: {escolhas[jogador]}')

    elif jogador ==2  and computador == 0:

        print('PERDEU')
        print(f'Computador: {escolhas[computador]}')
        print(f'Você: {escolhas[jogador]}')
        
    elif jogador == 2 and computador == 1:

        print('GANHOU ! ! !')
        print(f'Computador: {escolhas[computador]}')
        print(f'Você: {escolhas[jogador]}')

'''