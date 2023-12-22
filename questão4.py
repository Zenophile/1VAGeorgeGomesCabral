'''4. Usando um laço while, imprima cada elemento da lista [10,20,30,40,50,60] na ordem
inversa. Assuma que o número de elementos da lista é desconhecido, dessa forma, use
a função len para saber o tamanho da lista.'''


lista = [10,20,30,40,50,60]

lista.sort(reverse = True)
contador = 0
while contador < len(lista):
    print(lista[contador])
    contador += 1

print(lista)

'''Eu não entendi bem o que o senhor pediu nessa questão, por isso printei a lista inversa de duas formas diferentes
espero que pelo menos uma delas tenha atendido o que foi pedido na questão.'''

