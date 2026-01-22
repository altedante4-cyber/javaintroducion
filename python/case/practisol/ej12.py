"""
Generar una matriz 7x5 de coordenadas únicas con formato:
(X,Y,Z)-(X,Y,Z)-(X,Y,Z)-(X,Y,Z)-(X,Y,Z)
Donde X, Y, Z son números enteros entre 0-9 y cada tripleta
(X,Y,Z) debe ser única en toda la matriz.

Restricción: Usar 3 niveles de bucles anidados.
Ejemplo de salida:
(0,1,2)-(3,4,5)-(6,7,8)-(9,0,1)-(2,3,4)
(5,6,7)-(8,9,0)-(1,2,3)-(4,5,6)-(7,8,9)
...
"""
import random 

import random

# Conjunto global para almacenar todas las tripletas usadas y garantizar la unicidad.
# Es crucial que se defina fuera de los bucles de fila y tripleta.
tripletas_usadas = set() 

# Lista final para almacenar las 7 filas de la matriz.
matriz_resultado = []

# Restricción: Usar 3 niveles de bucles anidados.
FILAS = 7
TRIPLETAS_POR_FILA = 5

# --- Bucle Nivel 1: Iterar por las Filas (7 veces) ---
for fila_index in range(FILAS):
    
    # Cadena que representará la fila completa (e.g., "(0,1,2)-(3,4,5)...")
    linea_actual = [] 

    # --- Bucle Nivel 2: Iterar por las Tripletas dentro de la Fila (5 veces) ---
    for tripleta_index in range(TRIPLETAS_POR_FILA):
        
        tripleta_unica_encontrada = False
        
        # Bucle de verificación: Sigue generando y verificando hasta encontrar una tripleta única.
        while not tripleta_unica_encontrada:
            
            # Lista temporal para construir la tripleta (X, Y, Z)
            tripleta_generada = []

            # --- Bucle Nivel 3: Iterar por las Coordenadas (3 veces: X, Y, Z) ---
            for _ in range(3):
                # Generación del número entero aleatorio entre 0 y 9.
                coordenada = random.randint(0, 9) 
                tripleta_generada.append(coordenada)
            
            # Convertir la lista [X, Y, Z] a una tupla (X, Y, Z) para que pueda ser 
            # agregada y verificada eficientemente en el conjunto `tripletas_usadas`.
            tripleta_tupla = tuple(tripleta_generada)
            
            # Verificar la unicidad:
            if tripleta_tupla not in tripletas_usadas:
                # Si es única:
                tripletas_usadas.add(tripleta_tupla)
                tripleta_unica_encontrada = True
            # Si NO es única, el bucle 'while' se repite y se genera una nueva tripleta.
        
        # Formateo de la tripleta única como cadena "(X,Y,Z)"
        # La tupla ya es (X, Y, Z)
        cadena_tripleta = f"({tripleta_tupla[0]},{tripleta_tupla[1]},{tripleta_tupla[2]})"
        
        # Agregar la tripleta formateada a la línea actual
        linea_actual.append(cadena_tripleta)

    # Unir las 5 tripletas de la fila con el guion (-)
    fila_final_formato = "-".join(linea_actual)
    
    # Agregar la fila completa al resultado final de la matriz
    matriz_resultado.append(fila_final_formato)

# Impresión del resultado final
for codigo in matriz_resultado:
    print(codigo)

