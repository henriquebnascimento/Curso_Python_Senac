class Animal:
    # def __init__(self, nome):  o método construtor não precisou ser utilizado pois não tinham atributos/características para serem compartilhados com as subclasses.
    #     self.nome = nome
    
    def emitir_som(self):
        print(f"{self.nome} diz: barulho!")
        
    def fazer_som(self):
        pass
            
class Cachorro(Animal):
    def fazer_som(self):
        print('Au Au!') #criando uma forma diferente pra classe se comportar. pois na classe fazer_som não faz nada
class Gato(Animal):
    def fazer_som(self):
        print('Miau!')

# dog = Animal('Rex')
# cat = Animal('Tom')

# dog.emitir_som()
# cat.emitir_som()
animais = [Cachorro(), Gato()]
for animal in animais:
    animal.fazer_som()