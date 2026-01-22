"""
Docstring for practica6
6. Análisis de datos
Crea una tupla con información de productos: (nombre, precio, cantidad). Tienes 5 productos. Calcula:

El valor total de cada producto (precio × cantidad)

El producto más caro

El valor total del inventario

"""
nombre = ("michael","peredo","axelino")
precio =(23,24,56)
cantidad = (1,2,3,4)


lista_maximo = []


for i , j in zip(precio,cantidad):

    resultado = i * j

    lista_maximo.append(resultado)


print(lista_maximo)

sacar_maximo = max(lista_maximo)

print(sacar_maximo)
