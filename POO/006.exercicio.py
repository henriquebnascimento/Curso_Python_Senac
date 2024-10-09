class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        
    def exibir_informacoes(self):
        print('f"Nome: {self.__nome}, Idade:{self.__idade}')
        
pessoa = Pessoa('Alice', 30)

#Tentativa de acessar o atributo privado __nome
print(pessoa.__nome)