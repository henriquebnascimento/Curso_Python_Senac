# A ESTRUTURA BÁSICA DO LAÇO WHILE É:
#while condicao:
    # bloco de código a ser executado
    
# contador = 6
# while contador >= 5:
#     print(contador)
#     contador += 1
    
# while True:
#     a = input("digite fim para sair: ")
#     print(a)
#     if a =='fim':
#         break

# while True:
#     nome = input("Digite seu nome (ou 'sair' para parar):")
#     if nome == 'sair':
#         break
#     print(f'Olá {nome}!')
        
# import random
# numero_secreto = random.randint(1,10)
# tentativa = None
# while tentativa != numero_secreto:
#     tentativa = int(input("Advinhe o número '(entre 1 e 10)':"))
    
# print('Parabéns! Você adivinhou o número.')

# contagem = 10
# while contagem > 0:
#     contagem -= 1
    
# print('Feliz Ano Novo!')    


# while True:
#     num1 = int(input('Digite um número: '))
#     num2 = int(input('Digite outro número: '))
#     operacao = input("Digite a operação (+,-,*,/) ou 'sair' para parar: ")
    
#     if operacao == '+':
#         print(f'O resultado da soma de {num1} e {num2} é: {num1 + num2}')
#     elif operacao == '-':
#         print(f'O resultado da subtração de {num1} e {num2} é: {num1 - num2}')
#     elif operacao == '*':
#         print(f'O resultado da mutiplicaçaõ de {num1} e {num2} é: {num1 * num2}')  
#     elif operacao == '/':
#         if num2 != 0:
#             print(f'O resultado da divisão de {num1} e {num2} é: {num1 / num2}')
#         else:
#             print(f'Erro. Divisão por zero.')   
#     else:
#         print("Operação inválida.")

# import random
# n = random.randint(1,20)
# while True:
#     palpite = int(input('Digite um número entre 1 e 20: '))
#     if palpite < n:
#         print('Seu palpite é menor que o número sorteado.')
#     elif palpite > n:
#         print('Seu palpite é maior que o número sorteado.')
#     else:
#         print('Parabéns! Vocé acertou.')


#Use o laço while para imprimir os números de 1 a 10.
# cont = 0
# while cont < 10:
#     cont += 1
#     print(cont)
    
    
#Escreva um programa que peça ao usuário para digitar uma senha e continuye pedindo até que ele acerte a senha correta, que é "1234".

# senha_padrao = 1234

# while True: 
#     senha = int(input('Digite sua senha: '))
#     if senha != senha_padrao:
#         print('Senha inválida! Digite a senha novamente.')
#     else:
#         print('Acesso permitido!') 
#         break 

# soma_numeros = []
# cont = 0
# while True:
#     numero = int(input('Digite um número: '))
#     soma_numeros.append(numero)
#     cont += numero
#     if numero == 0:
#         break
# print(f'A soma dos números digitados é: {cont}')

# contador = 0
# numero = 2
# while contador < 20:
#     print(numero)
#     numero += 2
#     contador += 1
    
# print(numero)

nomes = []
cont = 0
while True:
    nome = input('Digite um nome: ').lower()
    nomes.append(nome)
    cont +=1
    if nome == 'sair':
        break
print(f'Vocé digitou {cont} nomes.')
print(nomes)
    
    