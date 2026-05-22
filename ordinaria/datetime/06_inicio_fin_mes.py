from datetime import datetime, timedelta
from calendar import monthrange

"""
PATRON: Límites de mes (inicio, fin, bisiestos)
Útil para ejercicios que piden calcular fin de mes,
primer día del mes, años bisiestos, etc.
"""


def ultimo_dia_mes(anio, mes):
    """Último día del mes usando calendar."""
    return monthrange(anio, mes)[1]


def primer_dia_mes(anio, mes):
    return datetime(anio, mes, 1)


def ultimo_dia_mes_dt(anio, mes):
    """Devuelve datetime del último día."""
    ultimo = ultimo_dia_mes(anio, mes)
    return datetime(anio, mes, ultimo)


def ejemplo_limites_mes():
    anio, mes = 2026, 2
    primero = primer_dia_mes(anio, mes)
    ultimo = ultimo_dia_mes_dt(anio, mes)

    print(f"Mes: {primero.strftime('%B %Y')}")
    print(f"Primer día: {primero.strftime('%d/%m/%Y')} ({primero.strftime('%A')})")
    print(f"Último día: {ultimo.strftime('%d/%m/%Y')} ({ultimo.strftime('%A')})")
    print(f"Total días: {ultimo_dia_mes(anio, mes)}")


def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


def ejemplo_bisiestos():
    for anio in [2024, 2025, 2026, 2027, 2028, 1900, 2000]:
        print(f"{anio}: {'Bisiesto' if es_bisiesto(anio) else 'No bisiesto'}")


def siguiente_mes(anio, mes):
    """Obtener el siguiente mes (maneja diciembre -> enero)."""
    if mes == 12:
        return anio + 1, 1
    return anio, mes + 1


def mes_anterior(anio, mes):
    """Obtener el mes anterior."""
    if mes == 1:
        return anio - 1, 12
    return anio, mes - 1


def ejemplo_navegar_meses():
    anio, mes = 2026, 12
    print(f"Actual: {mes}/{anio}")

    sig_anio, sig_mes = siguiente_mes(anio, mes)
    print(f"Siguiente: {sig_mes}/{sig_anio}")

    ant_anio, ant_mes = mes_anterior(anio, mes)
    print(f"Anterior: {ant_mes}/{ant_anio}")


def primer_dia_mes_siguiente(anio, mes):
    """Primer día del mes siguiente."""
    sig_anio, sig_mes = siguiente_mes(anio, mes)
    return datetime(sig_anio, sig_mes, 1)


def ejemplo_trimestres():
    """Agrupar fechas por trimestre."""
    fechas = [
        datetime(2026, 1, 15),
        datetime(2026, 3, 22),
        datetime(2026, 5, 10),
        datetime(2026, 9, 5),
        datetime(2026, 12, 25),
    ]

    for dt in fechas:
        trimestre = (dt.month - 1) // 3 + 1
        print(f"{dt.strftime('%d/%m/%Y')} -> T{trimestre}")


if __name__ == "__main__":
    ejemplo_limites_mes()
    print()
    ejemplo_bisiestos()
    print()
    ejemplo_navegar_meses()
    print()
    ejemplo_trimestres()
