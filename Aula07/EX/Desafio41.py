'''
Criado por: Gui Castro

19/01/2025

Crie um programa que leia a nota de um aluno e calcule sua média, mostrando um amensagem no final, de acordo com a meta atingida:

-Média abaixo de 5.0 = Reprovado
-Média entre 5.0 e 6.9 = Recuperação 
-Média 7.0  ou superior = Aprovado
'''
print('=====Média=====\n')

print('Digite as notas do aluno:\n')

n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
n3 = float(input('Terceira nota:'))
n4 = float(input('Quarta nota:'))

media = (n1 + n2 + n3 + n4) / 4

if media < 5.0:

    print(f'Aluno REPROVADO, Média:{media}')

# 7 > media >= 5.0 Tambem e valido
elif media >= 5.0 and media <7:
    
    print(f'Aluno e RECUPERAÇÂO, Média:{media}')

else:

    print(f'Aluno APRVADO, Média:{media}')
    