'''
Criado por: Gui Castro

20/01/2025

Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
'''
print('=====PALÍNDROMO=====')

texto = str(input('Digite uma frase:')).strip().lower()

# remove = texto.replace(' ','')
remove = ''.join(texto.split())

lista = []
for i in remove:

    #ord é uma função que retorna o numero em assci de um caracter 

    converte_em_numero = ord(i)

    #chr é uma função que retona o caracter do numero em assci

    #converte_em_texto = chr(converte_em_numero) 

    #append é usado para inserir dados de um avariavem em uma lista 

    lista.append(converte_em_numero)

if (lista == lista[::-1]) or (remove == remove[::-1] ):
        print(f'A frase {texto}, é um PALÍNDROMO: {remove[::-1]}')
else:
        print(f'A frase {texto},NÃO é um PALÍNDROMO')

'''
frase = str(input('Digite a frase:'))
palavras = frase.split()
#join junta o split
junto = ''.join(palavras)
inverso =''

for i in range(len(junto) -1, -1, -1):
        inverso += junto[i]

if inverso == junto:
        print('p')
else:
        print('n/p')
'''