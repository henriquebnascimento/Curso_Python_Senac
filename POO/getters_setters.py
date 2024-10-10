# pesquisar sobre decorador @property

# class Pessoa:
#     def __init__(self, nome):
#         self.__nome = nome # estrou criando uma camada de segurança __ que proteje o acesso dessa informação fora da classe.
        
#     @property  #getteres
#     def nome(self):
#         return self.__nome
    
#     @nome.setter #setters
#     def nome(self, novo_nome):
#         if isinstance(novo_nome, str) and novo_nome.strip():
#             self.__nome = novo_nome
#         else:
#             print('nome inválido.')
            
# # Uso da classe
# pessoa = Pessoa('Alice')
# print(pessoa.nome)
# pessoa.nome = 'Bob'
# print(pessoa.nome)
# pessoa.nome = ""
        
# Exemplo de POLIMORFISMO
# class Cachorro:
#     def falar(self):
#         return 'Au Au!'
    
# class Gato:
#     def falar(self):
#         return 'Miau!'
    
# def imitar_animais(animal):
#     print(animal.falar())
# #Uso do polimorfismo
# imitar_animais(Cachorro())
# imitar_animais(Gato())

class Produto:
    def __init__(self,preco):
        self._preco = preco
        
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco_< 0:
            raise ValueError('Preço inválido. Preço não pode ser negativo.')
        self._preco = novo_preco
    
    

        