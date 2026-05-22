# Variables iniciales predefinidas
texto1 = "Examen 1T01"
texto2 = "Octubre-2025"

# Función para separar palabras usando bucles (sin usar .split())
def separar_palabras(cadena, separador):
    palabras = []
    palabra_actual = ""
    for caracter in cadena:
        if caracter == separador:
            palabras.append(palabra_actual)
            palabra_actual = ""
        else:
            palabra_actual += caracter
    palabras.append(palabra_actual) # Añadir la última palabra
    return palabras

# Procesar texto1 (separado por espacio)
palabras1 = separar_palabras(texto1, " ")
p1_1 = palabras1[0]
p1_2 = palabras1[1]

# Procesar texto2 (separado por guión)
palabras2 = separar_palabras(texto2, "-")
p2_1 = palabras2[0]
p2_2 = palabras2[1]

# Calcular longitud total
longitud_total = 0
for caracter in texto1:
    longitud_total += 1
for caracter in texto2:
    longitud_total += 1

# Componer la cadena resultante
# Formato: p1_2-p2_2 p1_1 p2_1 (longitud)
resultado = p1_2 + "-" + p2_2 + " " + p1_1 + " " + p2_1 + " (" + str(longitud_total) + ")"

# Mostrar por consola
print(f"Resultado: {resultado}")
