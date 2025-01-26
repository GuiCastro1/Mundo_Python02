'''
Criado por: Gui Castro

21/01/2025

crie um programa que leia varios números inteiro e no final mostre a média, o maior e o menor. o programa so deve para quando usúario escolher parar.
'''
print('=====Media Maior & Menor=====')
para = 's'
contador = 0
media = 0
maior = 0
menor = 0

while para == 's':

    num = int(input('Digite um número:'))

    media += num

    contador += 1

    if contador == 1:
        maior = menor = num
    else:
        if num > maior :
            maior = num
        if num < menor:
            menor = num

    if contador % 5 == 0:
        para = str(input('Continuar? [N / S]')).lower()

        
print(f'Você digitou {contador}:')
print(f'O Maior número digitado foi: {maior}')
print(f'O Menor número digitado foi: {menor}')
print(f'A media dos números é:{media / contador}')
print('O programa acabou ! ! ! ! !')