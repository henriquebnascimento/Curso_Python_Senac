# Tratando erros / exceções

# resultado = 10/0
# print(resultado)
try:
    resultado = 10/0
    
except ZeroDivisionError:
    print('Erro: Divisão por zero não é permitida')
except NameError:
    print('Erro: Divisão por letra não é permitida')
    
else: #aqui pode ser usado também o finally que tera um código que será sempre executado
    print(f'O resultado é {resultado}') # se não houver erro na execução do código, irá ser mostrado o else.