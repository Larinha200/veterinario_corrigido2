
from classes import *
from funcion import*

pets = {}       

menu()
resp=int(input("---->"))
id=1
while True:
    if resp == 1:
       menu2()
       resp2=int(input("---->"))
       if resp2 == 1:
           
        Nome= input("Insira o nome:") 
        Idade=int(input("Insira a idade:"))
        Raca=input("Insira a raça:")
        Cor=input("Insira a cor:")
        Peso=float(input("Insira o peso:"))

        pets[len(pets)]= Gato (Nome, Idade , Raca, Cor, Peso)
        print(pets)
        
       
       