from datetime import datetime, timedelta

"""
PATRON: Días laborales y fines de semana
Útil para ejercicios de facturación, plazos hábiles,
contar días laborables entre fechas.
"""


def es_fin_semana(dt):
    return dt.weekday() >= 5  # 5=sábado, 6=domingo


def es_laboral(dt):
    return dt.weekday() < 5


def contar_laborales_entre(inicio, fin):
    """Cuenta días laborables entre dos fechas."""
    count = 0
    actual = inicio
    while actual <= fin:
        if es_laboral(actual):
            count += 1
        actual += timedelta(days=1)
    return count


def ejemplo_contar_laborales():
    inicio = datetime(2026, 5, 1)
    fin = datetime(2026, 5, 31)

    total = (fin - inicio).days + 1
    laborales = contar_laborales_entre(inicio, fin)
    fines = total - laborales

    print(f"Del {inicio.strftime('%d/%m')} al {fin.strftime('%d/%m/%Y')}:")
    print(f"  Total días: {total}")
    print(f"  Laborables: {laborales}")
    print(f"  Fines de semana: {fines}")


def sumar_dias_laborables(desde, num_dias):
    """Avanza N días laborables desde una fecha."""
    actual = desde
    while num_dias > 0:
        actual += timedelta(days=1)
        if es_laboral(actual):
            num_dias -= 1
    return actual


def ejemplo_sumar_laborales():
    hoy = datetime.now()
    en_10_laborales = sumar_dias_laborables(hoy, 10)
    print(f"Hoy: {hoy.strftime('%d/%m/%Y')} ({hoy.strftime('%A')})")
    print(f"En 10 días laborables: {en_10_laborales.strftime('%d/%m/%Y')} ({en_10_laborales.strftime('%A')})")


def listar_solo_laborales():
    """Listar solo días laborables de un mes."""
    from calendar import monthrange

    anio, mes = 2026, 5
    dias_mes = monthrange(anio, mes)[1]

    print(f"Días laborables de {mes}/{anio}:")
    for dia in range(1, dias_mes + 1):
        dt = datetime(anio, mes, dia)
        if es_laboral(dt):
            print(f"  {dt.strftime('%d/%m - %A')}")


if __name__ == "__main__":
    ejemplo_contar_laborales()
    print()
    ejemplo_sumar_laborales()
    print()
    listar_solo_laborales()
