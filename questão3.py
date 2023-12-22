'''3 Como critérios para passar em um exame o aluno deve anotar [(> 7.5 matemática) e (>
6.5 português)] ou [(> 8 redação) e (>6 matemática) e (> 8 português)]. Peça as três
notas do aluno e em apenas uma única expressão booleana avalie se o aluno passou
ou falhou no teste.'''

mat = float(input('Digite sua nota em matematica '))
pt = float(input('Digite sua nota em portugues '))
red = float(input('Digite sua nota em redação'))

if (mat > 7.5 and pt > 6.5) or (red > 8 and mat > 6 and pt > 8):
    print('Você passou no exame')
