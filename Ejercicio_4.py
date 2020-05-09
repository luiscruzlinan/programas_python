Hmayor=0
Hmenor=0
Mmayor=0
Mmenor=0
suma=0
res=input("Regitrar Persona?: ")
while(res!="no"):
    sexo=input("Ingresa tu Sexo: ")
    if(sexo=="H" or sexo=="F"):
        edad=int(input("Ingresa tu Edad: "))
        if(sexo=="H"):
            if(edad>=18):
                Hmayor+=1
                if(Hmayor==5):
                    print("Se han Censado 5 Hombres Mayores de Edad")
            else:
                Hmenor+=1
        else:
            if(edad>=18):
                Mmayor+=1
                if(Mmayor==5):
                    print("Se han Censado 5 Mujeres Mayores de Edad")
            else:
                Mmenor+=1
        if(Hmenor==5):
            print("Se han Censado 5 Hombres Menores de Edad")
        if(Mmenor==5):
            print("Se han Censado 5 Mujeres Menores de Edad")
        suma+=1
    else:
        print("Sexo Erroneo")
        break
    res=input("Registro Persona?: ")
print("Numero de Personas Censadas: ",suma)
print("Hombres Mayores de edad: ",Hmayor)
print("Hombres Menores de edad: ",Hmenor)
print("Mujeres Mayores de edad: ",Mmayor)
print("Mujeres Menores de edad: ",Mmenor)