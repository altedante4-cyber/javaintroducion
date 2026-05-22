import random

def tirar():
    return random.randint(1, 6) + random.randint(1, 6)

def estadisticas(n):
    resultados = {}
    for _ in range(n):
        s = tirar()
        resultados[s] = resultados.get(s, 0) + 1
    return resultados

n = 100000
res = estadisticas(n)
print(f"Simulacion de {n} tiros de 2d6:")
for suma in sorted(res):
    pct = res[suma] / (n / 100)
    barra = "#" * int(pct)
    print(f"  {suma:2d}: {pct:5.1f}% {barra}")
