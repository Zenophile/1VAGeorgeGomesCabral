'''6. Faça um programa que peça dois valores inteiros entre 2 e 15 ao usuário e apresente
todos os valores entre 1 e 1000 que são simultaneamente divisíveis por ambos os
valores fornecidos pelo usuário.'''

n1 = int(input('digite um valor entre 2 e 15'))
n2 = int(input('agora digite outro valor entre 2 e 15'))

if n1 >= 2 and n1 <= 15 and n2 >=2 and n2 <= 15:
    for x in range(1, 1000):
        if x % n1 == 0 and x % n2 == 0:
            print(x)
else:
    print('Reinicie o programa; ambos os valores devem ser entre 2 e 15, por favor')
