import random
def preunta(num):
    if num==1:
        return "Es Seguro"
    if num==2:
        return "Si"
    if num==3:
        return "probablemente"
    if num==4:
        return "intenta preguntar otra vez"
    if num==5:
        return "pregunta mas tarde"
    if num==6:
        return "concentrate y pregunta de nuevo"
    if num==7:
        return "mi rspuesta es no"
    if num==8:
        return "no se ve nada bien"
    if num==9:
        return "lo dudo mucho"

print("Soy la gran caracola magica, ingresar tu pregunta")
num=input()
print(preunta(random.randint(1,9)))
print("Oohhhhhhhh, la caracola magica ha hablado, blublublublbulbublub")
print("Tu preginta es: "+num)
print("tu respuesta es: "+preunta(random.randint(1,9)))