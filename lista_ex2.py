# criar uma lista com 5 notas e depois imprima a media geral
# notas = []
# for i in range(5):
#     nota =  float(input('Digite a nota do aluno: '))
#     notas.append(nota)
    
# media = 0

# for nota in notas:
#     media = media + nota
 
# media = media / 5
# print(f'A média geral é:{media}')    

# valores_produtos = []
# soma = 0
# for i in range(5):
#     preco_unitario = float(input('Digite o valor do produto: '))
#     valores_produtos.append(preco_unitario)
#     soma = soma + preco_unitario

# print(f'Você digitou os seguintes valores: {valores_produtos}.')   
# print(f'A soma total dos produtos é :{soma}') 

# numeros = []
# for i in range(5):
#     num = float(input('Digite um número:'))
#     numeros.append(num)
    
# maior = 0
# for num in numeros:
#     if num > maior:
#         maior = num
#     else:
#         maior = maior
        
# print(maior) 
# indice_do_maior =  numeros.index(maior)        
# print(indice_do_maior)          


# Exercício de string
# entrada = input('Digite uma string: ')
# resultado = ''

# for letra in entrada:
#     if not(letra in "aeiouAEIOU"):
#         resultado = resultado + letra
    
# print("Resultado: ", resultado)   
       
# lista_notas = []
# for i in range(5):
#     nota = float(input('Digite o valor dos produtos: '))
#     lista_notas.append(nota)
    
# media = 0
# for nota in lista_notas:
#         media = media + nota

# maior = 0
# for nota in lista_notas:
#     if nota > maior:
#         maior = nota
#     else:
#         maior = maior
    
# media = media / 5
# print(f'O maior valor informado foi: {maior}')

# print(f'A média geral do aluno é: {media}')

# lista =['Caju', 'Laranja', 'Banana','Uva']
# cont = 1
# for fruta in lista:
#     print(cont, fruta)
#     cont += 1
    
# lista[-1] = 'Laranja'
# lista[2] = 'Uva'
# print(lista)
# lista.append('Melancia')
# print(lista)
# lista.remove('Melancia')
# print(lista)

# del lista[2]
# print('deletando pelo índice3',lista)

# lista.sort()
# print(lista)
# lista.reverse()
# print(lista)

# lista = [2, 28, 9, 'league of legends', 78, 12]
# lista[0] = 33 # atribui 33 ao índice 0
# print(lista)
# lista[-1] = 'teste'
# print(lista)
# lista[3] = 99
# print(lista)

# a= [1,2,3,4,5]
# print(a[0]) # 1
# print(a[2]) # 3
# print(a[-1]) # 5
# print(a[-3]) # 3
# print(a[:1]) # 1
# print(a[:3]) # 1,2,3
# print(a[1:4:2]) # 2,4
# print(a[::-1]) # 5,4,3,2,1


# lista_servidores = []
# for i in range(5):
#     servidor = input('Digite o nome do servidor: ')
#     lista_servidores.append(servidor)  
      
# cont = 0
# for servidor in lista_servidores:
#         cont += 1
#         print(f'Lista de servidores: {cont, servidor}')  
           
# print(f'O total de servidores informado é: {cont}')  

# lista_servidores.reverse()
# for i, servidor in enumerate(lista_servidores):
#     print(i +1, '->', servidor)

# frase = input('Digite qualquer frase: ').lower()
# letra = 'e'
# cont = 0
# for i in frase:
#     if i in letra:
#         cont += 1
        
# print(f'Na frase informada, encontramos {cont} correspondência com critério informado.')
 
# a = [1,2,3]
# b = a
# a.append(4)
# print(b)
# a = b
# b.append('Eu') 
# print('Aqui é a: ',a)
# print(b)

# USANDO O MÉTODO EXTEND /  INSERE UMA LISTA EM OUTRA LISTA
# lista = [1,2]
# lista.extend([3,4])
# print(lista)

