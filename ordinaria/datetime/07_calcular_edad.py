from datetime import datetime, timedelta

"""
PATRON: Cálculo de edad y diferencias en años/meses/días
Útil para ejercicios de edad exacta, antigüedad,
tiempo transcurrido desde una fecha.
"""


def edad_exacta(fecha_nac):
    """Años, meses y días cumplidos hasta hoy."""
    hoy = datetime.now()

    anios = hoy.year - fecha_nac.year
    meses = hoy.month - fecha_nac.month
    dias = hoy.day - fecha_nac.day

    # Ajuste si el día del mes es negativo
    if dias < 0:
        # Restamos un mes y sumamos los días del mes anterior
        meses -= 1
        mes_anterior = hoy.month - 1 if hoy.month > 1 else 12
        anio_anterior = hoy.year if mes_anterior != 12 else hoy.year - 1
        dias_del_mes_anterior = (
            datetime(anio_anterior, mes_anterior + 1, 1) - timedelta(days=1)
        ).day if mes_anterior < 12 else 31
        dias += dias_del_mes_anterior

    # Ajuste si los meses son negativos
    if meses < 0:
        anios -= 1
        meses += 12

    return anios, meses, dias


def ejemplo_edad():
    nacimiento = datetime(1990, 6, 15)
    anios, meses, dias = edad_exacta(nacimiento)
    print(f"Fecha nacimiento: {nacimiento.strftime('%d/%m/%Y')}")
    print(f"Edad: {anios} años, {meses} meses, {dias} días")


def dias_hasta_cumpleanos():
    """Días restantes hasta el próximo cumpleaños."""
    hoy = datetime.now()
    nacimiento = datetime(1990, 6, 15)

    prox_cumple = datetime(hoy.year, nacimiento.month, nacimiento.day)
    if prox_cumple < hoy:
        # Ya pasó este año, calcular para el siguiente
        prox_cumple = datetime(hoy.year + 1, nacimiento.month, nacimiento.day)

    restan = (prox_cumple - hoy).days
    print(f"Próximo cumpleaños: {prox_cumple.strftime('%d/%m/%Y')}")
    print(f"Días restantes: {restan}")


def tiempo_transcurrido_desde(fecha_evento):
    """Texto legible de tiempo desde un evento."""
    ahora = datetime.now()
    delta = ahora - fecha_evento

    if delta.days >= 365:
        anios = delta.days // 365
        return f"Hace {anios} año(s)"
    elif delta.days >= 30:
        meses = delta.days // 30
        return f"Hace {meses} mes(es)"
    elif delta.days > 0:
        return f"Hace {delta.days} día(s)"
    elif delta.seconds >= 3600:
        return f"Hace {delta.seconds // 3600} hora(s)"
    elif delta.seconds >= 60:
        return f"Hace {delta.seconds // 60} minuto(s)"
    else:
        return "Hace unos segundos"


def ejemplo_tiempo_transcurrido():
    eventos = [
        datetime(2020, 3, 15),
        datetime(2025, 1, 1),
        datetime.now() - timedelta(hours=5),
        datetime.now() - timedelta(minutes=20),
    ]
    for ev in eventos:
        print(f"{ev.strftime('%d/%m/%Y %H:%M')} -> {tiempo_transcurrido_desde(ev)}")


def diferencia_entre_fechas_detalle(inicio, fin):
    """Diferencia completa entre dos fechas."""
    if fin < inicio:
        inicio, fin = fin, inicio

    anios = fin.year - inicio.year
    meses = fin.month - inicio.month
    dias = fin.day - inicio.day

    if dias < 0:
        meses -= 1
        mes_anterior = fin.month - 1 if fin.month > 1 else 12
        anio_anterior = fin.year if mes_anterior != 12 else fin.year - 1
        dias_del_mes = (
            datetime(anio_anterior, mes_anterior + 1, 1) - timedelta(days=1)
        ).day if mes_anterior < 12 else 31
        dias += dias_del_mes

    if meses < 0:
        anios -= 1
        meses += 12

    return anios, meses, dias


def ejemplo_diferencia():
    a = datetime(2020, 1, 30)
    b = datetime(2026, 5, 22)
    anios, meses, dias = diferencia_entre_fechas_detalle(a, b)
    print(f"De {a.strftime('%d/%m/%Y')} a {b.strftime('%d/%m/%Y')}:")
    print(f"  {anios} años, {meses} meses, {dias} días")


if __name__ == "__main__":
    ejemplo_edad()
    print()
    dias_hasta_cumpleanos()
    print()
    ejemplo_tiempo_transcurrido()
    print()
    ejemplo_diferencia()
