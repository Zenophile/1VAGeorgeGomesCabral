'''8 Peça um valor entre 100 e 200 ao usuário e apresente a soma dos valores ímpares de
0 até o valor fornecido pelo usuário.'''

n1 = int(input('Digite um valor entre 100 e 200 '))

contador = 0

for x in range(n1 - 1):
    contador += 1
    if x % 2 == 1:
        contador += x


print(contador)



