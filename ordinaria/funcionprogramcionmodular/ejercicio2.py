def digito_a_linea(digito):
    return 'X' * (10 - digito) + 'O' * digito

def codificar_pin_v2(pin):
    pin_str = str(pin).zfill(4)
    resultado = []
    for c in pin_str:
        digito = int(c)
        resultado.append(digito_a_linea(digito))
    return resultado

if __name__ == "__main__":
    lineas = codificar_pin_v2(6240)
    for linea in lineas:
        print(linea)
