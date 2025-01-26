# Condições Aninhadas em Python

As condições aninhadas permitem criar lógicas com múltiplos caminhos utilizando `if`, `elif` e `else`. Esse tipo de estrutura é ideal para lidar com situações em que existem diversas condições possíveis.

## Regras Gerais

- O `if` pode ser usado sozinho, sem a necessidade de incluir um `else`.
- O `elif` **não pode ser usado sem um `if`**. Ele funciona como uma alternativa intermediária entre `if` e `else`, permitindo adicionar quantas condições forem necessárias.
- O `elif` pode substituir o `else` e ser usado diversas vezes na mesma estrutura.

---

## Exemplo de Uso

## Condições Aninhadas

## Exemplo 1: Verificação de Triângulos

Este programa verifica se três segmentos de reta podem formar um triângulo e, se possível, identifica o tipo de triângulo.

```python
# Importa a biblioteca time para usar a função sleep (simula um processamento)
from time import sleep

print('=====Pode ser um triângulo? Qual?=====')

# Solicita ao usuário os comprimentos dos três lados do triângulo
l1 = float(input('Digite o valor da primeira reta:'))
l2 = float(input('Digite o valor da segunda reta:'))
l3 = float(input('Digite o valor da terceira reta:'))

# Verifica se os lados podem formar um triângulo usando a desigualdade triangular
if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
    print(f'AS Retas {l1}, {l2} e {l3} podem formar um triângulo')

    print('PROCESSANDO. . .')
    sleep(2)  # Simula um tempo de processamento

    # Verifica o tipo de triângulo
    if l1 == l2 == l3:  # Todos os lados iguais
        print('Equilátero = todos os lados iguais')
    elif (l1 == l2) or (l1 == l3) or (l2 == l3):  # Dois lados iguais
        print('Isósceles = Dois lados iguais')
    elif l1 != l2 != l3 != l1:  # Todos os lados diferentes
        print('Escaleno = Todos os lados diferentes')

else: 
    # Caso as retas não possam formar um triângulo
    print(f'As retas {l1},{l2} e {l3} NÃO PODEM formar um triângulo')
```

## Exemplo 2: Jokenpô (Pedra, Papel e Tesoura)

Este programa simula o jogo Pedra, Papel e Tesoura (Jokenpô), permitindo que o usuário jogue contra o computador.

```python
# Importa as bibliotecas necessárias
from random import randint  # Para gerar escolhas aleatórias para o computador
from time import sleep  # Para criar intervalos entre as mensagens
import emoji  # Para adicionar emojis nas escolhas

print('=====JOKENPÔ=====')

# Pergunta ao jogador se ele quer jogar
start = str(input('Você quer jogar? (y/n) 😈😈😈\n')).strip().upper()

if start == 'Y':
    print('''
    0- PEDRA
    1- PAPEL
    2- TESOURA\n''')

    # Recebe a escolha do jogador
    jogador = int(input(':'))

    # Define as opções com emojis
    escolhas = [
        emoji.emojize(":black_circle:"),  # Pedra
        emoji.emojize(":page_facing_up:"),  # Papel
        emoji.emojize(":scissors:")        # Tesoura
    ]
    
    # Escolha aleatória do computador
    computador = randint(0, len(escolhas) - 1)

    # Simula o "Jo-Ken-Pô"
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ ! ! !')

    # Verifica o resultado do jogo
    if jogador == computador:
        # Empate
        print('-=' * 25)
        print('EMPATE')
        print(f'Computador: {escolhas[computador]}')
        print(f'Você: {escolhas[jogador]}')
        print('-=' * 25)

    elif (jogador == 0 and computador == 1) or (jogador == 1 and computador == 2) or (jogador == 2 and computador == 0):
        # Computador vence
        print('-=' * 25)
        print('PERDEU')
        print(f'Computador: {escolhas[computador]}')
        print(f'Você: {escolhas[jogador]}')
        print('-=' * 25)

    else:
        # Jogador vence
        print('-=' * 25)
        print('GANHOU ! ! !')
        print(f'Computador: {escolhas[computador]}')
        print(f'Você: {escolhas[jogador]}')
        print('-=' * 25)

else:
    # Caso o jogador não queira jogar
    print('O jogo acabou ! ! ! ! !')
```



## Exemplo 3: Verifica a idade do usúario

```python
idade = int(input('Digite sua idade:'))

if idade < 18:
    print('Você é menor de idade.')
elif 18 <= idade < 65:
    print('Você é adulto.')
elif idade >= 65:
    print('Você é idoso.')
else:
    print('Idade inválida.')
```

---

## Boas Práticas

1. **Priorize a clareza:** Evite criar condições muito complexas. Caso necessário, divida em funções.
2. **Evite redundâncias:** Se uma condição já foi atendida, não há necessidade de verificar novamente.
3. **Adicione mensagens claras:** Certifique-se de que os `print` ou retornos expliquem o resultado da condição.

---

Com essas informações, você pode criar estruturas condicionais eficientes e organizadas em seus programas Python!



Esses exemplos mostram a aplicação prática de condições aninhadas para resolver problemas e criar interatividade em Python.

