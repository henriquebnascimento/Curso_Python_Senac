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

numeros = []
for i in range(5):
    num = float(input('Digite um número:'))
    numeros.append(num)
    
maior = 0
for num in numeros:
    if num > maior:
        maior = num
    else:
        maior = maior
        
print(maior) 
indice_do_maior =  numeros.index(maior)        
print(indice_do_maior)          

       
        
    
     

