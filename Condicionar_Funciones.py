import random
def suma(num1,num2):
    suma=num1+num2
    print("La Suma es:%i"%suma)
def resta(num1,num2):
    resta=num1-num2
    print("La Resta es:%i"%resta)
def multi(num1,num2):
    multi=num1*num2
    print("La Multiplicaiones  es:%i"%multi)
def divicion(num1,num2):
    divicion=num1/num2
    print("La Divicion es:%F"%divicion)
def menu():
    print("1-suma \n 2-Resta \n 3-Multiplicaion \n 4-Divicion ")
def operaciones(opcion):
    if(opcion==1):
        suma(num1,num2)
    if(opcion==2):
        resta(num1,num2)
    if(opcion==3):
        multi(num1,num2)
    if(opcion==4):
        divicion(num1,num2)
    
menu()
num1=random.randint(1,10)
num2=random.randint(1,10)
opcion=int(input("opcion: "))
operaciones(opcion)