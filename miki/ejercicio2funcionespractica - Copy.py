def validar_pin(pin):
    """
    Comprueba que el PIN tenga 4 caracteres y que todos sean dígitos.
    """
    return len(pin) == 4 and pin.isdigit()


def codificar_digito(digito):
    """
    Codifica un solo dígito según el nuevo sistema.
    """
    d = int(digito)
    return "X" * (10 - d) + "O" * d


def codificar_pin(pin):
    """
    Codifica el PIN completo devolviendo una lista de líneas codificadas.
    """
    if not validar_pin(pin):
        raise ValueError("El PIN debe tener exactamente 4 dígitos.")

    resultado = []
    for digito in pin:
        resultado.append(codificar_digito(digito))

    return resultado


def mostrar_codificacion(pin):
    """
    Muestra por pantalla la codificación del PIN.
    """
    lineas = codificar_pin(pin)
    for linea in lineas:
        print(linea)


pin = "6240"
mostrar_codificacion(pin)


