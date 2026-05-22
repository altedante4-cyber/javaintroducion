import random
import math

def construir_nave(nombres, modelos, colores):
    """
    Construye una nave espacial con atributos aleatorios.
    Retorna una lista: ["Nombre Modelo", "Color", Velocidad, Manejo, Escudo].
    """
    nombre_elegido = random.choice(nombres)
    modelo_elegido = random.choice(modelos)
    color_elegido = random.choice(colores)

    velocidad = random.randint(100, 300)
    manejo = 400 - velocidad
    escudo = 2 * manejo
    
    # Guardamos el escudo inicial para la función reparar_escudo
    return [f"{nombre_elegido} {modelo_elegido}", color_elegido, velocidad, manejo, escudo, escudo] # Último elemento es escudo_maximo_inicial

def la_mas_rapida(*naves):
    """
    Recibe un número variable de naves y devuelve la más rápida.
    """
    if not naves:
        return None

    nave_mas_rapida = naves[0]
    for nave in naves:
        if nave[2] > nave_mas_rapida[2]: # Comparar por Velocidad (índice 2)
            nave_mas_rapida = nave
    return nave_mas_rapida

def sigue_en_carrera(nave):
    """
    Verifica si la nave tiene escudo > 0.
    """
    return nave[4] > 0 # Escudo está en el índice 4

def ataque_laser(atacante, defensora):
    """
    Simula un ataque láser. El daño es la mitad de la velocidad del atacante.
    """
    dano = math.floor(atacante[2] / 2) # Velocidad está en el índice 2
    defensora[4] -= dano # Escudo está en el índice 4
    print(f"{atacante[0]} ataca a {defensora[0]} causando {dano} de daño. Escudo de {defensora[0]}: {defensora[4]}")

def reparar_escudo(nave, puntos):
    """
    Repara el escudo de la nave sin superar su valor máximo inicial.
    """
    escudo_actual = nave[4]
    escudo_maximo_inicial = nave[5] # Escudo máximo inicial está en el índice 5
    
    nave[4] = min(escudo_actual + puntos, escudo_maximo_inicial)
    print(f"{nave[0]} repara {puntos} de escudo. Escudo actual: {nave[4]}")

def duelo_espacial(nave1, nave2):
    """
    Simula un duelo espacial entre dos naves.
    """
    print(f"\n--- Duelo Espacial: {nave1[0]} vs {nave2[0]} ---")

    if not sigue_en_carrera(nave1) or not sigue_en_carrera(nave2):
        print("Error: Una o ambas naves no pueden combatir (escudo <= 0).")
        return
    if nave1 == nave2:
        print("Error: Una nave no puede combatir contra sí misma.")
        return

    # Determinar quién ataca primero por Manejo (índice 3)
    if nave1[3] >= nave2[3]:
        atacante = nave1
        defensor = nave2
    else:
        atacante = nave2
        defensor = nave1
    
    print(f"La nave con mayor manejo, {atacante[0]}, ataca primero.")

    while sigue_en_carrera(nave1) and sigue_en_carrera(nave2):
        ataque_laser(atacante, defensor)
        if not sigue_en_carrera(defensor):
            print(f"¡{defensor[0]} ha sido destruida!")
            print(f"¡{atacante[0]} es la ganadora del duelo!")
            return
        
        # Intercambiar roles
        atacante, defensor = defensor, atacante

# --- Flujo del programa principal ---
if __name__ == "__main__":
    print("Iniciando Ejercicio 1: Simulador de Carreras de Naves Espaciales")

    nombres_posibles = ["Estrella", "Cometa", "Nebulosa", "Galaxia"]
    modelos_posibles = ["X-Wing", "Tie Fighter", "Millennium", "Enterprise"]
    colores_posibles = ["Rojo", "Azul", "Verde", "Plata"]

    # Construir naves
    nave_a = construir_nave(nombres_posibles, modelos_posibles, colores_posibles)
    nave_b = construir_nave(nombres_posibles, modelos_posibles, colores_posibles)
    nave_c = construir_nave(nombres_posibles, modelos_posibles, colores_posibles)

    print("\n--- Naves Creadas ---")
    print(f"Nave A: {nave_a}")
    print(f"Nave B: {nave_b}")
    print(f"Nave C: {nave_c}")

    # La más rápida
    rapida = la_mas_rapida(nave_a, nave_b, nave_c)
    if rapida:
        print(f"\nLa nave más rápida es: {rapida[0]} con {rapida[2]} de velocidad.")

    # Duelo espacial
    duelo_espacial(nave_a, nave_b)

    # Reparar escudo de la nave C
    print("\n--- Reparación de Escudo ---")
    print(f"Escudo de {nave_c[0]} antes de reparar: {nave_c[4]}")
    reparar_escudo(nave_c, 50) # Reparar 50 puntos
    print(f"Escudo de {nave_c[0]} después de reparar: {nave_c[4]}")
    reparar_escudo(nave_c, 200) # Intentar reparar más allá del máximo
    print(f"Escudo de {nave_c[0]} después de intentar reparar mucho: {nave_c[4]}")

    print("\nFin del Ejercicio 1.")
