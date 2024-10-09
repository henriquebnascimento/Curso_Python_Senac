# pesquisar sobre decorador @property

class Pessoa:
    def __init__(self, nome):
        self.__nome = nome # estrou criando uma camada de segurança __ que proteje o acesso dessa informação fora da classe.
        
    @property  #getteres
    def nome(self):
        return self.__nome
    
    @nome.setter #setters
    def nome(self, novo_nome):
        if isinstance(novo_nome, str) and novo_nome.strip():
            self.__nome = novo_nome
        else:
            print('nome inválido.')
            
# Uso da classe
pessoa = Pessoa('Alice')
print(pessoa.nome)
pessoa.nome = 'Bob'
print(pessoa.nome)
pessoa.nome = ""
        