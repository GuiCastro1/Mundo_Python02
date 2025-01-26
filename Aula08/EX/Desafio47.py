'''
Criado por: Gui Castro

20/01/2025

Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 a 0 compausa de um segundo entre eles.

'''
from playsound import playsound
from time import sleep

print('=====CONTAGEM REGRESSIVA=====')

for i in range(10, -1, -1):

    print (i)
    sleep(1)

print('CHEGOU ! ! !')

playsound('C:/Users/Admin/Documents/Mundo_Python02/Aula08/SENNA.mp3')
