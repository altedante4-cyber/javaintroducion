from datetime import datetime, timedelta

"""
PATRON: Aritmética con timedelta
Útil para ejercicios que suman/restan días, semanas, horas
o calculan intervalos entre fechas.
"""


def sumar_y_restar():
    ahora = datetime.now()

    # Sumar días
    manana = ahora + timedelta(days=1)
    print(f"Mañana: {manana.day}")

    # Restar días
    ayer = ahora - timedelta(days=1)
    print(f"Ayer: {ayer.day}")

    # Sumar semanas
    en_2_semanas = ahora + timedelta(weeks=2)
    print(f"En 2 semanas: {en_2_semanas.day}")

    # Sumar horas / minutos
    en_3_horas = ahora + timedelta(hours=3)
    en_30_min = ahora + timedelta(minutes=30)
    en_90_seg = ahora + timedelta(seconds=90)


def intervalo_entre_fechas():
    """Calcular diferencia entre dos fechas."""
    inicio = datetime(2026, 1, 1)
    fin = datetime(2026, 12, 31)
    delta = fin - inicio  # timedelta

    print(f"Días transcurridos: {delta.days}")
    print(f"Segundos totales: {delta.total_seconds()}")
    print(f"Horas totales: {delta.total_seconds() / 3600:.2f}")


def iterar_con_pasos():
    """Generar fechas saltando de N en N días."""
    inicio = datetime.now()
    paso = timedelta(days=7)  # semanal

    for i in range(5):
        fecha = inicio + paso * i
        print(f"Iteración {i+1}: {fecha.strftime('%d/%m/%Y')}")


def calendario_revisiones():
    """
    Patrón típico de ejercicios de taller/suscripciones:
    fechas de revisión cada X días desde una fecha inicial.
    """
    registro = datetime.now()
    intervalo = timedelta(days=200)

    print("Revisiones programadas:")
    for i in range(1, 7):
        cita = registro + intervalo * i
        print(f"  Revisión {i}: {cita.strftime('%d/%m/%Y')}")


if __name__ == "__main__":
    sumar_y_restar()
    print()
    intervalo_entre_fechas()
    print()
    iterar_con_pasos()
    print()
    calendario_revisiones()
