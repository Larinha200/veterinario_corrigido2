class Animal():
    def __init__(self,Nome, Idade, Raca, Cor, Peso):
        self.__nome = Nome 
        self.__idade= Idade
        self.__raca= Raca
        self.__cor= Cor
        self.__peso= Peso


    def getNome(self):
        return self.__nome
    
    def getIdade(self):
        return self.__idade
    
    def getRaca(self):
        return self.__raca
    
    def getCor(self):
        return self.__cor
    
    def getPeso(self):
        return self.__peso
    

class Cachorro(Animal):
    def latir(self):
        print(" au au ")
    
class Cavalo(Animal) :
    def som(self):
        print("irrirrirrirri")

class Gato(): 
    def mia(self):
        print("miau miau")