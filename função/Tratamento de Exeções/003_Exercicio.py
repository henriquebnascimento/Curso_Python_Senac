lista_numeros = []
cont= 0
total_indice = len(lista_numeros)
while True:
    numero = input(f"Digite qualquer número pra adicionar na lista ou digite 'sair' para parar: ")
    if numero == 'sair':
        break
    else:
        lista_numeros.append(numero)
        cont += 1
    
print(f"Exibindo sua lista: {lista_numeros}")
print('Infome o índice que deseja acessar: ')
indice_escolhido = int(input())
try:
    indice_escolhido > total_indice
    
except IndexError:
    print('O valor informado não correnponde à nenhum índice da lista')
else:
    print(f"O elemento correspondente ao índice {indice_escolhido} é: {lista_numeros[indice_escolhido]}")
finally:
    print('Programa finalizado')
