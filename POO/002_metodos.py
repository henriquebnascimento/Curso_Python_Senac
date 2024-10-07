# MÉTODOS SÃO FUNCÕES DEFINIDAS DENTRO DE UMA CLASSE QUE DESCREVEM OS COMPORTAMENTOS DE UM OBJETO

class Pessoa: #criando uma classe
    def __init__(self, nome, idade, ano): # passando dois parâmetros através do método construtor init
        self.nome = nome
        self.idade = idade
        self.ano = ano
      
    def ano(self, ano):
        self.ano = ano
    
        
    def apresentar(self):
         print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos e nasci no ano de {self.ano}.")   
        
        
          
pessoa1 = Pessoa('Maria',39,1984 ) # Criando uma instancia da classe Pessoa. Instanciando, chamando a função, passando os argumentos. pessoa1 é um objeto da classe pessoa
print(pessoa1.nome)  #classe . atributo  (nome é um método da classe pessoa1)
print(pessoa1.idade)

pessoa1.apresentar()