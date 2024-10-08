# def saudacao(nome):
#     print(f'Olá {nome}, bem-vindo(a) à aula de funções em Python!')    
# saudacao('Henrique')


# def somar(a,b,c):
#     return a + b +c

# print(somar(10,20,18))


# def checar_numero (n):
#     if n > 0:
#         return 'Positivo'
#     elif n < 0:
#         return 'Negativo'
#     else:
#         return 'zero'
# print(checar_numero(10))

# def calculadora(a,b, operacao):
#     if operacao == '+':
#         return a + b
#     elif operacao == '-':
#         return a - b
#     elif operacao == '*':
#         return a * b
#     elif operacao == '/':
#         if b != 0:
#             return a / b
#         else:
#             return 'Erro. Não se divide número por zero'
            
# if calculadora(2,4,"*") >= 10:
#     print('maior que 10')
# else:
#     print('Menor que 10')    


# global_var = 100

# def exemplo_escopo():
#     local_var ='Estou dentro da função'
#     print(local_var)
#     print(global_var)
    
# exemplo_escopo()
# print(local_var) # erro por que está tentando acessar uma variável que só existe dentro da funçã


# def pessoa(nome="Visitante",idade=0):
#     print(f'Meu nome é {nome} e tenho {idade} anos.')

# pessoa(idade=15, nome='Jose') #ARGUMENTOS NOMEADOS
    
# def somar(*args): #utilizo quando nao sei a quantidade exata de argumentos
#     return sum(args)
# print(somar(1,2,3,4,5,6))

# def exibir_detalhe(**kwargs): #recebe mútiplos argumentos nomeados como um dicionário
#     for chave, valor in kwargs.items():
#         print(f'{chave}: {valor}')
# exibir_detalhe(nome='Carlos', idade=30, cidade ='São Paulo')


# def pessoa(**kwargs):
#     for chave, valor in kwargs.items():
#         print(f"{chave}: {valor}")
# pessoa(nome='Henrique', idade=39, cidade = 'Olinda') 

# def soma_pares(numeros): efetuar a soma dos números pares passados no argumento
#     soma = 0
#     i = 0
#     while i < len(numeros):
#         if numeros[i] % 2 == 0:
#             soma += numeros[i]
#         i += 1
#     return soma
# print(soma_pares([1,2,3,4,5,6]))

def soma(numeros):
    soma = 0
    i = 0
    while i < len(numeros):
        if numeros[i] % 2 ==0:
            soma += numeros[i]
        i += 1
    return soma
print(soma([1,2,3,4,5,6]))
print(i)
    