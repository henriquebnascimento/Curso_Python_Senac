class Pedido():
    def __init__(self,nome, marca, modelo, ano):
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def compra(self):
        print(f"{self.nome}, parabéns pela sua compra!!\nSeu {self.marca}{self.modelo}, ano {self.ano} está sendo processado.")
        
pedido1 = Pedido('Henrique','Peugeot', '206', 2008)
pedido2 = Pedido('Maria','Fiat', 'Pálio', 2015)

pedido1.compra()
pedido2.compra()        