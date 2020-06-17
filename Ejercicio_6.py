numeros=[]
def numero():
    try:
        num=int(input("Ingresa numeros: "))
        numeros.append(num)
    except ValueError:
        print("Valor Invalido")

for i in range(10):
    numero()
print(numeros)
for i in(numeros):
    print(i)