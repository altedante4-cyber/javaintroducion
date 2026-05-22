from datetime import datetime, timezone, timedelta

"""
PATRON: Formatos ISO 8601 y RFC
Útil para ejercicios de interoperabilidad (APIs, JSON, BD),
conversión entre string ISO y datetime.
"""


def isoformat_salida():
    """datetime -> string ISO 8601."""
    ahora = datetime.now()

    # ISO básico
    iso1 = ahora.isoformat()
    print(f"isoformat():      {iso1}")

    # ISO con separador ' '
    iso2 = ahora.isoformat(sep=" ")
    print(f"isoformat(sep=' '): {iso2}")

    # ISO con zona horaria
    ahora_tz = ahora.replace(tzinfo=timezone(timedelta(hours=2)))
    iso3 = ahora_tz.isoformat()
    print(f"isoformat() +tz:  {iso3}")

    # ISO UTC
    ahora_utc = datetime.now(timezone.utc)
    iso4 = ahora_utc.isoformat()
    print(f"isoformat() UTC:  {iso4}")


def iso_formatos_strftime():
    """Formatos ISO usando strftime."""
    ahora = datetime.now()

    print(f"YYYY-MM-DD:       {ahora.strftime('%Y-%m-%d')}")
    print(f"YYYY-MM-DD HH:MM: {ahora.strftime('%Y-%m-%d %H:%M')}")
    print(f"ISO 8601 completo: {ahora.strftime('%Y-%m-%dT%H:%M:%S')}")
    print(f"RFC 2822:         {ahora.strftime('%a, %d %b %Y %H:%M:%S %z')}")


def desde_iso():
    """String ISO -> datetime."""
    cadenas = [
        "2026-05-22",
        "2026-05-22T14:30:00",
        "2026-05-22T14:30:00+02:00",
        "2026-05-22 14:30:00",
        "2026-05-22T14:30:00.123456",
    ]

    for cad in cadenas:
        try:
            # fromisoformat() maneja muchos formatos ISO
            dt = datetime.fromisoformat(cad)
            print(f"OK: '{cad}' -> {dt}")
        except ValueError as e:
            print(f"ERROR: '{cad}' -> {e}")


def formato_iso_ejercicio_clasico():
    """
    Patrón típico: fechas vienen en ISO de una API/BD
    y hay que procesarlas.
    """
    datos_api = [
        {"id": 1, "fecha": "2026-05-22", "evento": "Revisión"},
        {"id": 2, "fecha": "2026-06-15", "evento": "Entrega"},
        {"id": 3, "fecha": "2026-07-01", "evento": "Pago"},
    ]

    hoy = datetime.now()

    for item in datos_api:
        dt = datetime.fromisoformat(item["fecha"])
        dias_restan = (dt - hoy).days

        estado = (
            "PASADO"
            if dias_restan < 0
            else "HOY" if dias_restan == 0 else f"Faltan {dias_restan} día(s)"
        )
        print(f"{item['evento']} ({item['fecha']}): {estado}")


if __name__ == "__main__":
    isoformat_salida()
    print()
    iso_formatos_strftime()
    print()
    desde_iso()
    print()
    formato_iso_ejercicio_clasico()
