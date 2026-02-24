def mostrar_ranking(jugadores):
    # enumerate genera tuplas (indice, valor)
    for puesto, nombre in enumerate(jugadores, start=1):
        print(f"{puesto}. {nombre}")

# zip combina listas en tuplas
def combinar_datos(nombres, edades):
    for n, e in zip(nombres, edades):
        print(f"{n} tiene {e} años")