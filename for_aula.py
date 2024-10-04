# l = [1,2,3,4,5,6,7,8,9]
# for i in l:
#     print(i)
    
# for i in range(5):
#     print(i)

#_____________________________

# soma = 0
# for i in range(1,11): # gera sequència de 1 até 10
#     soma += i
#     print('i agora vale: ',i)
#     print(f'A soma parcial é: {soma}')
#     somax = 'status code 200'

# print(f'A Soma total de 1 até 10 é: {somax}')

 


# palavra = 'Python'
# cont = 0
# for i in palavra:
#     print(f'A letra {i} tem índice {cont}') 
#     cont += 1
# for i, palavra in enumerate(palavra):
#     print(palavra,"->", i)



        
# print(f'Há {contador} vogais na frase.')

# contador = 0
# for letra in frase:
#     if letra not in vogais:
#         contador += 1
        
# print(f'Há {contador} consoantes na frase.')

frase = input('Digite a frase: ')
vogais ='aeiou'
contador = 0
for letra in frase:
    if letra in vogais:
        contador += 1
        
print(f"na frase {frase}, há {contador} letras")