# Entrada de dados

salarioBase =  float(input('Salário base: '))
gratificacao = float(input('Gratificação: '))
desconto = 150
# Processamento
remuneracao = salarioBase + gratificacao
salario_liquido = remuneracao - desconto

# Saída
print(f'O valor do salário bruto é R$: {salario_liquido:.2f}')

