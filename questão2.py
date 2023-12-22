'''2. Uma empresa decidiu dar bônus aos colaboradores baseada no tempo de serviço.
• Tempo de serviço > 10 anos – 10 %
• 6 anos <= Tempo de serviço <= 10 anos – 8 %
• Tempo de serviço <= 10 anos – 5 %
Apresente o valor líquido de aumento dado o tempo de serviço e salário do
colaborador'''

tempo_servico = int(input('digite o seu tempo de serviço '))
salario = int(input('digite o seu salario'))

if tempo_servico > 10:
    aumento = salario * 0.10
    salario *= 1.10
    print('seu salario aumentou para R$',salario, 'um aumento de R$',aumento)

elif tempo_servico < 10 and tempo_servico > 6:
    aumento = salario * 0.08
    salario *= 1.08
    print('seu salario aumentou para R$',salario, 'um aumento de R$',aumento)

elif tempo_servico <= 10:
    aumento = salario * 0.05
    salario *= 1.05
    print('seu salario aumentou para R$',salario, 'um aumento de R$',aumento)