# CONTANDO QUANTAS VEZES UM ELEMENTO APARECE NUMA LISTA

# lista2 = [1,2,3,1,8,12,7]
# print(lista2.count(1))

# RETORNA O ÍNDICE DA PRIMEIRA OCORRÊNCIA

# lista2 = [1,2,3,1,8,12,7]
# print(lista2.index(8))  # SE O VALOR NÃO EXISTIR NA LISTA, IRA SER APRESENTADO UM ERRO.

# INSERINDO UM ITEM NUMA LISTA
# lista = [2,4,6,8,10]
# print(lista)
# lista.insert(0,'aqui é o primeiro')
# print(lista)

# # REMOVE UM ELEMENTO DA POSIÇÃO INDICE E O RETORNA
# novaLista = [1,2,3,4]
# novaLista.pop(1)
# del novaLista[1]
# novaLista.pop()
# print(novaLista)

# USANDO O MÉTODO SPLIT

# frase = 'wwww.eupodiatamantando.com'
# fraseSeparada = frase.split('.')
# print(fraseSeparada)

# frase = '12:58:13'
# fraseSeparada = frase.split(':')
# # print(fraseSeparada)
# print(f'{fraseSeparada[0]} horas')
# print(f'{fraseSeparada[1]} minutos')
# print(f'{fraseSeparada[2]} segundos')
# print(f'{fraseSeparada[0]}h'+f'{fraseSeparada[1]}m'+f'{fraseSeparada[2]}s')

# CRIANDO LISTAS DE COMPRESSÃO

# lista1 = [1,2,3,4,5,6,7,8,9]
# lista_ao_quadrado = [x**2 for x in lista1]
# print(lista_ao_quadrado)

# lista = []
# for i in range(1,11):
#     lista.append(i)
#     quadrado = [x**2 for x in lista]
    
# print(quadrado)

# CRIANDO LISTAS COM EXPRESSÃO E COM CONDIÇÃO
# lista = []
# for i in range(1,11):
#     lista.append(i)
#     quadrado = [x**2 for x in lista if x%2 ==0]
    
# print(quadrado)

# pessoa = {
#     'nome': 'Henrique',
#     'idade': 39
# }
# print(pessoa)


# def saudacao (nome):
#     print(f'Olá {nome}! Bem vindo ao Curso de Python.')
    
# saudacao(nome='Henrique')

# def soma(a, b):
#     return a + b
# resultado = soma(10,50)
# print(resultado)

# def saudacao (nome='Visitante'):
#     print(f'Olá {nome}!')
    
# saudacao('Pedro')


# def soma(*numeros):
#     total = 0
#     for numero in numeros:
#         total += numero
#     return total
# resultado = soma(1,2,3,4)
# print(resultado)

# def calculadora(a, b, operacao = '+'):
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
#             return 'Erro. Não pode dividir por zero.'
#     elif operacao =='**':
#         return a**a and b**b
#     else:
#         print('Erro. operação inválida.')
# resultado = calculadora(2,4,'**')
# print('O resultado é: \n',resultado)

# def mostrarLinhas(msg, txt):
#     print('_'*30)
#     print(msg)
#     print('_'*30)
#     print(txt)
#     print('_'*30)   
    
# mostrarLinhas('      Funções em Python', '    Outra coisa adicionada')

# def soma(a,b):
#     return a + b
# print(soma(10,20))

# def area(l, c):
#     return l * c

# print(f'A área do terreno  é: {area(10,20)}cm²')


# def maior(*argumentos):
#     if not argumentos: #verifico se não for passado nenhum argumento
#         return 'Não foi passado nenhum valor.'
#     return sorted(argumentos)
# print(maior(1,3,5,7,9,17,4))
# MANIPULAÇÃO DE SEQUÊNCIA
def maior_valor():
    return max([1,2,3,4,5])
print(f'Maior valor é: {maior_valor()}')

def menor_valor():
    return min([5,4,3,2,1])
print(f'Menor valor é: {menor_valor()}')
