import random
cantidad="Cantidad: "
precio="Precio: "
leche=[cantidad,100,precio,20]
huevo=[cantidad,100,precio,18.5]
sabritas=[cantidad,100,precio,12.5]
coca=[cantidad,100,precio,25]
opciones_de_cliente=["1 - no","2 - si","3 - Claro","4 - Por supuesto","5 - Mejor hagame el amor","6 - Ponme en 4 y dame duro por el cucurucho papi"]
clientes = 0
venta_total=0
total_cliente = 0
total_productos = 0

venta_por_cliente = 0
ven_total_sabritas = 0
ven_total_huevo=0
ven_total_leche=0
ven_total_coca=0

total_leche = 0
total_huevo = 0
total_sabritas = 0
total_coca = 0

can_sabritas=0
can_leche=0
can_huevo=0
can_coca = 0

producto = 0
cantidad = 0

huevo_por_cliente = 0
leche_por_cliente = 0 
coca_por_cliente = 0
sabritas_por_cliente = 0

res=input("Cerrar la Tienda: ")
while(res!="si"):
    print(opciones_de_cliente)
    res=random.randint(1,6)
    while(res!=1):
        if(coca == 0 and huevo == 0 and leche == 0 and sabritas == 0):
             print("La tienda ha cerrado, productos agotados")
             break
        else:
            print("Leche Ingresa-->1")
            print("Huevos Ingresa-->2")
            print("Sabritas Ingresa-->3")
            print("Coca Ingresa-->4")
            num=random.randint(1,4)
            if(num==1 or num==2 or num==3 or num==4):

                if(num==1):
                    cantidad=random.randint(0,100)
                    if(cantidad>leche[1]):
                        print("No se tiene esa cantidad de Leche")
                    else:
                        total_leche= leche[3]*cantidad
                        leche[1]=leche[1]-cantidad
                        can_leche=can_leche+cantidad
                        ven_total_leche=ven_total_leche+total_leche
                        leche_por_cliente=leche_por_cliente+cantidad

                if(num==2):
                    cantidad=random.randint(0,100)
                    if(cantidad>huevo[1]):
                        print("No se tiene esa cantidad de Huevo")
                    else:
                        total_huevo=huevo[3]*cantidad
                        huevo[1]=huevo[1]-cantidad
                        can_huevo=can_huevo+cantidad
                        ven_total_huevo=ven_total_huevo+total_huevo
                        huevo_por_cliente=huevo_por_cliente+cantidad
                if(num==3):
                    cantidad=random.randint(0,100)
                    if(cantidad>sabritas[1]):
                        print("No se tiene esa cantidad de Sabritas")
                    else:
                        total_sabritas=sabritas[3]*cantidad
                        sabritas[1]=sabritas[1]-cantidad
                        can_sabritas=can_sabritas+cantidad
                        ven_total_sabritas=ven_total_sabritas+total_sabritas
                        sabritas_por_cliente=sabritas_por_cliente+cantidad
                if(num==4):
                    cantidad=random.randint(0,100)
                    if(cantidad>coca[1]):
                        print("No se tiene esa cantidad de Cocas")
                    else:
                        total_coca=coca[3]*cantidad
                        coca[1]=coca[1]-cantidad
                        can_coca=can_coca+cantidad
                        ven_total_coca=ven_total_coca+total_coca
                        coca_por_cliente=coca_por_cliente+cantidad
            else:
             print("Producto erroneo")
        print(opciones_de_cliente)
        res=random.randint(1,6)
    total_cliente = total_coca + total_huevo + total_leche + total_sabritas
    venta_total = venta_total + total_cliente
    total_productos = can_coca + can_huevo + can_leche + can_sabritas
    print("-----------------------El cliente ha terminado la compra--------------------")
    print("Coca vendida: ", coca_por_cliente)
    coca_por_cliente = 0
    print("Huevo vendido: ", huevo_por_cliente)
    huevo_por_cliente = 0
    print("Leche vendida: ", leche_por_cliente)
    leche_por_cliente = 0
    print("Sabritas vendidas: ", sabritas_por_cliente)
    sabritas_por_cliente = 0
    print("Total a pagar: ", total_cliente)
    clientes = clientes + 1
    print("---------------------------Producto Restante-------------------")
    print("Huevo: ", huevo[1])
    if(huevo[1]==50):
        print("Huevo a la mitad de su existencia")
    elif(huevo[1]==25):
        print("Huevo Agotandose")
    elif(huevo[1]<=10):
        print("Huevo Escaso")
    print("Leche: ", leche[1])
    if(leche[1]==50):
        print("Leche a la mitad de su existencia")
    elif(leche[1]==25):
        print("Leche Agotandose")
    elif(leche[1]<=10):
        print("Leche Escasa")
    print("Coca: ", coca[1])
    if(coca[1]==50):
        print("Coca a la mitad de su existencia")
    elif(coca[1]==25):
        print("Coca Agotandose")
    elif(coca[1]<=10):
        print("Coca Escasa")
    print("Sabritas: ", sabritas[1])
    if(sabritas[1]==50):
        print("Sabritas a la mitad de su existencia")
    elif(sabritas[1]==25):
        print("Sabritas Agotandose")
    elif(sabritas[1]<=10):
        print("Sabritas Escasas")
    res=input("Cerrar la Tienda: ")
print("##################### LA TIENDA HA CERRADO ######################\n\n")
print("#################### Productos vendidos ##################")
print("Total de huevo vendido: ", can_huevo)
print("Venta total de huevo: ", ven_total_huevo)
print("Total de leche vendida: ", can_leche)
print("Venta total de leche: ", ven_total_leche)
print("Total de Sabritas vendidas: ", can_sabritas)
print("Venta total de Sabritas: ", ven_total_sabritas)
print("Total de coca vendida: ", can_coca)
print("Venta total de coca", ven_total_coca)
print("################# Productos restantes ###########################")
print("Leche: ", leche[1])
print("Huevo: ", huevo[1])
print("Coca: ", coca[1])
print("Sabritas: ", sabritas[1])
print("######################### Venta total ##############################")
print("Productos totales vendidos: ", total_productos)
print("Venta total del día: ", venta_total)
print("Total de clientes del día: ", clientes)
