from datetime import datetime

"""
PATRON: Formateo y parseo de fechas
Útil para ejercicios que piden mostrar fechas en distintos formatos
o convertir strings a objetos datetime.
"""

def formatear_con_strftime():
    ahora = datetime.now()

    # Formato numérico corto
    print(ahora.strftime("%d/%m/%Y"))        # 22/05/2026
    print(ahora.strftime("%d/%m/%y"))        # 22/05/26
    print(ahora.strftime("%H:%M:%S"))        # 14:30:00

    # Formato con texto
    print(ahora.strftime("%d de %B de %Y"))  # 22 de May de 2026
    print(ahora.strftime("%A, %d %B %Y"))    # Friday, 22 May 2026

    # Formato con mes/día nombre corto
    print(ahora.strftime("%b %d, %Y"))       # May 22, 2026
    print(ahora.strftime("%a %d-%m-%Y"))     # Fri 22-05-2026

    # Fecha y hora combinados
    print(ahora.strftime("%Y-%m-%d %H:%M:%S"))        # 2026-05-22 14:30:00
    print(ahora.strftime("%d/%m/%Y a las %H:%M"))     # 22/05/2026 a las 14:30

    # Sin relleno de ceros (%-d, %-m en Linux/Mac)
    print(ahora.strftime("%-d del %-m de %Y"))        # 22 del 5 de 2026

    # Trimestre / semana del año
    print(ahora.strftime("%j"))   # día del año (001-366)
    print(ahora.strftime("%W"))   # semana del año (00-53)
    print(ahora.strftime("%w"))   # día de la semana (0=domingo)


def parsear_con_strptime():
    cadenas = [
        "22/05/2026",
        "22/05/26",
        "2026-05-22",
        "May 22 2026",
        "22-05-2026",
    ]
    # Diccionario formato -> ejemplo de salida
    formatos = {
        "%d/%m/%Y": "22/05/2026",
        "%d/%m/%y": "22/05/26",
        "%Y-%m-%d": "2026-05-22",
        "%b %d %Y": "May 22 2026",
        "%d-%m-%Y": "22-05-2026",
    }
    for cadena in cadenas:
        for fmt, ejemplo in formatos.items():
            try:
                dt = datetime.strptime(cadena, fmt)
                print(f"OK: '{cadena}' con formato '{fmt}' -> {dt}")
                break
            except ValueError:
                continue
        else:
            print(f"ERROR: '{cadena}' no coincide con ningún formato")


if __name__ == "__main__":
    print("--- Formateo ---")
    formatear_con_strftime()
    print("\n--- Parseo ---")
    parsear_con_strptime()
