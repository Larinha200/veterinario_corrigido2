from app import *
from classes import *
from funcion import*

pet1 = {}       

menu()
resp=int(input("---->"))
id=1
while resp !=0:
    if resp == 1:
       if resp == 1:
           
        Nome= input("Insira o nome:") 
        Idade=int(input("Insira a idade:"))
        Raca=input("Insira a raça:")
        Cor=input("Insira a cor:")
        Peso=float(input("Insira o peso:"))

        pet1[Nome]= Gato (Nome, Idade, Raca, Cor, Peso)
        x = pet1[Nome]
        print(x.getNome())
        print(x.getIdade())
        print(x.getRaca())
        print(x.getCor())
        print(x.getPeso())

       
       