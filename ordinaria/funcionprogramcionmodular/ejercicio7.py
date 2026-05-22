def es_hexadecimal(c):
    return '0' <= c <= '9' or 'a' <= c.lower() <= 'f' or 'A' <= c.upper() <= 'F'

def es_mac_valida(mac):
    if len(mac) == 17:
        posiciones_dos_puntos = [2, 5, 8, 11, 14]
        for i in posiciones_dos_puntos:
            if mac[i] != ':':
                return False
        for i in range(17):
            if i in posiciones_dos_puntos:
                continue
            if not es_hexadecimal(mac[i]):
                return False
        return True
    elif len(mac) == 14:
        posiciones_puntos = [4, 9]
        for i in posiciones_puntos:
            if mac[i] != '.':
                return False
        for i in range(14):
            if i in posiciones_puntos:
                continue
            if not es_hexadecimal(mac[i]):
                return False
        return True
    return False

def macsValidas(*macs):
    validas = 0
    no_validas = 0
    for mac in macs:
        if es_mac_valida(mac):
            print(f"{mac} es válida")
            validas += 1
        else:
            print(f"{mac} no es válida")
            no_validas += 1
    print(f"MACs válidas: {validas}")
    print(f"MACs no válidas: {no_validas}")

if __name__ == "__main__":
    print("Ejemplo 1:")
    macsValidas("F4:8E:38:AF:F4:1C", "7521-MXP")
    print()
    print("Ejemplo 2:")
    macsValidas("F48E38AFF41C", "f48e.38af.f41c", "F:3:AF:4:1:11")
