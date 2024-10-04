#TUPLAS

frutas = ['maça', 'banana','laranja']
frutas.append('uva')
frutas.remove('banana')
indice = frutas.index('laranja')
print(indice)
print(frutas)
frutas.reverse()
print(frutas)

# TUPLAS

cores = ('vermelho', 'verde', 'azul')
indice1 = cores.index('vermelho')
indice2 = cores.index('azul')
print(indice1 , indice2)
#cores['verde'] = 'amarelo'  # o objeto tupla não suporta atribuição de item
outras_cores = ('amarelo', 'roxo')
print(cores + outras_cores)

cor1, cor2, cor3 =  cores
print(cor1)
print(cor2)
print(cor3)

