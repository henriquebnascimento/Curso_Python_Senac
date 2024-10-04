# Escreva um programa que imprima os números de 1 até 10 usando um laço.
# for i in range(1,11):
#     print(i)
#****************************************************
# Escreva um programa que some dotos os números de 1 a 50 e imprima o resultado.  
# cont = 0
# soma = 0
# for i in range(1,51):
#     soma = soma + i
#     cont += 1
    
# print(f'A soma dos números de 1 até 50 é: {soma}') 
#***************************************************
# Esscreva um programa que SOLICITE  um número e exiba a tabuada

# tabuada = int(input('Informe qual tabuada quer imprimir: '))
# for i in range(11):
#     print(f'{tabuada} x {i} = {tabuada*i}')

#***************************************************

# for i in range(21):
#     if i % 2 == 0:
#         print(i)

#***************************************************
# frase = 'Python é divertido'

# contador = 0
# for letra in frase:
#     contador += 1 

# print(f'Na frase informada, tem {contador} letras')

#***************************************************
# Escreva a lista abaixo na ordem inversa
# lista = [1,2,3,4,5]
# print(lista)
# #lista na ordem inversa
# lista.reverse()
# print(lista)
#***************************************************

# Escreva um programa que receba um numero interio n do usuário e imprima todos os números primos menos que n;
# n = int(input("Digite um número inteiro: ")) 

# for num in range(2, n):
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             break
#     else:
#         print(num)


#***************************************************
# Escreva um programa que imprima dodos os quadrados perfeitos de 1 a 100;
# for i in range(1,11):
#     quadrado_perfeito = i**2
#     print(quadrado_perfeito)
    
# Dada uma string qualquer fornecida pelo usuário, use um laço for para contar quantas vogais e contoantes existem na string
# frase = input('Digite uma frase: ').lower()
# frase_separada = frase.split()
# print(frase_separada)
# cont = 0
# for palavras in frase_separada:
#     cont += 1
    
# print(f'O total de palavras que a frase possui é :{cont}')  

#***************************************************
# Escreva um programa que verifique, dentro de um intervalo fornecido pelo usuário, (por exemplo, de 10 a 200), quais números são políndromos.

#travei aqui

#***************************************************
# Escreva um programa que gere um número aleatório entre 1 e 20. 
# O usuário deve tentar advinhar esse número, e o programa deve informar se o palpite é maior ou menor do que o 
# número sorteado, ate que ele acerte. (pesquisar por random)
import random

numero = random.randint(1, 20)

while True:
    palpite = int(input("Adivinhe o número entre 1 e 20: "))
    if palpite == numero:
        print("Parabéns! Você acertou!")
        break
    print("Muito baixo!" if palpite < numero else "Muito alto!")

     

        
    
    
        
        
