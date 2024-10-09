# class Pessoa:
#     def __init__(self, nome, idade):
#         self.__nome = nome
#         self.__idade = idade
        
#     def exibir_informacoes(self):
#         print('f"Nome: {self.__nome}, Idade:{self.__idade}')
        
# pessoa = Pessoa('Alice', 30)

# #Tentativa de acessar o atributo privado __nome
# print(pessoa.__nome)

class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.idade = idade
        
    @property  # converte meu método em um atribulto e esse método é um gettres, (só pega a informação)
    def nome(self):
        return self.__nome  
    
  
        
    def exibir_informacoes(self):
        print('f"Nome: {self.__nome}, Idade:{self.__idade}')
        
pessoa = Pessoa('Alice', 30)

#Tentativa de acessar o atributo privado __nome
print(pessoa.nome) # é um método sendo acessado como um atribulto, pois estou utilizando o propery
print(pessoa.idade) # atribulto
pessoa.exibir_informacoes() # método 
