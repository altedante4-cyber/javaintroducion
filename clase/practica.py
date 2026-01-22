# 9. Conteo y Posición de un Carácter
# ==============================================================================
print("\n--- 9. Conteo y Posición de un Carácter ---")

cadena = input("Introduce la cadena completa: ")
caracter = input("Introduce el carácter a buscar: ")

if len(caracter) != 1:
    print("Por favor, introduce exactamente un carácter para buscar.")
else:
    posiciones = []
    conteo = 0
    
    # Recorrer la cadena con su índice
    indice = 0
    while indice < len(cadena):
        if cadena[indice] == caracter:
            posiciones.append(indice) # Guardar el índice
            conteo += 1

        indice += 1

    posiciones_str = ""
    i = 0
    while i < len(posiciones):
        if i > 0:
            posiciones_str += ", "
        posiciones_str += str(posiciones[i])
        i += 1
    
    print(f"El carácter '{caracter}' aparece en {conteo} ocasiones.")
    print(f"Las posiciones (índice 0) en las que aparece son: {posiciones_str}")