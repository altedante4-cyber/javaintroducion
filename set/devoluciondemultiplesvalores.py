def calcular_estadisticas(lista_numeros):
    suma = sum(lista_numeros)
    media = suma / len(lista_numeros)
    # Devolvemos una tupla con dos valores
    return suma, media

# Uso con desempaquetado
total, promedio = calcular_estadisticas([10, 20, 30])