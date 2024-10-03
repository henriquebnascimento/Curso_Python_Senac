lista1 = []
lista1 = [1,'2',3] # Criando uma lista
print(type(lista1), lista1)

# Declaração explícita de lista
lista2 = list((1,'2',3)) # quando eu uso uma palavra reservada list , estou convertendo uma tupla para uma lista
print(lista2)

lista3 = ['C', 4.65, True, "True", 'Vamos Aprender', ['outra', 'lista', 'interna'], lista2]
print(lista3[::-1])
print(lista3[2:6:2])
print(lista3[0:])

lista4 = ['primeiro', 'segundo', 'terceiro']
print(len(lista4))

print(lista3)

#adicionando elementos em uma lista ( trabalhando com métodos)
lista1.append('Python')
lista1.append('Java')
lista1.append('Php')
lista1.append('C#')

print(lista1)

# inserir elementos em uma posição específica
lista1.insert(2, 'C++')
print(lista1)

# Remove um elemento pelo seu valor
lista1.remove('Java')
print(lista1)

#Indexação (Pegar um índice de um elemento pelo valor)
indice = lista4.index('segundo')
print(indice)
lista4[indice] = 'Laranja'
print(lista4)

#Invertendo uma lista
lista4.reverse()
print('Lista invertida: ', lista4)

# Ordenando uma lista. Pode ser em ordem alfabética, em ordem crescente

lista4.sort()
print(lista4)

lista5 = [5,4,6,8,9,7,2]
lista5.sort(reverse=True)
lista5.sort()
print(lista5)
lista5.reverse()
print(lista5)

# QUIZ 1.
a = [1,2,3] #tenho os índices 0,1,2
b = a[:] # 
b[0]= 5
print(a[3])

# QUIZ 2.

minhalista = [76,92.3, 'oi', True, 4, 76]
minhalista.append('pera')
minhalista.append(76)
minhalista.insert(3,'gato')
minhalista.insert(0,99)
indice = minhalista.index('oi')
print(indice)
minhalista.remove(True)
print(minhalista)

# QUIZ 3.
uma_lista = [4,2,8,6,5]
uma_lista = uma_lista + [['gato', 'bode', 'bola']]
print(uma_lista)

lista6 = [1,2,3]
lista7 = [5,4,3]
lista_final =  list(set(lista6+lista7)) # pega valores unicos
print(lista_final) 
