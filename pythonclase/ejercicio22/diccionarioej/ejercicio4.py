clientes = { "Chuletón, José": 35, "Tosidad, Rubén": 27, "Rupto, Francisco": 44, "Cotón, Carmelo": 56 }

lista_ordenada = []

for clave, edad in clientes.items():
    # 1. Corregimos el orden: el apellido va antes de la coma
    apellido, nombre = clave.split(", ")
    
    # 2. Guardamos primero el nombre para que sorted() lo use como prioridad
    lista_ordenada.append([nombre, apellido, edad])

# 3. sorted() ordenará por el primer elemento de cada sublista (el nombre)
lista_final = sorted(lista_ordenada)

for i in lista_final:
    # i[0] es nombre, i[1] es apellido, i[2] es edad
    print(f"{i[0]} {i[1]} ({i[2]})")