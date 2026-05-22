import random

def inicializar_votacion(num_candidatos):
    """
    Inicializa la estructura de datos para la votación.
    Retorna un diccionario donde la clave es el ID del candidato y el valor es un diccionario
    con 'votos' y 'activo'.
    """
    candidatos = {}
    for i in range(1, num_candidatos + 1):
        candidatos[f'C{i:02d}'] = {'votos': 0, 'activo': True}
    return candidatos

def simular_votos(candidatos):
    """
    Asigna un número aleatorio de votos a cada candidato activo.
    """
    print("Simulando votos...")
    for id_candidato, datos in candidatos.items():
        if datos['activo']:
            datos['votos'] = random.randint(1, 100)

def eliminar_candidato_menos_votado(candidatos):
    """
    Identifica y elimina al candidato(s) con el menor número de votos entre los activos.
    """
    candidatos_activos = {id: datos for id, datos in candidatos.items() if datos['activo']}

    if len(candidatos_activos) <= 1:
        return False  # No hay suficientes candidatos para eliminar o ya hay un ganador

    min_votos = float('inf')
    candidatos_con_menos_votos = []

    for id_candidato, datos in candidatos_activos.items():
        if datos['votos'] < min_votos:
            min_votos = datos['votos']
            candidatos_con_menos_votos = [id_candidato]
        elif datos['votos'] == min_votos:
            candidatos_con_menos_votos.append(id_candidato)
    
    # Eliminar uno o todos los empatados con menos votos
    for id_eliminar in candidatos_con_menos_votos:
        candidatos[id_eliminar]['activo'] = False
        print(f"Candidato {id_eliminar} eliminado con {candidatos[id_eliminar]['votos']} votos.")
    
    return True

def mostrar_resultados(candidatos):
    """
    Muestra una tabla con los IDs de los candidatos activos y su número de votos.
    """
    print("\n--- Resultados de la Votación ---")
    print("ID  | Votos | Estado")
    print("----|-------|--------")
    
    ids_ordenados = sorted(candidatos.keys())
    for id_candidato in ids_ordenados:
        datos = candidatos[id_candidato]
        estado = "Activo" if datos['activo'] else "Eliminado"
        print(f"{id_candidato} | {datos['votos']:<5} | {estado}")
    print("--------------------------------")

def contar_candidatos_activos(candidatos):
    """
    Cuenta y retorna el número de candidatos activos.
    """
    return sum(1 for datos in candidatos.values() if datos['activo'])

# --- Flujo del programa principal ---
if __name__ == "__main__":
    print("Iniciando Ejercicio 2: Sistema de Votación Simplificado")
    
    # Inicializa una votación con 5 candidatos.
    num_candidatos_inicial = 5
    votacion = inicializar_votacion(num_candidatos_inicial)
    print(f"Votación inicializada con {contar_candidatos_activos(votacion)} candidatos.")
    
    ronda = 1
    while contar_candidatos_activos(votacion) > 1:
        print(f"\n--- Ronda {ronda} ---")
        simular_votos(votacion)
        mostrar_resultados(votacion)
        
        if not eliminar_candidato_menos_votado(votacion):
            print("No se pudo eliminar a nadie (posiblemente solo queda un candidato o error).")
            break
        ronda += 1

    mostrar_resultados(votacion)
    ganador = [id for id, datos in votacion.items() if datos['activo']]
    if ganador:
        print(f"\n¡El ganador es el candidato {ganador[0]}!")
    else:
        print("No hay un ganador claro (posiblemente todos eliminados o empate final).")
    
    print("\nFin del Ejercicio 2.")
    