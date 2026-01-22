def recibirpin(a, b, c, d):
    # Retornamos directamente la lista de enteros
    return [a, b, c, d]


def generar_codificacion(pin_lista):
    # El ancho total es 10 según tu código
    ancho = 10

    for i in range(len(pin_lista)):
        valor_pin = pin_lista[i]
        # El punto donde empiezan las 'O' es el ancho menos el valor del PIN
        punto_corte = ancho - valor_pin

        fila = ""
        for j in range(ancho):
            if j >= punto_corte:
                fila += "O"
            else:
                fila += "X"
        print(fila)


# Prueba con el PIN del ejemplo 6240
pin = recibirpin(6, 2, 4, 0)
generar_codificacion(pin)











