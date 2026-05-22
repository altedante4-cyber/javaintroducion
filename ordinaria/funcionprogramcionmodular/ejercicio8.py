def es_digito(c):
    return '0' <= c <= '9'

def es_letra_valida(c):
    c = c.upper()
    vocales = ['A', 'E', 'I', 'O', 'U']
    invalidas = ['Ñ', 'Q']
    if not ('A' <= c <= 'Z'):
        return False
    if c in vocales or c in invalidas:
        return False
    return True

def es_matricula_valida(matricula):
    if len(matricula) < 7 or len(matricula) > 8:
        return False
    
    if not all(es_digito(d) for d in matricula[:4]):
        return False
    
    if len(matricula) == 7:
        letras = matricula[4:]
        if len(letras) != 3:
            return False
        return all(es_letra_valida(l) for l in letras)
    else:
        intermedio = matricula[4]
        if intermedio not in [' ', '-']:
            return False
        letras = matricula[5:]
        if len(letras) != 3:
            return False
        return all(es_letra_valida(l) for l in letras)

def matriculasValidas(*matriculas):
    validas = 0
    no_validas = 0
    for m in matriculas:
        if es_matricula_valida(m):
            print(f"{m} es válida")
            validas += 1
        else:
            print(f"{m} no es válida")
            no_validas += 1
    print(f"Matrículas válidas: {validas}")
    print(f"Matrículas no válidas: {no_validas}")

if __name__ == "__main__":
    print("Ejemplo 1:")
    matriculasValidas("22CDR", "7521-MXP", "1224MN")
    print()
    print("Ejemplo 2:")
    matriculasValidas("5432 – BCF", "3456BAC")
