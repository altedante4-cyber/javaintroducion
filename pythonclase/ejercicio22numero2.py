from datetime import datetime

fechas_input = ["13/02/25", "hola carmela", "12 34 56", "14/06/2026", "bra, bra", "56/13/26"]

correctas_pasado = []
correctas_futuro = []
incorrectas = []

hoy = datetime.now()

# Definimos los formatos posibles (con año de 2 y 4 dígitos)
formatos = ["%d/%m/%y", "%d/%m/%Y"]

for cadena in fechas_input:
    es_valida = False
    fecha_objeto = None
    
    # Intentamos parsear con ambos formatos
    for fmt in formatos:
        try:
            fecha_objeto = datetime.strptime(cadena, fmt)
            es_valida = True
            break # Si funciona, salimos del bucle de formatos
        except ValueError:
            continue
    
    if es_valida:
        # Ejercicio 3: Separar por fecha actual
        if fecha_objeto < hoy:
            correctas_pasado.append(cadena)
        else:
            correctas_futuro.append(cadena)
    else:
        # Ejercicio 2: Guardar las incorrectas
        incorrectas.append(cadena)

# --- Salida por consola ---
print("Fechas correctas ANTERIORES a hoy:")
for f in correctas_pasado: print(f"  {f}")

print("\nFechas correctas POSTERIORES a hoy:")
for f in correctas_futuro: print(f"  {f}")

print("\nFechas incorrectas:")
for f in incorrectas: print(f"  {f}")