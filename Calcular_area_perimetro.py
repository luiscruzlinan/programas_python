import random
pi=3.1416
def menu():
    print("1-Cuadrado \n 2-Triangulo \n 3-Circilo \n 4-Rectangulo")
def operaciones(opcion):
    if(opcion==1):
        cuadrado()
    if(opcion==2):
        triangulo()
    if(opcion==3):
        circulo()
    if(opcion==4):
        rectangulo()    
def cuadrado():
    lado=random.randint(1,100)
    area=lado*lado
    print("El cuadrado mide: ",lado)
    print("El area del cuadrado es:%i"%area)
    perimetro=lado+lado+lado+lado
    print("El perimetro del cuadrado es:%i"%perimetro)
def triangulo():
    base=random.randint(1,100)
    altura=random.randint(1,100)
    area=(base*altura)/2
    print("Las medidas del Triangulo son base:%i"%base, "y la altura:%i" %altura )
    print("El area del cuadrado es:%f"%area)
    perimetro=base*3
    print("El perimetro del cuadrado es:%i"%perimetro)
def circulo():
    radio=random.randint(1,100)
    area=pi *(radio ** 2)
    print("El radio del cirulo es:%i"%radio)
    print("El area del cuadrado es:%i"%area)
    perimetro=(pi*2)*radio
    print("El perimetro del cuadrado es:%i"%perimetro)
def rectangulo():
    base=random.randint(1,100)
    altura=random.randint(1,100)
    area=base*altura
    print("La base del recyangulo es:%i"%base ,"y la altura es:%i" %altura)
    print("El area del cuadrado es:%i"%area)
    perimetro=(base*2)+(altura*2)
    print("El perimetro del cuadrado es:%i"%perimetro)
menu()
ope=int(input("Ingresa tu opcion:"))
operaciones(ope)