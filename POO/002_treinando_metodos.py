
class Pessoa():
    def __init__(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        
    def apresentar(self):
        print(f"Meu nome é {self.nome}, \ntenho {self.idade} anos. \nMeu telefone é: {self.telefone}")
        
pessoa1 = Pessoa('Maria', 39, '81 98556-1234')
pessoa2 = Pessoa('João', 41, 'Número não cadastrado.')

pessoa1.apresentar()
print(30*'_')
pessoa2.apresentar()