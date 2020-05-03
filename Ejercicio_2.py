sexo=input("Ingresa tu Sexo ")
if(sexo=="hombre" or sexo=="mujer"):
    edad=int(input("Ingresa tu Edad "))
    if(sexo=="mujer" and edad>=18):
        print("NO vas al bote")
    if(sexo=="mujer" and edad<18):
            print("vas al bote")
    if(sexo=="hombre" and edad>=18):
        print("ya esta peludo")
    if(sexo=="hombre" and edad<18):
            print("esta pollito")      
else:
    print("es un demonio")