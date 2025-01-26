'''
Criado por: Gui Castro

19/01/2025

Faça um programa que leia a data de nascimento de uma pessoa e informe de acordo com sua idade:

-Se ele ainda vai se alistar ao serviço militar
-Se é a hora de se alistar 
-Se ja passou do tempo de se alistar

Seu programa também deve mostrar o tempo que falta ou qu passou do prazo.
'''
from datetime import date

print('=====Alistamento=====\n')

print('Seu alistamento militar esta em dia?\n')

print('Iforme sua data de nascimento para descobrir.\n')

data = str(input("data:")).strip().upper()

remove_barra = data.replace('/','')

validacao = remove_barra.split()

ano_user = validacao[0][4:]

pega_ano = date.today().year

if len(validacao[0]) > 8 :

    print(f'A data infomada:{data} possui a mais de 8 digitos: {len(validacao[0])}\n ')

    print('Tente novamente daqui a pouco')

elif len(validacao[0]) < 8:

     print(f'A data infomada:{data} possui menos de 8 digitos: {len(validacao[0])}\n')

     print('Tente novamente daqui a pouco')

else:
        idade = pega_ano - int(ano_user)

        if idade == 18:

            print(f'Você tem : {idade} anos. Procure a junta militar mais proxima a sua região.\n')

        elif idade < 18:

            tempo =  18 - idade

            print(f'Faltam {tempo} para você fazer 18 anos\n')
            print(f'Ano do alistamento {tempo + pega_ano}\n')

        elif idade > 18:

            tempo =  idade - 18

            print(f'Já se passaram {tempo} anos desde que você completou 18 anos.\n')
            print(f'Ano de alistamento {pega_ano - tempo}\n')        

        print('O PROGRAMA ACABOU  ! ! !')

'''
Melhorias aplicadas:
Entrada clara e validação de formato:
Verifique o formato da data diretamente e evite manipulações desnecessárias.
Use regex para validações simples.
Eliminação de código redundante:
Evite duplicação de mensagens de erro.
Use estruturas claras para verificar idade.
Boas práticas:
Mensagens mais claras e bem formatadas.
Melhoria nos nomes das variáveis para torná-las mais descritivas.
Código otimizado:
python
Copiar
Editar
from datetime import date
import re

print('===== Alistamento Militar =====\n')

# Entrada da data de nascimento
data_nascimento = input("Informe sua data de nascimento (DD/MM/AAAA): ").strip()

# Verificar formato da data usando regex
if not re.match(r"^\d{2}/\d{2}/\d{4}$", data_nascimento):
    print("Erro: A data deve estar no formato DD/MM/AAAA.")
else:
    # Extrair o ano de nascimento
    dia, mes, ano = data_nascimento.split('/')
    
    try:
        ano_nascimento = int(ano)
        ano_atual = date.today().year
        idade = ano_atual - ano_nascimento

        # Calcular status de alistamento
        if idade == 18:
            print(f"Você tem {idade} anos. Procure a junta militar mais próxima da sua região.")
        elif idade < 18:
            anos_restantes = 18 - idade
            print(f"Faltam {anos_restantes} anos para você se alistar.")
        else:
            anos_atrasados = idade - 18
            print(f"Já se passaram {anos_atrasados} anos desde o prazo de alistamento.")
            print("Procure a junta militar mais próxima da sua região se ainda não se alistou.")
    except ValueError:
        print("Erro: O ano informado é inválido.")

print("\nFim do programa.")
Principais alterações:
Validação do formato da data:
Usa regex para verificar o formato correto (DD/MM/AAAA).
Separação de responsabilidades:
Cada parte do código tem uma função clara, como entrada, validação e cálculo.
Tratamento de exceções:
Use try-except para lidar com entradas inválidas.
Legibilidade:
Variáveis com nomes mais descritivos tornam o código mais fácil de entender.
Este código é mais robusto, legível e eficiente!


Melhorias aplicadas:
Entrada clara e validação de formato:
Verifique o formato da data diretamente e evite manipulações desnecessárias.
Use regex para validações simples.
Eliminação de código redundante:
Evite duplicação de mensagens de erro.
Use estruturas claras para verificar idade.
Boas práticas:
Mensagens mais claras e bem formatadas.
Melhoria nos nomes das variáveis para torná-las mais descritivas.
Código otimizado:
python
Copiar
Editar
from datetime import date
import re

print('===== Alistamento Militar =====\n')

# Entrada da data de nascimento
data_nascimento = input("Informe sua data de nascimento (DD/MM/AAAA): ").strip()

# Verificar formato da data usando regex
if not re.match(r"^\d{2}/\d{2}/\d{4}$", data_nascimento):
    print("Erro: A data deve estar no formato DD/MM/AAAA.")
else:
    # Extrair o ano de nascimento
    dia, mes, ano = data_nascimento.split('/')
    
    try:
        ano_nascimento = int(ano)
        ano_atual = date.today().year
        idade = ano_atual - ano_nascimento

        # Calcular status de alistamento
        if idade == 18:
            print(f"Você tem {idade} anos. Procure a junta militar mais próxima da sua região.")
        elif idade < 18:
            anos_restantes = 18 - idade
            print(f"Faltam {anos_restantes} anos para você se alistar.")
        else:
            anos_atrasados = idade - 18
            print(f"Já se passaram {anos_atrasados} anos desde o prazo de alistamento.")
            print("Procure a junta militar mais próxima da sua região se ainda não se alistou.")
    except ValueError:
        print("Erro: O ano informado é inválido.")

print("\nFim do programa.")
Principais alterações:
Validação do formato da data:
Usa regex para verificar o formato correto (DD/MM/AAAA).
Separação de responsabilidades:
Cada parte do código tem uma função clara, como entrada, validação e cálculo.
Tratamento de exceções:
Use try-except para lidar com entradas inválidas.
Legibilidade:
Variáveis com nomes mais descritivos tornam o código mais fácil de entender.
Este código é mais robusto, legível e eficiente!
'''