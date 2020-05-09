nombre=input("Ingresar Nombre: ")
carrera=input("Ingresar Carrera: ")
suma=0
tempomeno=0
tempomay=0
for i in range(9):
    materias=int(input("Ingresar Calificacion: "))
    suma=+materias
    if(materias>=7):
        tempomay+=1
    else:
        tempomeno+=1
promedio=suma/9
print("Nombre del Alumno: "+nombre)
print("Carrera: "+carrera)
print(promedio)
print(tempomay," Son mayores que 7")
print(tempomeno," Son menores que 7")
if(promedio>=7):
    print("APROBADO")
else:
    print("REPROBADO")
