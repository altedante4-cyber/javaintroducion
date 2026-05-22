from datetime import datetime, timezone, timedelta

"""
PATRON: Zonas horarias y UTC
Útil para ejercicios que trabajan con husos horarios,
conversión a UTC, hora local vs global.
NOTA: Para zona horaria localizada (ej: "Europe/Madrid")
se necesita la librería 'pytz' o 'zoneinfo' (Python 3.9+).
"""


def utc_ahora():
    """Obtener la hora actual en UTC."""
    ahora_utc = datetime.now(timezone.utc)
    print(f"UTC ahora: {ahora_utc.strftime('%Y-%m-%d %H:%M:%S %Z')}")


def hora_local_sin_timezone():
    """datetime.now() sin zona -> hora local ingenua."""
    local = datetime.now()
    print(f"Local (naive): {local.strftime('%Y-%m-%d %H:%M:%S')}")


def convertir_a_utc():
    """Convertir hora local naive a UTC asumiendo UTC+2."""
    local = datetime.now()
    # Asignar un offset fijo
    local_con_tz = local.replace(tzinfo=timezone(timedelta(hours=2)))
    utc = local_con_tz.astimezone(timezone.utc)
    print(f"Local+2: {local_con_tz.strftime('%H:%M')}")
    print(f"UTC:     {utc.strftime('%H:%M')}")


def diferencia_husos():
    """
    Calcular diferencia horaria entre dos zonas.
    Usando offsets fijos (sin pytz/zoneinfo).
    """
    madrid = timezone(timedelta(hours=2))
    ny = timezone(timedelta(hours=-4))

    ahora_madrid = datetime.now(madrid)
    ahora_ny = ahora_madrid.astimezone(ny)

    print(f"Madrid: {ahora_madrid.strftime('%H:%M')}")
    print(f"NY:     {ahora_ny.strftime('%H:%M')}")


def timestamp_unix():
    """Convertir a/desde timestamp Unix."""
    ahora = datetime.now()

    # datetime -> timestamp (segundos desde 1970-01-01 UTC)
    ts = ahora.timestamp()
    print(f"Timestamp Unix: {ts}")

    # timestamp -> datetime
    dt_desde_ts = datetime.fromtimestamp(ts)
    print(f"Desde timestamp: {dt_desde_ts.strftime('%Y-%m-%d %H:%M:%S')}")

    # timestamp -> datetime UTC
    dt_utc = datetime.fromtimestamp(ts, tz=timezone.utc)
    print(f"Desde timestamp UTC: {dt_utc.strftime('%Y-%m-%d %H:%M:%S %Z')}")


def tiempo_transcurrido_epoch():
    """Segundos transcurridos desde una fecha."""
    inicio = datetime(2026, 1, 1)
    ahora = datetime.now()
    segundos = (ahora - inicio).total_seconds()
    print(f"Segundos desde 01/01/2026: {segundos:.2f}")


if __name__ == "__main__":
    utc_ahora()
    print()
    hora_local_sin_timezone()
    print()
    convertir_a_utc()
    print()
    diferencia_husos()
    print()
    timestamp_unix()
    print()
    tiempo_transcurrido_epoch()
