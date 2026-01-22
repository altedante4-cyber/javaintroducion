# ----------------------------------------------------
# Problema de Práctica 1: Conversor de Temperatura
# ----------------------------------------------------

# --- Constantes de Fórmulas ---
FACTOR_F = 9 / 5
OFFSET_F = 32
OFFSET_K = 273.15

def convertir_temperatura():
    """
    Convierte temperaturas entre Celsius, Fahrenheit y Kelvin.
    """
    
    # 1. Entrada y Preparación de datos
    temperatura_raw = input("Ingrese la temperatura (ej. 25.0C): ")

    # La moneda (unidad) es la última letra. La cantidad es todo lo demás.
    unidad = temperatura_raw[-1].upper()
    
    # Reemplaza la coma por punto (si se usó) y separa la cantidad
    cantidad_str = temperatura_raw[:-1].replace(',', '.')
    
    # Convertir a float para aceptar números decimales
    try:
        cantidad = float(cantidad_str)
    except ValueError:
        # Esto maneja casos como 'ABC' o si la entrada es solo la letra
        print("Error: La cantidad debe ser un número válido.")
        return

    # 2. Lógica de Conversión usando condicionales (match/case)
    
    match unidad:
        
        case 'C':
            # REGLA: Si la entrada es Celsius (C), convertir a Fahrenheit y Kelvin.
            
            resultado_fahrenheit = (cantidad * FACTOR_F) + OFFSET_F
            resultado_kelvin = cantidad + OFFSET_K
            
            # Formato de salida con TRES cifras decimales (:.3f)
            print(
                f"{cantidad} grados Celsius equivalen a {resultado_fahrenheit:.3f} grados Fahrenheit "
                f"y {resultado_kelvin:.3f} grados Kelvin."
            )
            
        case 'F':
            # REGLA: Si la entrada es Fahrenheit (F), dar SÓLO el resultado en Celsius.
            
            # Fórmula de F a C: C = (F - 32) * 5/9. (5/9 es la inversa de FACTOR_F)
            resultado_celcius = (cantidad - OFFSET_F) * (1 / FACTOR_F)
            
            # Formato de salida con TRES cifras decimales (:.3f)
            print(
                f"{cantidad} grados Fahrenheit equivalen a {resultado_celcius:.3f} grados Celsius."
            )

        case 'K':
            # REGLA: Si la entrada es Kelvin (K), dar SÓLO el resultado en Celsius.
            
            # Fórmula de K a C: C = K - 273.15
            resultado_celcius = cantidad - OFFSET_K
            
            # Formato de salida con TRES cifras decimales (:.3f)
            print(
                f"{cantidad} grados Kelvin equivalen a {resultado_celcius:.3f} grados Celsius."
            )
            
        case _:
            print("Error: Unidad de temperatura no reconocida. Use C, F o K.")

# Ejecutar la función principal
convertir_temperatura()