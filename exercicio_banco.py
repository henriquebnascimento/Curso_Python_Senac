salario = float(input('Qual seu salário? '))
valor_solicitado = float(input('Qual valor do empréstimo? '))

margem = (valor_solicitado / salario)*100

if margem <= 50.0:
    print(f"O valor de R$:{valor_solicitado:.2f} foi aprovado!")
elif margem <= 75.0:
    print(f"O pedido de R$:{valor_solicitado:.2f} está em análise!")    
else:
    print(f"O valor de R$:{valor_solicitado:.2f} não foi aprovado!")