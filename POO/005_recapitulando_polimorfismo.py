
class Animal:
    
    def  nadar (self):
        pass
        
    def  andar (self):
        pass
    
    def voar(self):
        pass    
    
class Aquaticos(Animal):
    def nadar(self):
        print('Esse animal nada')  
            
class Terreste(Animal):
    def  andar(self):
        print('Este animal anda')    

class Voadores(Animal):
    def  voar(self):
        print('Esse animal voa')
        
peixe = Aquaticos()
cavalo = Terreste()        
gaviao = Voadores()

peixe.nadar()
cavalo.andar()
gaviao.voar()

peixe.
        