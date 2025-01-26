'''
Criado por: Gui Castro

23/01/2025

Crie um programa que leia o sexo e idade de várias pessoas.A cada pessoa o usúario deve responder se deseja continuar. No final mostre:

Quantas pessoas tem mais de 18 anos; 

Quantos homens foram cadastrados; 

Quantas mulheres com menos de 20 anos foram cadastradas.
'''
maiores = homem = mulher_menor = 0

while True:

    idade = int(input('Digite a idade:'))
    sexo =' '

    while sexo not in 'FM':

        sexo = str(input('Sexo [M / F]')).strip().upper()[0]

    if idade >= 18:

        maiores +=1

    if sexo == 'M':

        homem += 1

    if sexo == 'F' and idade  <=  18:

        mulher_menor +=1

    continuar = ' '

    while continuar not in 'SN':

        continuar = str(input('Deseja continuar [S / N]')).strip().upper()[0]
    
    if continuar == 'N':
        break
    
print(f'Você registrou {maiores} maiores de 18')
print(f'Você registrou {homem} homens')
print(f'Você registrou {mulher_menor} mulheres menores com menos de 18')
