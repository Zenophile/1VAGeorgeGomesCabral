'''7. Peça um valor entre 2 e 20 ao usuário e calcule o fatorial desse número.'''

n1 = int(input('digite um valor entre 2 e 20'))

if n1 <= 20 and n1 >= 2:
    resultado = 1
    for x in range(1, n1  +1):
        resultado *= x


print(resultado)
