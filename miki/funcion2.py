def generar_linea(digito):
    """Crea una sola línea basada en un dígito."""
    linea = ""
    # El 0 se convierte en 9 (última posición), los demás en n-1
    posicion_o = 9 if digito == 0 else digito - 1

    for i in range(10):
        if i == posicion_o:
            linea += "O"
        else:
            linea += "x"
    return linea


def codificarpin(a, b, c, d):
    # Metemos los argumentos en una lista para iterar sobre ellos
    pin = [a, b, c, d]
    estructura = []

    for digito in pin:
        # Llamamos a nuestra 'fábrica' de líneas
        nueva_linea = generar_linea(digito)
        estructura.append(nueva_linea)

    return estructura


# Ejecución
resultado = codificarpin(6, 4, 2, 0)
for linea in resultado:
    print(linea)