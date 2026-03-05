import random

# 1. Generar el diccionario de 456 jugadores
# Usamos un ID como clave y un puntaje aleatorio como valor
jugadores = {f"Jug_{i+1:03}": random.randint(10, 99) for i in range(456)}

# 2. Configuración de la visualización
columnas = 12
lista_claves = list(jugadores.keys())
total_jugadores = len(lista_claves)

# 3. Patrón de iteración para mostrar en columnas
# El bucle externo salta de 12 en 12
for i in range(0, total_jugadores, columnas):
    # El bucle interno recorre los elementos de la "fila" actual
    for j in range(i, i + columnas):
        if j < total_jugadores:
            id_jugador = lista_claves[j]
            puntaje = jugadores[id_jugador]
            # Formateamos para que cada columna ocupe el mismo espacio
            print(f"{id_jugador}:{puntaje}", end="  ")
    
    # Salto de línea al terminar cada fila de 12
    print()