# Python: Curso Mundo 02 do Canal Curso em Vídeo

## Conteúdo:

### Condições Aninhadas;
### Laço de repetição For;
### Laço de repetição While.

## Condições Aninhadas

As condições aninhadas permitem criar lógicas com múltiplos caminhos utilizando `if`, `elif` e `else`.

### Exemplo:
```python
nome = str(input('Digite seu nome:'))

if nome == 'Guilherme':
    print('UaU ! ! ! ! ! ')
elif nome == 'João' or nome == 'Ana' or nome == 'Maria':
    print('Que nome comum')
elif nome in 'Manoella, Andressa, Elaine, Luciana':
    print(f'Já tive uma professora que se chamava {nome}')
else:
    print(f'Seu nome não consta no meu Banco De Dados')
```
---

## Laço com Variável de Controle

Os laços são utilizados para executar repetições enquanto uma condição for verdadeira.

### Exemplo com `for`:
O laço `for` permite iterar sobre sequências ou um intervalo definido.

```python
for i in range(1, 10):
    print(f'Passo {i}')
```

### Exemplo com `while`:
O laço `while` repete enquanto a condição é verdadeira.

#### Exemplo básico:
```python
while not maca:
    passo()
pega()
```

#### Estrutura com `while True` e `break`:
O laço infinito com `break` é usado para interromper o fluxo quando uma condição é atendida.

```python
while True:
    if chao:
        passo()
    if buraco:
        pula()
    if moeda:
        pega()
    if trofeu:
        pula()
        break
pega()
```
---

## Dicas para Aprender Programação

1. **Concentração:** Dê atenção ao que está aprendendo.
2. **Anote Tudo:** Documente cada conceito e código que aprender.
3. **Grupo de Estudo:** Estudar com outras pessoas pode ajudar a fixar o conteúdo.
4. **Ensine Alguém:** Repassar o que aprendeu solidifica o conhecimento.
5. **Pratique Muito:** Nada substitui a prática constante.
6. **Não Pule Exercícios:** Complete todos para dominar a lógica.
7. **Não Copie Respostas Antes de Tentar:** O aprendizado vem do esforço.
8. **Não Desista:** Persistência é a chave para aprender programação.

---

Essas anotações cobrem as principais técnicas e boas práticas apresentadas no módulo 2 do curso. Continue práticando e explorando os exemplos!

