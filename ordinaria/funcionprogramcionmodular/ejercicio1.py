def digito_a_linea(digito):
    posicion = (digito - 1) % 10
    linea = ['X'] * 10
    linea[posicion] = 'O'
    return ''.join(linea)

def codificar_pin(pin):
    pin_str = str(pin).zfill(4)
    resultado = []
    for c in pin_str:
        digito = int(c)
        resultado.append(digito_a_linea(digito))
    return resultado

if __name__ == "__main__":
    lineas = codificar_pin(6240)
    for linea in lineas:
        print(linea)
