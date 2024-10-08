# MÉTODOS SÃO FUNCÕES DEFINIDAS DENTRO DE UMA CLASSE QUE DESCREVEM OS COMPORTAMENTOS DE UM OBJETO

class Pessoa: #criando uma classe
    def __init__(self, nome, idade, telefone, ano): # passando dois parâmetros através do método construtor init
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.ano = ano
      
    # def ano(self, idade):
    #     self.ano = int(2024) - int(idade)
    
              
    def apresentar(self):
        print(f"Primeiro nome: {self.nome},\nIdade: {self.idade} anos, \nTelefone: {self.telefone},\nAno de nascimento: {self.ano}.")   
        
        
          
pessoa1 = Pessoa('Henrique',39, '81 98556-1030',1984 ) # Criando uma instancia da classe Pessoa. Instanciando, chamando a função, passando os argumentos. pessoa1 é um objeto da classe pessoa
pessoa2 = Pessoa('Maria', 42, '81 98556-2145', 1975)
# print(pessoa1.nome)  #classe . atributo  (nome é um método da classe pessoa1)
# print(pessoa1.idade)


pessoa1.apresentar()
print('______________________')
pessoa2.apresentar()