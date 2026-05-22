from datetime import datetime

"""
PATRON: Comparación de fechas
Útil para ejercicios que ordenan, filtran o clasifican fechas
(anteriores / posteriores a una referencia, normalmente "hoy").
"""


def comparar_con_hoy():
    hoy = datetime.now()
    fechas = [
        datetime(2025, 1, 15),
        datetime(2026, 6, 1),
        datetime(2027, 12, 25),
        hoy,
    ]

    for dt in fechas:
        if dt < hoy:
            print(f"{dt.date()} -> ANTERIOR a hoy")
        elif dt == hoy:
            print(f"{dt.date()} -> HOY")
        else:
            print(f"{dt.date()} -> POSTERIOR a hoy")


def clasificar_lista_strings():
    """
    Patrón clásico: recibir strings, parsear, clasificar.
    """
    cadenas = ["13/02/25", "14/06/2026", "01/01/2020", "25/12/2027"]
    hoy = datetime.now()
    formatos = ["%d/%m/%y", "%d/%m/%Y"]

    anteriores = []
    posteriores = []

    for cad in cadenas:
        for fmt in formatos:
            try:
                dt = datetime.strptime(cad, fmt)
                break
            except ValueError:
                continue
        else:
            continue

        if dt < hoy:
            anteriores.append(cad)
        else:
            posteriores.append(cad)

    print(f"Anteriores a hoy: {anteriores}")
    print(f"Posteriores a hoy: {posteriores}")


def ordenar_fechas():
    fechas = [
        datetime(2026, 5, 22),
        datetime(2025, 12, 1),
        datetime(2026, 1, 15),
        datetime(2024, 8, 10),
    ]

    print("Original:", [f.date() for f in fechas])
    print("Ascendente:", [f.date() for f in sorted(fechas)])
    print("Descendente:", [f.date() for f in sorted(fechas, reverse=True)])

    # Fecha más antigua / más reciente
    print(f"Más antigua: {min(fechas).date()}")
    print(f"Más reciente: {max(fechas).date()}")


def filtrar_por_rango():
    inicio = datetime(2026, 1, 1)
    fin = datetime(2026, 12, 31)

    fechas = [
        datetime(2025, 6, 15),
        datetime(2026, 3, 10),
        datetime(2026, 7, 22),
        datetime(2027, 1, 5),
    ]

    dentro = [f for f in fechas if inicio <= f <= fin]
    fuera = [f for f in fechas if f < inicio or f > fin]

    print(f"Dentro de 2026: {[f.date() for f in dentro]}")
    print(f"Fuera de 2026: {[f.date() for f in fuera]}")


if __name__ == "__main__":
    comparar_con_hoy()
    print()
    clasificar_lista_strings()
    print()
    ordenar_fechas()
    print()
    filtrar_por_rango()
