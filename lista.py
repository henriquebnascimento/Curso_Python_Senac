# declarando uma lista vazia em Python
lista1 = []
lista1 = [1,'2',3] # Criando uma lista
print(type(lista1), lista1)

# Declaração explícita de lista
lista2 = list((1,'2',3)) # quando eu uso uma palavra reservada list , estou convertendo uma tupla para uma lista
print(lista2)

lista3 = ['C', 4.65, True, "True", 'Vamos Aprender', ['outra', 'lista', 'interna'], lista2]
print(lista3[::-1])

lista4 = ['primeiro', 'segundo', 'terceiro']
print(lista4)
lista4[2] = 'praia' 
