
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
           
        nome= input("Insira o nome:") 
        idade=int(input("Insira a idade:"))
        raca=input("Insira a raça:")
        cor=input("Insira a cor:")
        peso=float(input("Insira o peso:"))
        pets[len(pets)+1]= Gato(nome, idade, raca, cor, peso)
        menu()
        resp=int(input("---->"))

       
        
    
    elif resp ==2:
            
        escolhida=input("digite:")

        for chave, animal in pets.items():
            if animal.getRaca().strip().lower() == escolhida:
                
                print(f"{chave}° - Nome: {animal.getNome()}")
                print(f"\tIdade: {animal.getIdade()}")
                print(f"\tRaça: {animal.getRaca()}")
                print(f"\tCor: {animal.getCor()}")
                print(f"\tPeso: {animal.getPeso()}kg\n")
        