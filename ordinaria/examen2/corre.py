import random

def inicializar_torneo(num_participantes):
    """
    Inicializa la estructura de datos para el torneo con todos los participantes activos.
    Retorna un diccionario donde la clave es el ID del participante y el valor es True (activo).
    """
    participantes = {}
    for i in range(1, num_participantes + 1):
        participantes[f'{i:03d}'] = True  # ID formateado con 3 dígitos
    return participantes

def eliminar_participantes_aleatorios(participantes, cantidad_a_eliminar):
    """
    Elimina una cantidad aleatoria de participantes activos.
    """
    participantes_activos = [id for id, activo in participantes.items() if activo]
    
    if not participantes_activos:
        print("No quedan participantes activos para eliminar.")
        return

    if cantidad_a_eliminar > len(participantes_activos):
        print(f"Advertencia: Se intentaron eliminar {cantidad_a_eliminar} participantes, pero solo quedan {len(participantes_activos)} activos. Se eliminarán todos los restantes.")
        cantidad_a_eliminar = len(participantes_activos)

    participantes_a_eliminar = random.sample(participantes_activos, cantidad_a_eliminar)
    for id_participante in participantes_a_eliminar:
        participantes[id_participante] = False
    print(f"Se eliminaron {cantidad_a_eliminar} participantes.")

def mostrar_estado_torneo(participantes, columnas):
    """
    Muestra el estado actual de los participantes en formato de tabla.
    """
    print("\n--- Estado Actual del Torneo ---")
    ids_ordenados = sorted(participantes.keys())
    
    for i in range(0, len(ids_ordenados), columnas):
        fila = []
        for j in range(columnas):
            if i + j < len(ids_ordenados):
                id_participante = ids_ordenados[i + j]
                if participantes[id_participante]:
                    fila.append(id_participante)
                else:
                    fila.append('---')
            else:
                fila.append('   ') # Espacios para alinear si la última fila no está completa
        print(' '.join(fila))
    print("------------------------------")

def contar_participantes_activos(participantes):
    """
    Cuenta y retorna el número de participantes activos.
    """
    return sum(1 for activo in participantes.values() if activo)

# --- Flujo del programa principal ---
if __name__ == "__main__":
    print("Iniciando Ejercicio 1: Gestión de Participantes en un Torneo")
    
    # 1. Inicializa un torneo con 100 participantes.
    num_inicial_participantes = 100
    torneo = inicializar_torneo(num_inicial_participantes)
    print(f"Torneo inicializado con {contar_participantes_activos(torneo)} participantes activos.")
    
    # 2. Muestra el estado inicial del torneo.
    mostrar_estado_torneo(torneo, 10)

    # 3. Elimina 20 participantes aleatorios.
    print("\nEliminando 20 participantes...")
    eliminar_participantes_aleatorios(torneo, 20)
    print(f"Participantes activos restantes: {contar_participantes_activos(torneo)}")
    
    # 4. Muestra el estado actualizado.
    mostrar_estado_torneo(torneo, 10)

    # 5. Elimina otros 30 participantes aleatorios.
    print("\nEliminando otros 30 participantes...")
    eliminar_participantes_aleatorios(torneo, 30)
    print(f"Participantes activos restantes: {contar_participantes_activos(torneo)}")
    
    # 6. Muestra el estado actualizado.
    mostrar_estado_torneo(torneo, 10)

    # 7. Intenta eliminar 60 participantes (cuando solo queden 50 activos).
    print("\nIntentando eliminar 60 participantes (quedan 50 activos)...")
    eliminar_participantes_aleatorios(torneo, 60)
    print(f"Participantes activos restantes: {contar_participantes_activos(torneo)}")
    
    # 8. Muestra el estado final y el número de participantes activos restantes.
    mostrar_estado_torneo(torneo, 10)
    print(f"\nFin del Ejercicio 1. Total de participantes activos: {contar_participantes_activos(torneo)}")
