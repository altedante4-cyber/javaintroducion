"""Ejercicios genéricos de programación 7
- switch (match en python) y arrays de una y dos dimensiones
"""

import random


# ──────────────────────────────────────────────
# Ejercicio 1 y 2: Calculadora con switch
# ──────────────────────────────────────────────
def calculadora():
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    op = input("Operación (S/R/M/D, √, ², ³): ").strip().upper()

    match op:
        case "S": r = a + b
        case "R": r = a - b
        case "M": r = a * b
        case "D": r = a / b if b != 0 else "ERROR: división entre 0"
        case "√": r = a ** 0.5
        case "²": r = a ** 2
        case "³": r = a ** 3
        case _:   r = "Operación no válida"

    print("Resultado:", r)


# ──────────────────────────────────────────────
# Ejercicio 3: Número de mes a nombre
# ──────────────────────────────────────────────
def mes():
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    n = int(input("Número del 1 al 12: "))
    if 1 <= n <= 12:
        print(meses[n - 1])
    else:
        print("ERROR: no hay mes con ese número")


# ──────────────────────────────────────────────
# Ejercicio 4: Nota a calificación
# ──────────────────────────────────────────────
def calificacion():
    n = int(input("Nota (1-10): "))

    match n:
        case 1 | 2:          print("Muy deficiente")
        case 3 | 4:          print("Insuficiente")
        case 5:              print("Suficiente")
        case 6:              print("Bien")
        case 7 | 8:          print("Notable")
        case 9 | 10:         print("Sobresaliente")
        case _:              print("ERROR: nota no válida")


# ──────────────────────────────────────────────
# Ejercicio 5: Array aleatorio → máx, mín, media
# ──────────────────────────────────────────────
def estadisticas_array():
    n = int(input("Tamaño del array: "))
    arr = [random.randint(10, 1000) for _ in range(n)]

    print("Array:", arr)
    print("Máximo:", max(arr))
    print("Mínimo:", min(arr))
    print("Media:", round(sum(arr) / n, 2))


# ──────────────────────────────────────────────
# Ejercicio 6: Posiciones del máximo y mínimo
# ──────────────────────────────────────────────
def posiciones_extremos():
    n = int(input("Tamaño del array: "))
    arr = [random.randint(10, 1000) for _ in range(n)]

    max_val = max(arr)
    min_val = min(arr)

    pos_max = [i for i, v in enumerate(arr) if v == max_val]
    pos_min = [i for i, v in enumerate(arr) if v == min_val]

    print("Array:", arr)
    print(f"Máximo {max_val} en posiciones:", pos_max)
    print(f"Mínimo {min_val} en posiciones:", pos_min)


# ──────────────────────────────────────────────
# Ejercicio 7: Recuperar valor por posición
# ──────────────────────────────────────────────
def valor_por_posicion():
    n = int(input("Tamaño del array: "))
    arr = [random.randint(10, 1000) for _ in range(n)]

    print("Array:", arr)

    idx = int(input("Posición a recuperar: "))
    if 0 <= idx < len(arr):
        print(f"arr[{idx}] =", arr[idx])
    else:
        print("ERROR: posición fuera del array")


# ──────────────────────────────────────────────
# Ejercicio 8: Buscaminas — generación del tablero
# ──────────────────────────────────────────────
def buscaminas():
    tam = int(input("Tamaño del tablero (N x N): "))
    minas = int(input("Número de minas: "))

    if minas > tam * tam:
        print("ERROR: más minas que casillas")
        return

    # tablero lleno de 0
    tabla = [[0] * tam for _ in range(tam)]

    # colocar minas aleatorias sin repetir posición
    puestas = 0
    while puestas < minas:
        f = random.randrange(tam)
        c = random.randrange(tam)
        if tabla[f][c] == 0:
            tabla[f][c] = 1
            puestas += 1

    # dibujar
    for fila in tabla:
        print(" ".join(str(c) for c in fila))


# ──────────────────────────────────────────────
# Menú principal
# ──────────────────────────────────────────────
def menu():
    ops = {
        "1": ("Calculadora", calculadora),
        "2": ("Mes del año", mes),
        "3": ("Calificación", calificacion),
        "4": ("Estadísticas array", estadisticas_array),
        "5": ("Posiciones extremos", posiciones_extremos),
        "6": ("Valor por posición", valor_por_posicion),
        "7": ("Buscaminas", buscaminas),
    }

    while True:
        print("\n" + "=" * 40)
        print("EJERCICIOS - BOLETÍN 7")
        print("=" * 40)
        for k, (nom, _) in ops.items():
            print(f"  {k}. {nom}")
        print("  0. Salir")

        sel = input("\nElige: ").strip()
        if sel == "0":
            break
        if sel in ops:
            print()
            ops[sel][1]()
        else:
            print("Opción no válida")


if __name__ == "__main__":
    menu()
