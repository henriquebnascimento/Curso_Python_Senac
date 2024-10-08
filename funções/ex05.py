# Crie uma função chamada saudação() que recebe um nome como parâmetro e retorna uma saudação personalizada
def saudacao(nome):
    print(f"Olá {nome}, seja bem vindo ao Curso de Python no Senac.")
    
saudacao('Henrique')

# Escreva uma função soma() que recebe dois números parâmetros e retorna a soma deles.

def soma(a,b):
    return a + b
resultado = soma(10,15)
print(resultado)

# Escreva uma função fatorial() que cebe um número inteiro positivo como parâmetro e retorna o ragorial desse número.

def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fatorial(num - 1)
        
numero = int(input("Digite um número: "))
print(f"O fatorial de {numero} é {fatorial(numero)}")
