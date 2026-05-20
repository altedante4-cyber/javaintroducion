

respuesta=""
lista_compras=[]
while respuesta != "n":

    articulo = input("INtroduce un articulo ")
    cantidad = input("Introuduce la cantidad")
    precio = input("Introduce el precio ")

    lista_compras.append({
          "articulo":articulo,
          "cantidad":cantidad,
          "precio":precio
    })
    
    respuesta = input("Quieres seguir introudciendo articulos en la lista (si/no )")

print(f"Tu lista de la compra se enecunetra en el fichero compra.txt")
try:
    with open("compra.txt","w",encoding="utf-8") as f:
        precio_compra = 0 
        
        for i in lista_compras:
            a = i["precio"]
            precio_compra += float(a)
            f.write(f"{i["cantidad"]} {i["articulo"]}\n")

        f.write(f"Total articulo en la lista: {len(lista_compras)}\n")
        f.write(f"Precio de la compra: {precio_compra}")
except Exception:
    print("Ocurrio un error con el archivo ")
