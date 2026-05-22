import math

def curar_equipo(puntos, *heroes):
    """
    Aplica curación a un número variable de héroes, sin superar su vida máxima.
    Un héroe es una lista: ["Nombre", Nivel, Vida_Actual, Vida_Maxima].
    """
    print(f"\nCurando equipo con {puntos} puntos...")
    for heroe in heroes:
        nombre, nivel, vida_actual, vida_maxima = heroe[0], heroe[1], heroe[2], heroe[3]
        nueva_vida = min(vida_actual + puntos, vida_maxima)
        heroe[2] = nueva_vida
        print(f"{nombre} curado. Vida actual: {heroe[2]}/{heroe[3]}")

def subir_nivel(heroe):
    """
    Aumenta el nivel del héroe, su vida máxima y restaura su vida actual.
    Un héroe es una lista: ["Nombre", Nivel, Vida_Actual, Vida_Maxima].
    """
    nombre, nivel, vida_actual, vida_maxima = heroe[0], heroe[1], heroe[2], heroe[3]
    
    heroe[1] += 1 # Aumenta Nivel
    nueva_vida_maxima = math.ceil(vida_maxima * 1.20)
    heroe[3] = nueva_vida_maxima # Aumenta Vida_Maxima
    heroe[2] = nueva_vida_maxima # Restaura Vida_Actual al nuevo máximo
    print(f"\n{nombre} ha subido al Nivel {heroe[1]}. Nueva Vida Máxima: {heroe[3]}")

def mision_peligrosa(dano_base, *heroes):
    """
    Simula una misión donde los héroes reciben daño.
    Un héroe es una lista: ["Nombre", Nivel, Vida_Actual, Vida_Maxima].
    """
    print(f"\n--- Misión Peligrosa (Daño base: {dano_base}) ---")
    for heroe in heroes:
        nombre, nivel, vida_actual, vida_maxima = heroe[0], heroe[1], heroe[2], heroe[3]
        
        dano_recibido = max(1, dano_base - nivel) # Daño mínimo de 1
        heroe[2] -= dano_recibido
        
        print(f"{nombre} (Nivel {nivel}) recibe {dano_recibido} de daño. Vida actual: {heroe[2]}/{heroe[3]}")
        
        if heroe[2] <= 0:
            print(f"¡{nombre} ha caído en la misión!")

# --- Flujo del programa principal ---
if __name__ == "__main__":
    print("Iniciando Ejercicio 2: Gestión de un Equipo de Héroes")

    # Héroes iniciales: ["Nombre", Nivel, Vida_Actual, Vida_Maxima]
    heroe1 = ["Arturo", 5, 80, 100]
    heroe2 = ["Merlín", 3, 50, 70]
    heroe3 = ["Morgana", 7, 120, 120]

    print("\n--- Estado Inicial de los Héroes ---")
    print(f"Heroe 1: {heroe1}")
    print(f"Heroe 2: {heroe2}")
    print(f"Heroe 3: {heroe3}")

    # Curar equipo
    curar_equipo(20, heroe1, heroe2)
    print(f"Heroe 1 después de curar: {heroe1}")
    print(f"Heroe 2 después de curar: {heroe2}")

    # Subir de nivel a un héroe
    subir_nivel(heroe1)
    print(f"Heroe 1 después de subir de nivel: {heroe1}")

    # Misión peligrosa
    mision_peligrosa(30, heroe1, heroe2, heroe3)
    print("\n--- Estado Final de los Héroes ---")
    print(f"Heroe 1: {heroe1}")
    print(f"Heroe 2: {heroe2}")
    print(f"Heroe 3: {heroe3}")

    # Otra misión para ver si caen
    mision_peligrosa(60, heroe1, heroe2, heroe3)
    print("\n--- Estado Final (segunda misión) de los Héroes ---")
    print(f"Heroe 1: {heroe1}")
    print(f"Heroe 2: {heroe2}")
    print(f"Heroe 3: {heroe3}")

    print("\nFin del Ejercicio 2.")
