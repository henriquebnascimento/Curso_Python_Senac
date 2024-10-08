valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp =  str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
    
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse = True)
print(valores)
if 5 in valores:
    print('O número 5 consta na lista.')
else:    
    print('O número 5 não foi encontrado na lista')