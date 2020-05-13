lechePrecio=20
huevoPrecio=18.5
sabritasPrecio=12.5
cocaPrecio=25
cantCompraLeche=0
cantCompraHuevo=0
cantCompraSabritas=0
cantCompraCoca=0
clientes=0
totalDeProductos=0
gananciaTotal=0
res=input("Cerrar la Tienda: ")
while(res!="si"):
    res=input("Decea seleccionar un producto: ")
    while(res!="no"):
        lecheCantidad=100
        huevoCantidad=100
        sabritasCatidad=100
        cocaCantidad=100
        print("Leche Ingresa-->1")
        print("Huevos Ingresa-->2")
        print("Sabritas Ingresa-->3")
        print("Coca Ingresa-->4")
        num=int(input("Ingresa la Obcion: "))
        if(num==1 or num==2 or num==3 or num==4):

            if(num==1):
                cantidad=int(input("Ingresa la Cantidad: "))
                lecheCantidad-=cantidad
                cantCompraLeche+=cantidad
            if(num==2):
                cantidad=int(input("Ingresa la Cantidad: "))
                huevoCantidad-=cantidad
                cantCompraHuevo+=cantidad
            if(num==3):
                cantidad=int(input("Ingresa la Cantidad: "))
                sabritasCatidad-=cantidad
                cantCompraSabritas+=cantidad
            if(num==4):
                cantidad=int(input("Ingresa la Cantidad: "))
                cocaCantidad-=cantidad
                cantCompraCoca+=cantidad
            totalDeProductos=cantCompraCoca+cantCompraHuevo+cantCompraLeche+cantCompraSabritas
            gananciaTotal=(cantCompraCoca*cocaPrecio)+(cantCompraHuevo*huevoPrecio)+(cantCompraLeche*lechePrecio)+(cantCompraSabritas*sabritasPrecio)
            print("Cantidad de producto que Quedan: "+'\n'"Leche: "+str(lecheCantidad)+'\n'"Huevo: "+str(huevoCantidad)+'\n' "Sabritas: "+str(sabritasCatidad)+'\n' "Coca: "+str(cocaCantidad))    
            res=input("Despues de seleccionar un producto: ")
            if(res=="no"):
                print("La cantidad de cada producto que compro: "+'\n'"Leche: "+str(cantCompraLeche)+'\n'"Huevo: "+str(cantCompraHuevo)+'\n' "Sabritas: "+str(cantCompraSabritas)+'\n' "Coca: "+str(cantCompraCoca))
                print("El total por cada producto comprado: "'\n'"Leche: "+str(cantCompraLeche*lechePrecio)+'\n'"Huevo: "+str(cantCompraHuevo*huevoPrecio)+'\n' "Sabritas: "+str(cantCompraSabritas*sabritasPrecio)+'\n' "Coca: "+str(cantCompraCoca*cocaPrecio))
                print("Numero total de todos los productos vendidos: ",totalDeProductos)
                print("Ganacias totales del dia:", gananciaTotal)
        else:
             print("Producto erroneo")
             res=input("Despues de seleccionar un producto: ")
    totalDeProductos=cantCompraCoca+cantCompraHuevo+cantCompraLeche+cantCompraSabritas
    gananciaTotal=(cantCompraCoca*cocaPrecio)+(cantCompraHuevo*huevoPrecio)+(cantCompraLeche*lechePrecio)+(cantCompraSabritas*sabritasPrecio)
    clientes+=1
    print("Cantidad de producto que Quedan: "+'\n'"Leche: "+str(lecheCantidad)+'\n'"Huevo: "+str(huevoCantidad)+'\n' "Sabritas: "+str(sabritasCatidad)+'\n' "Coca: "+str(cocaCantidad))
    if(lecheCantidad<=50):
        print("<Leche> a la mitad de su existencia")
    elif(lecheCantidad<=25):
        print("<Leche> Producto agotandose")
    elif(lecheCantidad<=10):
        print("<Leche> Pruducto escaso")
    elif(lecheCantidad==0):
        print("<Leche> Producto agotado")
    if(huevoCantidad<=50):
        print("<Huevo> a la mitad de su existencia")
    elif(huevoCantidad<=25):
        print("<Huevo> Producto agotandose")
    elif(huevoCantidad<=10):
        print("<Huevo> Pruducto escaso")
    elif(huevoCantidad==0):
        print("<Huevo> Producto agotado")
    if(sabritasCatidad<=50):
        print("<Sabritas> a la mitad de su existencia")
    elif(sabritasCatidad<=25):
        print("<Sabritas> Producto agotandose")
    elif(sabritasCatidad<=10):
        print("<Sabritas> Pruducto escaso")
    elif(sabritasCatidad==0):
        print("<Sabritas> Producto agotado")
    if(cocaCantidad<=50):
        print("<Coca> a la mitad de su existencia")
    elif(cocaCantidad<=25):
        print("<Coca> Producto agotandose")
    elif(cocaCantidad<=10):
        print("<Coca> Pruducto escaso")
    elif(cocaCantidad==0):
        print("<Coca> Producto agotado")
    if(lecheCantidad==0 and huevoCantidad==0 and sabritasCatidad==0 and cocaCantidad==0):
        print("Todos los productos se han agotado")
        break    
    res=input("Cerrar la Tienda: ")
print("Numero de clientes totales del dia: ",clientes)
print("Numero total de cada producto vendiendo: "+'\n'"Leche: "+str(cantCompraLeche)+'\n'"Huevo: "+str(cantCompraHuevo)+'\n' "Sabritas: "+str(cantCompraSabritas)+'\n' "Coca: "+str(cantCompraCoca))
print("Numero total de todos los productos vendidos: ",totalDeProductos)
print("Total de ganancias por cada producto"+'\n'"Leche: "+str(cantCompraLeche*lechePrecio)+'\n'"Huevo: "+str(cantCompraHuevo*huevoPrecio)+'\n' "Sabritas: "+str(cantCompraSabritas*sabritasPrecio)+'\n' "Coca: "+str(cantCompraCoca*cocaPrecio))
print("Ganacias totales del dia:", gananciaTotal)
print("Cantidad de cada producto que queda en existencia"+'\n'"Leche: "+str(lecheCantidad)+'\n'"Huevo: "+str(huevoCantidad)+'\n' "Sabritas: "+str(sabritasCatidad)+'\n' "Coca: "+str(cocaCantidad))
