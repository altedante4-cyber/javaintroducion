import random

letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digitos = "0123456789"
caracteres = letras + digitos + "!@#$%&?"
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnopqrstuvwxyz"

def generar_clave(longitud=12):
    return "".join(random.choice(caracteres) for _ in range(longitud))

def generar_claves_multiples(cantidad, longitud=12):
    return {f"clave_{i+1}": generar_clave(longitud) for i in range(cantidad)}

def clave_con_requisitos(longitud=12):
    if longitud < 4:
        raise ValueError("longitud minima 4")
    mayus = random.choice(mayusculas)
    minus = random.choice(minusculas)
    digito = random.choice(digitos)
    simbolo = random.choice("!@#$%&?")
    resto = [random.choice(caracteres) for _ in range(longitud - 4)]
    lista = [mayus, minus, digito, simbolo] + resto
    random.shuffle(lista)
    return "".join(lista)

if __name__ == "__main__":
    print("=== GENERACION DE CLAVES ===")
    print(f"Clave simple:      {generar_clave()}")
    print(f"Clave (8 chars):   {generar_clave(8)}")
    print(f"Clave con reqs:    {clave_con_requisitos()}")
    print()
    claves = generar_claves_multiples(5, 10)
    for nombre, clave in claves.items():
        print(f"  {nombre}: {clave}  (longitud: {len(clave)})")
