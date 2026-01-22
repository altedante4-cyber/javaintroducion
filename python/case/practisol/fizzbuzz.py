# ----------------------------------------------------
# Ejercicio 3: Generador de Secuencia Numérica Condicional (FizzBuzz)
# ----------------------------------------------------

def generar_fizzbuzz():
    """
    Genera la secuencia numérica del 1 al N, reemplazando números
    divisibles por 3, 5, o ambos.
    """
    try:
        # Pide la entrada y la convierte a entero
        limite_superior = int(input("Ingrese el número límite (N, ej: 15): "))
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")
        return

    resultados = []
    
    # Bucle FOR para recorrer los números desde 1 hasta el límite superior (incluido)
    # range(1, N + 1) asegura que N se incluya.
    for n in range(1, limite_superior + 1):
        salida = ""
        
        # 1. VERIFICACIÓN CRÍTICA (Divisible por 3 Y 5)
        # Esto debe ir primero para que los números como 15 no caigan en 'Fizz' o 'Buzz'
        if n % 3 == 0 and n % 5 == 0:
            salida = "FizzBuzz"
            
        # 2. Divisible por 3 solamente
        elif n % 3 == 0:
            salida = "Fizz"
            
        # 3. Divisible por 5 solamente
        elif n % 5 == 0:
            salida = "Buzz"
            
        # 4. Caso por defecto (No divisible por 3 ni por 5)
        else:
            # Convertir el número a cadena para que la lista contenga solo strings
            salida = str(n)
            
        resultados.append(salida)

    # Imprimir el resultado final separado por comas
    print("Secuencia generada:")
    print(", ".join(resultados))

# Ejecutar la función principal
generar_fizzbuzz()