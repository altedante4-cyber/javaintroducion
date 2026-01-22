# ---------------------------------------------------------------------
# Ejercicio 2: Contador de Vocales y Frecuencia
# Meta: Contar la frecuencia de cada vocal y encontrar la más común.
# ---------------------------------------------------------------------

def contar_vocales(frase_original):
    """
    Analiza una frase para contar la frecuencia de las vocales (a, e, i, o, u)
    y determina cuál es la más frecuente.
    """
    
    # 1. Inicialización y Limpieza de la Frase
    # Usamos un diccionario donde la clave es la vocal y el valor es el contador.
    conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Convertir la frase a minúsculas para contar A/a, E/e, etc., como la misma vocal.
    frase_limpia = frase_original.lower()
    
    # 2. Conteo en una Sola Pasada
    
    # Recorremos cada carácter de la frase limpia
    for char in frase_limpia:
        # Verificamos si el carácter es una de las claves de nuestro diccionario
        if char in conteo_vocales:
            # Si lo es, incrementamos su contador
            conteo_vocales[char] += 1
            
    # 3. Determinación del Máximo Conteo
    
    # Obtenemos el valor más alto de todos los recuentos (ej. 2)
    max_conteo = max(conteo_vocales.values())
    
    # Identificamos las vocales que tienen ese conteo máximo (para manejar empates)
    vocales_mas_frecuentes = []
    
    # Iteramos sobre el diccionario (clave=vocal, valor=cuenta)
    for vocal, cuenta in conteo_vocales.items():
        if cuenta == max_conteo and cuenta > 0: # Excluimos el caso donde el máximo es 0
            vocales_mas_frecuentes.append(vocal)
            
    # 4. Formato de Salida
    
    # a) Construir la lista de recuentos (ej. "a: 2, e: 2, i: 1, ...")
    recuentos_str = ', '.join([f"{vocal}: {conteo_vocales[vocal]}" for vocal in conteo_vocales])
    
    # b) Construir el mensaje de las vocales más frecuentes
    if len(vocales_mas_frecuentes) == 1:
        frecuente_msg = f"La vocal más frecuente es '{vocales_mas_frecuentes[0]}'."
    elif len(vocales_mas_frecuentes) > 1:
        # Unir las vocales con " y " para un mensaje legible (ej. "a, e y o")
        vocales_unidas = ', '.join(vocales_mas_frecuentes[:-1])
        frecuente_msg = f"Las vocales más frecuentes son {vocales_unidas} y '{vocales_mas_frecuentes[-1]}' (ambas con {max_conteo} apariciones)."
    else:
        frecuente_msg = "No se encontraron vocales en la frase."
        
    print(f"--- Recuentos ---\n{recuentos_str}")
    print(frecuente_msg)


# --- Ejecución del Programa ---
frase_de_prueba = "El cielo está azul"
print(f"Analizando frase: '{frase_de_prueba}'\n")
contar_vocales(frase_de_prueba)

print("\n" + "="*20 + "\n")

frase_de_prueba_2 = "El murciélago come queso"
print(f"Analizando frase: '{frase_de_prueba_2}'\n")
contar_vocales(frase_de_prueba_2) # Prueba de vocales con acentos y mayúsculas