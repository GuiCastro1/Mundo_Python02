'''
Criado por: Gui Castro

20/01/2025

Faça um programa que leia o pesso de cinco pessoas. No final mostre qual foi o maior e menor peso.
'''

print('=====MAIOR & MENOR PESO=====')
lista = []

for i in range(1,6):

    peso = float(input(f'O peso da {i}ª pessoa:'))

    lista.append(peso)
#sort cria uma nova lista ordenada e é mais facil de usar para exercicios de pegar numeros. Porém usa mais memoria por ter que criar a outra lista
'''
Quando usar:
Use sorted quando não quiser modificar o objeto original e precisar de um novo.
Use sort quando quiser modificar a lista original diretamente e economizar memória.
Principais Diferenças:
Característica	sorted	sort
Retorno	Retorna uma nova lista ordenada/	Modifica a lista original
Funciona com	Qualquer iterável	/Apenas listas
Método/Função	Função global	/Método de listas
Modifica original?	Não	/Sim

'''
lista.sort()

print(f'Menor peso: {lista[0]}')
print(f'Maior peso: {lista[-1]}')



maior = 0
menor = 0

for p in range(1, 6):

    peso = float(input(f'O peso da {p}ª pessoa:'))

    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O menor peso:{menor}')
print(f'O maior peso:{maior}')
