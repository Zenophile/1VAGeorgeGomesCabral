'''1. Usando if-elif-else, faça um programa que, dependendo da nacionalidade do usuário,
imprima (br-bom dia; es-buen dia; fr-bom jour; ge-gutten morgen; outros-good
morning).'''


nacionalidade = input('Digite sua nacionalidade (br, es, fr, ge, outros) ')

if nacionalidade == 'br':
    print('bom dia')
elif nacionalidade == 'es':
    print('buen dia')
elif nacionalidade == 'fr':
    print('bom jour')
elif nacionalidade == 'ge':
    print('gutten morgen')
elif nacionalidade == 'outros':
    print('good morning')
