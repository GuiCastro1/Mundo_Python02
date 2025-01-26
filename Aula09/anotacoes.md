# Laços WHILE

---

### Diferença entre FOR e WHILE

- **FOR**: Usado quando sabemos o número de iterações. Utiliza uma variável de controle e um intervalo definido.
- **WHILE**: Usado quando o número de iterações depende de uma condição. Continua até que a condição se torne falsa.

---

### Boas práticas do PEP 8 para WHILE
1. Use nomes de variáveis descritivos.
2. Evite loops infinitos a menos que o comportamento seja intencional (e finalize-os com `break`).
3. Garanta que a condição do `while` eventualmente se tornará falsa.
4. Utilize indentação e espaçamento corretos.

---

### Exemplos e Explicações

#### Exemplo 1: Comparando FOR e WHILE

```python
# FOR com range
for i in range(1, 11):
    print(i, end=' ')

print('FIM')

# WHILE com controle semelhante ao FOR
i = 1
while i < 11:  # Enquanto i for menor que 11
    print(i, end=' ')
    i += 1  # Incrementa a variável

print('FIM')
```

#### Exemplo 2: Soma de números até o usuário encerrar

```python
# Soma dos números inseridos até digitar 0
n = 1  # Variável inicial
soma = 0

while n != 0:
    n = int(input('Digite um número (0 para sair): '))
    soma += n  # Soma os números

print(f'A soma de todos os números é: {soma}')
```

#### Exemplo 3: Repetição condicional

```python
# Pergunta ao usuário se deseja continuar
continuar = 'S'

while continuar == 'S':  # Enquanto o usuário digitar 'S'
    print('Ebaaaa ! ! !')
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()

print('FIM')
```

#### Exemplo 4: Loop infinito controlado por `break`

```python
# Contador até 100 usando WHILE e `break`
contador = 0

while True:  # Loop infinito
    contador += 1
    print(contador)

    if contador == 100:  # Condição para sair
        break
```

#### Exemplo 5: Soma controlada por um valor específico

```python
# Soma de números até o usuário digitar 999
soma = 0
print('Digite 999 para exibir a soma')

while True:
    num = int(input('Digite um número: '))

    if num == 999:  # Condição de parada
        break
    
    soma += num  # Soma os números

print(f'A soma é: {soma}')
```

#### Exemplo 6: Jogo da Adivinhação

```python
# Importa as bibliotecas
from time import sleep
from random import randint
from playsound import playsound

print('===== JOGO DA ADIVINHAÇÃO =====')
print('TENTE ADIVINHAR EM QUE NÚMERO ESTOU PENSANDO ENTRE 1 E 10')
#Pergunta se o jogador
jogar = input('Você quer jogar? [Y/N] 😈😈😈: ').strip().upper()[0]
#Valida se a resposta e sim, se não o jogo acaba.
if jogar == 'Y':
    #pega valor do usúario
    resposta = int(input('Digite um número: '))
    #Inicia o contador de tentativas
    tentativas = 0
    #Usa o randint sortear um número aleatório
    numero_computador = randint(1, 10)
    #O laço começa o jogo e só acaba quando a resposta é igual o número do computador
    while resposta != numero_computador:
        # Efeito de processamento
        for i in range(1, 4):
            print(f'PROCESSANDO{i * "."}')
            sleep(0.3)
        #Da uma dica para o usúario se o número e maior ou menor
        if resposta > numero_computador:
            print('MENOS ...')
        elif resposta < numero_computador:
            print('MAIS ...')
        #Exibe o erro e a bilioteca playsound toca um audio de risada
        print('Você ERROU ! ! ! Tente Novamente 😈😈😈')
        playsound('C:/Users/Admin/Documents/Mundo_Python02/Aula08/zoioconriga.mp3')

        resposta = int(input('Digite um número: '))
        tentativas += 1
    #exibe a vitória e o playsound toca a música de chegada do SENNA
    print(f'Você GANHOU! 😤😤😤')
    print(f'Tentativas: {tentativas}')
    playsound('C:/Users/Admin/Documents/Mundo_Python02/Aula08/SENNA.mp3')

else:
    print('Talvez na próxima! 😤😤😤')
```

#### Exemplo 7: Jogo Ímpar ou Par

```python
# Importa as bibliotecas
# Importando randint para gerar números aleatórios e playsound para tocar som
from random import randint
from playsound import playsound

# Exibindo o título do jogo
print("===== Jogo do ÍMPAR OU PAR =====")

# Inicializando o contador de vitórias consecutivas
contador = 0

# Início do loop principal do jogo
while True:
    # O computador escolhe um número aleatório entre 1 e 100
    num_computador = randint(1, 100)
    
    # Pergunta ao jogador se ele escolhe "Par" ou "Ímpar"
    par_impar = input("Par ou Ímpar? [P/I]: ").strip().upper()

    # Validação da entrada: garante que o jogador insira apenas "P" ou "I"
    while par_impar not in "PI":
        par_impar = input("Opção inválida! Par ou Ímpar? [P/I]: ").strip().upper()

    # O jogador escolhe um número
    num = int(input("Escolha um número: "))
    
    # Calcula a soma dos números escolhidos pelo jogador e pelo computador
    soma = num + num_computador
    
    # Determina se a soma é "PAR" ou "ÍMPAR"
    resultado = "PAR" if soma % 2 == 0 else "ÍMPAR"
    
    # Verifica se o jogador venceu com base na escolha dele e no resultado
    venceu = (par_impar == "P" and soma % 2 == 0) or (par_impar == "I" and soma % 2 == 1)

    # Exibe os resultados da rodada
    print(f"\nVOCÊ: {num} | COMPUTADOR: {num_computador} | TOTAL: {soma} ({resultado})")
    
    # Caso o jogador tenha vencido
    if venceu:
        contador += 1  # Incrementa o contador de vitórias
        print(f"Você GANHOU! Vitórias consecutivas: {contador}\n")
        playsound("Aula08/SENNA.mp3")  # Toca um som de celebração
    else:
        # Caso o jogador tenha perdido
        print(f"Você PERDEU! Total de vitórias: {contador}")
        break  # Encerra o loop e o jogo

```

