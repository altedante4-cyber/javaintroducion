import random

print("🎮 PIENSA UN NÚMERO ENTRE 0 Y 100 🎮")
print("Yo intentaré adivinarlo en 5 intentos")
print("Responde con: 'mayor', 'menor' o 'correcto'\n")

# Inicialización
minimo = 0
maximo = 100
intentos = 0
adivinado = False

while intentos < 5 and not adivinado:
    intentos += 1

    # La máquina propone un número (estrategia de búsqueda binaria)
    propuesta = (minimo + maximo) // 2

    print(f"Intento {intentos}/5: ¿Es el {propuesta}?")
    respuesta = input("Tu número es (mayor/menor/correcto): ").lower().strip()

    if respuesta == "correcto":
        print(f"\n¡JA! Lo adiviné en {intentos} intento(s)")
        adivinado = True
    elif respuesta == "mayor":
        minimo = propuesta + 1
        print(f"Ok, tu número es MAYOR que {propuesta}")
    elif respuesta == "menor":
        maximo = propuesta - 1
        print(f"Ok, tu número es MENOR que {propuesta}")
    else:
        print("Respuesta no válida. Usa: mayor, menor o correcto")
        intentos -= 1  # No contar este intento

    print(f"Rango actual: {minimo}-{maximo}\n")

if not adivinado:
    print(f"\n¡No pude adivinarlo en 5 intentos!")
    print("¿Seguro que estabas pensando en un número entre 0 y 100?")