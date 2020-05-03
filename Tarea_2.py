Nombre=input("Ingresa Tu Nombre ")
Carrera=input("Ingresa Tu Carrera ")
materia1=int(input("Ingresa la Calificacion 1 "))
materia2=int(input("Ingresa la Calificacion 2 "))
materia3=int(input("Ingresa la Calificacion 3 "))
materia4=int(input("Ingresa la Calificacion 4 "))
materia5=int(input("Ingresa la Calificacion 5 "))
promedio=(materia1+materia2+materia3+materia4+materia5)/5
print("Tu Nombre es: "+ Nombre)
print("El promedio es: ",promedio)
if(promedio != 0):
    if( promedio<=10 ):
        if(promedio==10):
            print("Tu Calificacion es: A ")
        if(promedio>=9 and promedio<10):
            print("Tu Calificacion es: B")
        if(promedio>=8 and promedio<9):
            print("Tu Calificacion es: C")    
        if(promedio>=7 and promedio<8):
            print("Tu Calificacion es: D")
        if(promedio>6 and promedio<7):
            print("Tu Calificacion es: E")
        if(promedio<6):
            print("Tu Calificacion es: F")     
    else:
        print("Promedio Erroneo")
else:
    print("Promedio Erroneo")