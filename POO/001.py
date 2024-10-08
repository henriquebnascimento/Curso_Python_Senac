# Estudando POO

class Pessoa: #criando uma classe
    def __init__(self, nome, idade): # passando dois parâmetros através do método construtor init
        self.nome = nome
        self.idade = idade
        
pessoa1 = Pessoa('Maria',30) # Criando uma instancia da classe Pessoa. Instanciando, chamando a função, passando os argumentos. pessoa1 é um objeto da classe pessoa
print(pessoa1.nome)  #classe . atributo
print(pessoa1.idade)

pessoa2 = Pessoa('chico',40)
print(pessoa2.nome)
print(pessoa2.idade)


