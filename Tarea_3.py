numero=input("Ingresar un Numero: ")
numero=len(numero)
if(numero<=5):
    if(numero==5):
        print("el numero tiene 5 digitos")
    if(numero==4):
        print("el numero tiene 4 digitos")
    if(numero==3):
        print("el numero tiene 3 digitos")    
    if(numero==2):
        print("el numero tiene 2 digitos")  
    if(numero==1):
        print("el numero tiene 1 digitos")      
else:
    print("El Numero tiene mas de 5 digitos y tiene: ",numero )