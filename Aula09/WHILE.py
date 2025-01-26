# for i in range(1, 11):
#     print(i, end=' ')

# i = 1
#SEI LIMITE FOR E WHILE
#NÃO SEI WHILE
# while i != 11 or i < 11:

#     print(i, end=' ')

#     i+=1
# print('FIM')
# n = 1
# s = 0
# while n != 0:

#     n = int(input('Digite um número:'))
    
#     s+=n

# print(f'A soma de todos os numeros é:{s}')

# s = 'S'

# while s == 'S':

#     print('Ebaaaa ! ! !')

#     s = str(input('Deseja continuar? [S / N]')).upper()

# print('FIM')


# contador = 0

# while True:
#     contador += 1
#     print(contador)

#     if contador == 100:

#         break

soma  = 0
print('Digite 999 para exibir soma')
while True:
    num = int(input('Digite um número'))

    if num == 999:
        break
    else:
        soma += num

print(soma)