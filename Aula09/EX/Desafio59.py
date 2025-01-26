'''
Criado por: Gui Castro

21/01/2025

Melhore o desafio 28 onde o computador vai pensar um número entre  0 e 10. Só que agora o jogador vai tentar adivinhar até acertar. mostrando no final o numero de tentativas.

'''

from time import sleep
from random import randint
from playsound import playsound

print('=====JOGO DA ADIVINHAÇÃO=====')

print('TENTE ADIVINHAR EM QUE NÚMERO ESTOU PENSANDO ENTRE 1 E 10')

jogador = str(input('Você quer jogar? \n[Y / N] 😈😈😈')).upper().strip()[0]

if jogador == 'Y':

    resportas = int(input('Digite um número:'))
    contador = 0
    computador = randint(1,10)
    
    while resportas != computador:

        for i in range(1,4): 
            print(f'PROCESSANDO{i * '.'}')
            sleep(0.3)
        
        if resportas > computador:
            print('MENOS ...')
        if resportas < computador:
            print('MAIS ...')
        print('Você ERROU ! ! ! Tente Novamente',end=' ')
        print('😈😈😈HA HA HA HA HA HA')
        
        playsound('C:/Users/Admin/Documents/Mundo_Python02/Aula08/zoioconriga.mp3')
        resportas = int(input('Digite um número:'))
        contador += 1

    if resportas == computador:
            print(f'Você GANHOU  ! ! ! 😤😤😤')
            print(f'Tentativas:{contador}')
            playsound('C:/Users/Admin/Documents/Mundo_Python02/Aula08/SENNA.mp3')

else:
    print('Talvez na próxima!😤😤😤')

'''
    import random
import time
from playsound import playsound

def jogo_adivinhacao():
    print('===== JOGO DA ADIVINHAÇÃO =====')
    print('TENTE ADIVINHAR EM QUE NÚMERO ESTOU PENSANDO ENTRE 1 E 10')

    jogador = input('Você quer jogar? [Y/N] 😈😈😈 ').strip().upper()

    if jogador == 'Y':
        numero_secreto = random.randint(1, 10)
        tentativas = 0

        while True:
            try:
                resposta = int(input('Digite um número: '))
                tentativas += 1

                # Efeito de processamento
                for i in range(1, 4):
                    print(f'PROCESSANDO{"." * i}')
                    time.sleep(0.3)

                # Feedback do jogo
                if resposta > numero_secreto:
                    print('MENOS ...')
                elif resposta < numero_secreto:
                    print('MAIS ...')
                else:
                    print(f'Você GANHOU! 😤😤😤')
                    print(f'Tentativas: {tentativas}')
                    playsound('C:/Users/Admin/Documents/Mundo_Python02/Aula08/SENNA.mp3')
                    break

                print('Você ERROU! Tente novamente! 😈😈😈 HA HA HA HA HA HA')
                playsound('C:/Users/Admin/Documents/Mundo_Python02/Aula08/zoioconriga.mp3')

            except ValueError:
                print('Por favor, digite um número válido.')

    else:
        print('Talvez na próxima! 😤😤😤')

# Chamar o jogo
jogo_adivinhacao()
'''

'''
from random import randint
computador = randint(0,10)
print('Que numero estou pensando???')
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Digite um número'))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais ... tente de novo')
        elif jogador > computador:
            print('Menos ... tente de novo')

print(f'Acertou depois de {tentativas} tentativas')
'''
    