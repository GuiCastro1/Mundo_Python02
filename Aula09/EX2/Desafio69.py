'''
Criado por: Gui Castro

23/01/2025

Faça um programa que jogue par ou ímpar com o computador.O jogo só será interrompido qundo o JOGADOR perder, mostre quantas vitórias o jogador teve.
'''
print('=====Jogo do ÍMPAR OU PAR=====')

from random import randint
from time import sleep
from playsound import playsound

contador = 0

while True:

    num_computador = randint(1,100)

    par_impar = str(input('Par ou Ímpar?[P / I]')).strip().upper()

    while par_impar not in'PI':

        par_impar = str(input('Par ou Ímpar?[P / I]')).strip().upper()

    num = int(input('Número:'))

    if par_impar == 'P' and (num + num_computador) % 2 == 1:

        print('PERDEU\n')
        print(f'COMPUTADOR {num_computador}')
        print(f'VOCÊ {num}\n')
        print(f'{num + num_computador} é ÍMPAR' )
        print(f'Ganhos consecutivos:{contador}')

        break

    if par_impar == 'I' and (num + num_computador) % 2 == 0:

        print('PERDEU\n')
        print(f'COMPUTADOR {num_computador}')
        print(f'VOCÊ {num}\n')
        print(f'{num + num_computador} é PAR' )
        print(f'Ganhos consecutivos:{contador}')

        break

    else:
        contador += 1 

        print('GANHOU  ! ! ! !\n')
        print(f'COMPUTADOR {num_computador}')
        print(f'VOCÊ {num}\n')
        print(f'{num + num_computador} é {'PAR' if num + num_computador % 2 ==0 else 'ÍMPAR'}')

        playsound('Aula08/SENNA.mp3')
'''



from random import randint
from playsound import playsound

print("===== Jogo do ÍMPAR OU PAR =====")

contador = 0

while True:
    num_computador = randint(1, 100)
    par_impar = input("Par ou Ímpar? [P/I]: ").strip().upper()

    while par_impar not in "PI":
        par_impar = input("Opção inválida! Par ou Ímpar? [P/I]: ").strip().upper()

    num = int(input("Escolha um número: "))
    soma = num + num_computador
    resultado = "PAR" if soma % 2 == 0 else "ÍMPAR"
    venceu = (par_impar == "P" and soma % 2 == 0) or (par_impar == "I" and soma % 2 == 1)

    print(f"\nVOCÊ: {num} | COMPUTADOR: {num_computador} | TOTAL: {soma} ({resultado})")
    if venceu:
        contador += 1
        print(f"Você GANHOU! Vitórias consecutivas: {contador}\n")
        playsound("Aula08/SENNA.mp3")
    else:
        print(f"Você PERDEU! Total de vitórias: {contador}")
        break

'''