def encontrar_primer_duplicado(datos):
    vistos = set()
    for elemento in datos:
        if elemento in vistos:
            return elemento  # Encontrado
        vistos.add(elemento)
    return None