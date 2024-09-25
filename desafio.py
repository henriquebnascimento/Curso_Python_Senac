hotel = input('Digite o nome do hotel com 6 caracteres: ')
cidade = input('Digite a cidade com 8 caracteres: ')
avaliacao = input('Digite um numero entre 1 a 5: ')
while avaliacao < 1 or avaliacao > 5:
    print('O número informado deve está entre 1 e 5')

print(20*'*')
print(f'********{hotel}********')
print(f'****{avaliacao} estrela(s)****')
print(f'******Em {cidade}*****')
print(20*'*')
