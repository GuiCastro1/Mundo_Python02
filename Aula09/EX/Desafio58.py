'''
Criado por: Gui Castro

21/01/2025

Faça um programa que leia o sexo de um pessoa, mas só aceite  os valores "M" ou "F". Caso esteja errado, peça a digitação novamente, até ter um valor correto.
'''
print('=====VALIDAÇÃO DE DADOS=====')
    
sexo = str(input('Qual é o seu sexo? \n[M / F]:')).upper().strip()[0]
      
while sexo != 'F' and sexo != 'M':

        print('Sexo Invalido')

        sexo = str(input('Tente Novamente:')).upper().strip()
        
print('Sexo valido ! ! !')
print('O programa acabou ! ! !')

'''
G
sexo = str(input('Informe seu sexo [M / F]')).upper().strip()[0] pega só a primera letra

while sexo not in 'FfMm'

        sexo = str(input('Tente novamente'))

print('Sucesso')
'''