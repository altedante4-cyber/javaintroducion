clientes = { "Chuletón, José": 35, "Tosidad, Rubén": 27, "Rupto,Francisco": 44, "Cotón Carmelo": 56 }

ordenador = sorted(clientes.items() , key=lambda k:k[1]  ,reverse=True)
nombre_nuevo=[]
for i in ordenador:
    nombre , pila = i
    
    palabra = ""
    for j in nombre:

        if j != "\n":
            palabra += j.replace(","," ")
        else:
            palabra += ""
    nombre_nuevo.append([palabra,pila])


for i in nombre_nuevo:
    nombre = i[0].split()
    pila = i[1]

    print(f"{nombre[1]} {nombre[0]} ({pila})")
