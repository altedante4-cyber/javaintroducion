import random

dado = (1, 2, 3, 4, 5, 6)

def tirar_dado():
    return random.choice(dado)

def tirar_dados(cantidad):
    return tuple(tirar_dado() for _ in range(cantidad))

def sumar_dados(tiros):
    return sum(tiros)

def clasificar_tiro(tiros):
    total = sumar_dados(tiros)
    if total >= 17:
        return "excelente"
    elif total >= 12:
        return "bueno"
    elif total >= 7:
        return "regular"
    else:
        return "malo"

def historial_tiros(n):
    return {f"tiro_{i+1}": tirar_dados(2) for i in range(n)}

def analizar_historial(historial):
    resumen = {}
    for nombre, tiros in historial.items():
        total = sumar_dados(tiros)
        resumen[nombre] = {
            "valores": tiros,
            "suma": total,
            "clasificacion": clasificar_tiro(tiros),
        }
    return resumen

def simulacion_montecarlo(n=100000):
    conteos = {}
    for _ in range(n):
        tiros = tirar_dados(2)
        s = sumar_dados(tiros)
        conteos[s] = conteos.get(s, 0) + 1
    return conteos

if __name__ == "__main__":
    print("=== JUEGO DE DADOS ===")
    h = historial_tiros(5)
    analisis = analizar_historial(h)
    for nombre, info in analisis.items():
        print(f"  {nombre}: {info['valores']} suma={info['suma']} ({info['clasificacion']})")
    print()
    print("--- SIMULACION 2D6 (100000 tiros) ---")
    sim = simulacion_montecarlo()
    for suma in sorted(sim):
        pct = sim[suma] / 1000
        barra = "#" * int(pct)
        print(f"  Suma {suma:2d}: {sim[suma]:5d} ({pct:.1f}%) {barra}")
