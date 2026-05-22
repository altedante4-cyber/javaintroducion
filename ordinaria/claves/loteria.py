import random

NUMEROS_POR_BOLETO = 6
RANGO = range(1, 46)

def generar_boleto_sets():
    return set(random.sample(list(RANGO), NUMEROS_POR_BOLETO))

def generar_boleto_lista():
    boleto = random.sample(list(RANGO), NUMEROS_POR_BOLETO)
    boleto.sort()
    return boleto

def generar_sorteo():
    return frozenset(random.sample(list(RANGO), NUMEROS_POR_BOLETO)) # un forzenset es un set inmutable no se
# puede modificar despues de creado no tien add ,remove  se usa cuando necesites un conjunto que pueda usar como clave de 
# dicionario  odentro de otro set


def jugar():
    boleto_user = generar_boleto_sets()
    sorteo = generar_sorteo()
    aciertos = boleto_user & sorteo
    return boleto_user, sorteo, aciertos

def simulacion_masiva(cantidad):
    resultados = {}
    for _ in range(cantidad):
        boleto_user, sorteo, aciertos = jugar()
        n = len(aciertos)
        resultados[n] = resultados.get(n, 0) + 1
    return resultados

if __name__ == "__main__":
    print("=== LOTERIA (6/45) ===")
    boleto, sorteo, aciertos = jugar()
    print(f"  Tu boleto: {sorted(boleto)}")
    print(f"  Sorteo:    {sorted(sorteo)}")
    print(f"  Aciertos:  {sorted(aciertos)}  ({len(aciertos)} numeros)")
    print()
    print("--- SIMULACION MASIVA (10000 sorteos) ---")
    res = simulacion_masiva(10000)
    for n_aciertos in sorted(res):
        porcentaje = res[n_aciertos] / 100
        print(f"  {n_aciertos} aciertos: {res[n_aciertos]} veces ({porcentaje:.1f}%)")
