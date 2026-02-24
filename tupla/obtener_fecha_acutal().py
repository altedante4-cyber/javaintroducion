def obtener_fecha_actual():
    # Devolvemos una tupla (día, mes, año)
    return (22, 1, 2026)

# Desempaquetamos directamente al llamar
d, m, a = obtener_fecha_actual()
print(f"Hoy es {d} de {m}")