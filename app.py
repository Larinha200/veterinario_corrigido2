

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
        pets[len(pets)+1]= Gato(Nome=nome, Idade=idade, Raca =raca, Cor =cor, Peso=peso)
        print(pets)
        
        
       
       