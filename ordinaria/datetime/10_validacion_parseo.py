from datetime import datetime

"""
PATRON: Validación y parseo robusto de fechas
Útil para ejercicios donde las entradas son impredecibles:
strings inválidos, múltiples formatos, datos sucios.
"""


def parsear_fecha_estricta(cadena, formatos):
    """
    Intenta parsear una cadena con varios formatos.
    Retorna (datetime|None, formato_que_funciono|None).
    """
    for fmt in formatos:
        try:
            dt = datetime.strptime(cadena, fmt)
            return dt, fmt
        except ValueError:
            continue
    return None, None


def ejemplo_parseo_multiple():
    cadenas = [
        "13/02/25",
        "14/06/2026",
        "hola carmela",
        "12 34 56",
        "56/13/26",
        "2026-05-22",
        "May 22 2026",
    ]
    formatos = ["%d/%m/%y", "%d/%m/%Y", "%Y-%m-%d", "%b %d %Y"]

    print("Parseo múltiple:")
    for cad in cadenas:
        dt, fmt = parsear_fecha_estricta(cad, formatos)
        if dt:
            print(f"  OK: '{cad}' (fmt={fmt}) -> {dt}")
        else:
            print(f"  ERROR: '{cad}' no se pudo parsear")


def validar_fecha_valida(anio, mes, dia):
    """
    Verificar si una fecha es válida (ej: 30/02 no es válida).
    """
    try:
        dt = datetime(anio, mes, dia)
        return True
    except ValueError:
        return False


def ejemplo_validar_fechas():
    pruebas = [
        (2026, 2, 28),
        (2026, 2, 29),  # 2026 no es bisiesto
        (2024, 2, 29),  # 2024 sí es bisiesto
        (2026, 4, 31),  # Abril tiene 30 días
        (2026, 13, 1),  # Mes 13 no existe
    ]

    print("Validación de fechas:")
    for anio, mes, dia in pruebas:
        if validar_fecha_valida(anio, mes, dia):
            print(f"  {dia:02d}/{mes:02d}/{anio} -> VÁLIDA")
        else:
            print(f"  {dia:02d}/{mes:02d}/{anio} -> INVÁLIDA")


def sanitizar_fecha(cadena):
    """
    Limpiar y normalizar una cadena antes de parsear.
    """
    cad = cadena.strip()

    # Reemplazar separadores comunes por /
    for sep in ["-", ".", "_", " "]:
        cad = cad.replace(sep, "/")

    # Eliminar caracteres no numéricos excepto /
    partes = []
    for parte in cad.split("/"):
        limpio = "".join(c for c in parte if c.isdigit())
        if limpio:
            partes.append(limpio)

    if len(partes) == 3:
        return "/".join(partes)
    return cadena  # devolver original si no se pudo


def ejemplo_sanitizar():
    sucias = [
        "13-02-2025",
        "14.06.2026",
        " 22/05/2026 ",
        "2026_05_22",
    ]

    print("Sanitización de fechas:")
    for sucia in sucias:
        limpia = sanitizar_fecha(sucia)
        dt, _ = parsear_fecha_estricta(limpia, ["%d/%m/%Y", "%Y/%m/%d"])
        resultado = dt.strftime("%d/%m/%Y") if dt else "NO VÁLIDA"
        print(f"  '{sucia}' -> '{limpia}' -> {resultado}")


def clasificar_con_validacion(lista_cadenas):
    """
    Patrón completo: parsear, validar y clasificar.
    Devuelve (correctas, incorrectas).
    """
    formatos = ["%d/%m/%y", "%d/%m/%Y", "%Y-%m-%d"]
    correctas = []
    incorrectas = []

    for cad in lista_cadenas:
        dt, _ = parsear_fecha_estricta(cad, formatos)
        if dt:
            correctas.append((cad, dt))
        else:
            incorrectas.append(cad)

    return correctas, incorrectas


def ejemplo_clasificar():
    datos = ["13/02/25", "hola carmela", "12 34 56", "14/06/2026", "56/13/26"]
    correctas, incorrectas = clasificar_con_validacion(datos)

    print("Clasificación final:")
    print(f"  Correctas ({len(correctas)}):")
    for cad, dt in correctas:
        print(f"    {cad} -> {dt}")
    print(f"  Incorrectas ({len(incorrectas)}):")
    for cad in incorrectas:
        print(f"    {cad}")


if __name__ == "__main__":
    ejemplo_parseo_multiple()
    print()
    ejemplo_validar_fechas()
    print()
    ejemplo_sanitizar()
    print()
    ejemplo_clasificar()
