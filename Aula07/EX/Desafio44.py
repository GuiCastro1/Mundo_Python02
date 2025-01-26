'''
Criado por: Gui Castro

19/01/2025

Desenvolva uma lógica que leia o peso de uma pessoa, calcule se IMC e mostre o status, de acordo com a tabela:

-Abaixo de 18.5: Abaixo do peso 
-Entre 18.5 e 25.0 : Peso ideal 
-25.0 até 30.0 : Sobrepeso
-30.0 até 40.0 : Obesidade
-Acima de 40.0 : Obesidade mórbida
'''
print('=====Calculadora de IMC=====')

altura = float(input('Digite sua altura:'))
peso = float(input('Digite seu peso:'))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC é:{imc:.1f}. Você está abaixo do peso.')

elif imc >= 18.5 and imc <= 25.0:
    print(f'Seu IMC é:{imc:.1f}. Você está dentro do peso ideal')

elif imc >= 25.0 and imc <= 30.0:
    print(f'Seu IMC é:{imc:.1f}. Você está acima do peso')

elif imc >= 30.0 and imc <= 40.0:
    print(f'Seu IMC é:{imc:.1f}. Você está com Obesidade')
    
else:
    print(f'Seu IMC é:{imc:.1f}. Você está com Obesidade Mórbida')
