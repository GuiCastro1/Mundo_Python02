'''
Criado por: Gui Castro

21/01/2025

Crie um programa que leia um termo e calcule a sequncia de fibonacci até esse mesmo termo

'''
print('=====FIBONACCI=====')

# termo = int(input('Digite o termo:'))

# fibonacci = [0 ,1]

# for i in range(0, termo -2):

#     valor_termo = fibonacci [-1] + fibonacci [-2]

#     fibonacci.append(valor_termo)

# print(f'O termo {termo} da sequência de fibonacci é:{fibonacci[-1]}')

# while len(fibonacci) < termo:

#     valor_termo = fibonacci [-1] + fibonacci[-2]
#     fibonacci.append(valor_termo)

# print(f'O termo {termo} da sequência de fibonacci é:{fibonacci[-1]}')

t = 13

n = 0
nn = 1

c = 0

while c < t-2:

    nnn = n + nn

    print(nnn)

    n = nn
    nn = nnn

    c += 1

    #''''deslocamento'''''