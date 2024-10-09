# class Animal:
#     def __init__(self, nome):
#         self.nome = nome
    
#     def emitir_som(self):
#         print(f"{self.nome} diz: barulho!")
        
# class Cachorro(Animal):
#     pass
# class Gato(Animal):
#     pass

# dog = Animal('Rex')
# cat = Animal('Tom')

# dog.emitir_som()
# cat.emitir_som()



class Automovel:
    def __init__(self, veiculo, marca='Toyota', modelo='2010'):
        self.veiculo = veiculo
        self.marca = marca
        self.modelo = modelo
                  
    def compra(self):        
        print(f"O pedido de compra do(a) {self.veiculo} {self.marca}, ano {self.modelo} está sendo separado na pátio.") 
        
class Carro(Automovel):
    pass
    
class Motos(Automovel):
    pass

carro = Automovel('Honda','Civic', 2024)
moto = Automovel('Yamaha', 'Lander', 2026)  
carro.compra()
moto.compra()