'''
Criado por: Gui Castro

20/01/2025

Desenvolva um programa que leia o primeiro termo e a razão de uma PA(Progressaõ Aritimetica). No final mostre os 10 primeiros termos dessa progressão
'''
print('=====PROGRASSÃO ARIRIMÉTICA=====')

termo = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
#meu
for i in range(1, 11):

    conta = termo + (i - 1) * razao

    print(f'{conta}✂', )
#Guanabara
decimo = termo + (10 - 1) * razao

for i in range(termo, decimo + razao, razao):

    print(f'{i}✂',)
