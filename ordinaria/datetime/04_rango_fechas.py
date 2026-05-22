from datetime import datetime, timedelta

"""
PATRON: Generación de rangos de fechas
Útil para ejercicios que piden listar todos los días entre dos fechas,
generar calendarios, o iterar día a día.
"""


def rango_dias(inicio, fin):
    """Genera lista de días entre dos fechas (inclusive)."""
    fechas = []
    actual = inicio
    while actual <= fin:
        fechas.append(actual)
        actual += timedelta(days=1)
    return fechas


def listar_dias_entre():
    inicio = datetime(2026, 5, 1)
    fin = datetime(2026, 5, 10)

    for dt in rango_dias(inicio, fin):
        print(dt.strftime("%d/%m/%Y"))


def generador_por_semana():
    """Iterar semana a semana desde hoy."""
    hoy = datetime.now()

    for i in range(4):
        fecha = hoy + timedelta(weeks=i)
        print(f"Semana {i+1}: {fecha.strftime('%d/%m/%Y')}")


def contar_dias_por_mes():
    """Días totales de cada mes en un rango."""
    inicio = datetime(2026, 1, 1)
    fin = datetime(2026, 12, 31)

    actual = inicio
    while actual <= fin:
        # Último día del mes actual
        if actual.month == 12:
            ultimo = datetime(actual.year, 12, 31)
        else:
            ultimo = datetime(actual.year, actual.month + 1, 1) - timedelta(days=1)

        dias = (ultimo - actual).days + 1
        print(f"{actual.strftime('%B %Y')}: {dias} días")

        # Avanzar al primer día del siguiente mes
        if actual.month == 12:
            actual = datetime(actual.year + 1, 1, 1)
        else:
            actual = datetime(actual.year, actual.month + 1, 1)


def listar_fechas_hasta_hoy():
    """Patrón: contar días desde una fecha hasta hoy."""
    nacimiento = datetime(1990, 6, 15)
    hoy = datetime.now()

    cumples = []
    anio = nacimiento.year
    while anio <= hoy.year:
        try:
            cumple = datetime(anio, nacimiento.month, nacimiento.day)
            cumples.append(cumple)
        except ValueError:
            # 29 feb en año no bisiesto -> pasar al 28
            cumple = datetime(anio, nacimiento.month, nacimiento.day - 1)
            cumples.append(cumple)
        anio += 1

    print(f"Cumpleaños desde {cumples[0].year} hasta {cumples[-1].year}:")
    for c in cumples:
        print(f"  {c.strftime('%d/%m/%Y')} ({c.strftime('%A')})")


if __name__ == "__main__":
    listar_dias_entre()
    print()
    generador_por_semana()
    print()
    contar_dias_por_mes()
    print()
    listar_fechas_hasta_hoy()
