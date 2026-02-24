def obtener_clima(ciudad_dia_tupla):
    # Usamos una tupla (Ciudad, Fecha) como clave única
    historico = {
        ("Madrid", "2026-01-22"): "Soleado",
        ("Barcelona", "2026-01-22"): "Nublado"
    }
    return historico.get(ciudad_dia_tupla, "Sin datos")

print(obtener_clima(("Madrid", "2026-01-22")))