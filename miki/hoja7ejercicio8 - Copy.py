import random


def tablero(filas, columnas, minas):
    # Validar que no haya más minas que celdas
    if minas > filas * columnas:
        print("Error: Demasiadas minas para el tamaño del tablero")
        return None

    minas_colocadas = 0
    tablero_matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

    # Utilizamos while para colocar minas
    while minas_colocadas < minas:
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)

        # Solo colocar mina si la celda es 0
        if tablero_matriz[fila][columna] == 0:
            tablero_matriz[fila][columna] = 1
            minas_colocadas += 1

    return tablero_matriz


# Ejemplo de uso
tableros = tablero(3, 3, 10)  # Esto dará error (10 > 3*3)

if tableros:  # Solo mostrar si no es None
    for fila in tableros:
        print("".join(map(str, fila)))