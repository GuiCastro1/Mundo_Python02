'''
Criado por: Gui Castro

20/01/2025

Refaça o desafio 09, mostrando a tabuda que o usuário escolher, só que agora usando o um laço for.
'''
print('=====TABUADA=====')

n = int(input('Digite um número para exibir a tabuada'))

print('-=' *20)

for i in range(1, 11):

    print(f'{n} x {i:2} = {n*i}')

print('-=' *20)