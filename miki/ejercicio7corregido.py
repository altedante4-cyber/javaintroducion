def es_mac_valida(mac):
    # Convertir a mayúsculas para simplificar
    mac = mac.upper()

    # Verificar formato dos puntos
    if ':' in mac:
        partes = mac.split(':')

       #si se deivenden 6 parte es una mac valida
        if len(partes) != 6:
            return False

        for parte in partes:
            if len(parte) != 2:  # aqui verificamos que cada blo contenga solo dos
                return False

            # Verificar que sea hexadecimal válido
            try:  # si se pasa  de 255 o si es menor davuelve false
                valor = int(parte, 16)
                if valor < 0 or valor > 255:
                    return False
            except ValueError:
                return False  # No es hexadecimal válido

        return True # si no retorna true

    # Verificar formato punto (CISCO)
    elif '.' in mac:
        partes = mac.split('.')

        if len(partes) != 3:  # contenga 3 parte en ves de 6 partees
            return False

        for parte in partes:
            if len(parte) != 4:  # Cada bloque debe tener 4 caracteres
                return False

            # Verificar que sea hexadecimal válido
            try: # verificar que no se pasa
                valor = int(parte, 16)
                if valor < 0 or valor > 65535:  # 0xFFFF = 65535
                    return False
            except ValueError:
                return False  # No es hexadecimal válido

        return True

    # Si no tiene ':' ni '.', no es formato válido
    return False


def macsValidas(*args):
    contador_validas = 0
    contador_no_validas = 0

    for mac in args:
        if es_mac_valida(mac):
            print(f"{mac} es válida")
            contador_validas += 1
        else:
            print(f"{mac} no es válida")
            contador_no_validas += 1

    print(f"MACs válidas: {contador_validas}")
    print(f"MACs no válidas: {contador_no_validas}")


# Ejemplos de uso
print("=== Prueba 1 ===")
macsValidas("F4:8E:38:AF:F4:1C", "7521-MXP")

print("\n=== Prueba 2 ===")
macsValidas("F48E.38AF.F41C", "f4:8e:38:af:f4:1c", "AA:BB:CC:DD:EE:FF", "1234.5678.90AB")