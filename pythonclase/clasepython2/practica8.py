"""
Docstring for practica8
8. Gestor de inventario con tuplas anidadas
Crea una estructura de datos con tuplas anidadas que represente:

Categorías → Productos → (nombre, precio, stock)
Implementa funciones para:

Buscar productos por categoría

Calcular valor total por categoría

Actualizar stock (recordando que las tuplas son inmutables)
"""

# ====== ESTRUCTURA DE INVENTARIO ======
# Categorías → Productos → (nombre, precio, stock)

inventario = (
    # Categoría: Electrónica
    ("Electrónica", (
        ("Laptop", 1200.00, 5),
        ("Smartphone", 800.00, 10),
        ("Tablet", 300.00, 0),  # Stock agotado
        ("Audífonos", 150.00, 15)
    )),
    
    # Categoría: Ropa
    ("Ropa", (
        ("Camiseta", 25.00, 50),
        ("Jeans", 60.00, 20),
        ("Chaqueta", 90.00, 8),
        ("Zapatos", 120.00, 12)
    )),
    
    # Categoría: Hogar
    ("Hogar", (
        ("Sartén", 40.00, 30),
        ("Toallas", 15.00, 100),
        ("Lámpara", 75.00, 5)
    ))
)


#buscar producto por categoria

categoria = input("ingrese la categoria que de se buscar \n 1.Electronica \n 3.Hogar \n 2.Ropa \n opcion =  ")

match categoria:

    case '1':

        convertir_mayuscula = int(categoria) - 1 

        for producto , valor in enumerate(inventario[convertir_mayuscula]):
            
            cadena_bonita = ""
            for i in valor:
                cadena_bonita += i[0] + " "
        
        print(cadena_bonita)

               
    case '2':

        

        convertir_mayuscula = int(categoria) - 1 

        for producto , valor in enumerate(inventario[convertir_mayuscula]):
            cadena_bonita = ""
            for i in valor:
                cadena_bonita += i[0] + " "
        
        print(cadena_bonita)


    case '3':

        convertir_mayuscula = int(categoria) - 1 

        for producto , valor in enumerate(inventario[convertir_mayuscula]):
            cadena_bonita = ""
            for i in valor:
                cadena_bonita += i[0] + " "
        
        print(cadena_bonita)


    case _:

        print("Numero invalido intente ingresar un numero que sea valido por favor")

        
valor = int(input("ingrese la categoria que quiera calcula su valor \n 1.Electronica  \n 2.Ropa \n 3.Hogar"))

match valor:

    case 1 :

        opcion = valor - 1


        categoria_nombre,producto = inventario[opcion]

        print(f"\n valor total de la ategoria {categoria_nombre} \n")

        for nombre,precio,cantidad in producto:
            total = precio * cantidad
            print(f"{nombre} : {total}")
    case 2 :

        opcion = valor - 1


        categoria_nombre,producto = inventario[opcion]

        print(f"\n valor total de la ategoria {categoria_nombre} \n")

        for nombre,precio,cantidad in producto:
            total = precio * cantidad
            print(f"{nombre} : {total}")
    case 3 :

        opcion = valor - 1


        categoria_nombre,producto = inventario[opcion]

        print(f"\n valor total de la ategoria {categoria_nombre} \n")

        for nombre,precio,cantidad in producto:
            total = precio * cantidad
            print(f"{nombre} : {total}")
 
    case _:

        print("erro pelotudo ")
        

                
            