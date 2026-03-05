def total_compra(productos:dict) :
     # sumar valores en los dicionarios con la funcion sum 

    #  total = sum(productos.values())
    #  print(total) esto si solo tiene 2 claves pero como tiene 3 no nos vales 

    total = 0 

    for i in lista_compras:
    
        total += i['precio']


    return total 
def aplicar_descuento(productos:dict ,porcentaje:int):
    # si eltotoal supera 50 euros aplicar automaticamente un 10% de descuento 

    total = total_compra(productos)

    if total < 50 :
        return total # devolvemso el total tal como esta
    
    return total - (total * 0.50)

def producto_mas_caro(productos:dict):
    #que devuvelv a el nombre dle producto con mayor precio_unitario 
    mayor_precio_unitario = productos[0]['precio']

    for precio in productos:
        producto_actual =precio['precio']

        if producto_actual > mayor_precio_unitario:
            mayor_precio_unitario = producto_actual
    
    return mayor_precio_unitario



lista_compras =[]

cantidad_productos_agregar = 2

for i in range(cantidad_productos_agregar):

    producto = input("Ingrese el nombre del producto ")
    cantidad = int(input("Ingrese la cantidad "))
    precio =  float(input("ingrese el precio "))

    # producto_nuevo = {producto:cantidad,precio}
    # lista_compras.append(producto_nuevo) ==========> esta manera de aqui esta mal por que los valores se guradaban de manera desordenada
    #CREAR EL DICCIONARIO CORRECTAMNETE (CON CLAVES : VALORES)
    producto_nuevo = {
        "producto":producto,
        "cantidad":cantidad,
        "precio" : precio 
    }

    lista_compras.append(producto_nuevo)


#cuidado con este al hacer la prueba meti dos claves iguales pasa que los didcionarios no acepta claves iguales las claves tienen que ser unicas 

print("TICKET DE COMPRA : ")
for productos in lista_compras:

    print(f"{productos['producto']:<15} x{productos['cantidad']:<10}  {productos['precio']:.2f} EUR")
    

print(f"TOTAL: {total_compra(lista_compras):.2f}EUR  (sin descuento)")
print(f"APLICANDO DESCUENTO TE  SALDRIA {aplicar_descuento(lista_compras,10)}  aplicado un descuento de 10%")
