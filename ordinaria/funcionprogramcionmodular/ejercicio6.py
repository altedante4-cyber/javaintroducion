def es_ip_valida(ip):
    partes = ip.split('.')
    if len(partes) != 4:
        return False, None
    try:
        octetos = []
        for p in partes:
            octeto = int(p)
            if octeto < 0 or octeto > 255:
                return False, None
            octetos.append(octeto)
        return True, octetos
    except ValueError:
        return False, None

def clasificar_ip(ip):
    valida, octetos = es_ip_valida(ip)
    if not valida:
        return "Dirección no válida"
    
    primer_byte = octetos[0]
    
    if primer_byte >= 224 and primer_byte <= 255:
        return "Dirección reservada"
    elif primer_byte >= 0 and primer_byte <= 127:
        return f"{ip}/8"
    elif primer_byte >= 128 and primer_byte <= 191:
        return f"{ip}/16"
    elif primer_byte >= 192 and primer_byte <= 223:
        return f"{ip}/24"
    else:
        return "Dirección no válida"

if __name__ == "__main__":
    ip = input("Introduce una dirección IP: ")
    print(clasificar_ip(ip))
