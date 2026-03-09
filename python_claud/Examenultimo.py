import random
def inicializaJuego(jugadores, numJugadores):
    """Inicializa el diccionario de jugadores"""
    for i in range(1, numJugadores + 1):
        jugadores[i] = True
def numJugadoresActivos(jugadores):
    """Devuelve el número de jugadores activos"""
    return sum(1 for v in jugadores.values() if v)
def eliminarJugadores(jugadores, num):
    """Elimina jugadores al azar"""
    activos = numJugadoresActivos(jugadores)
    
    if activos == 1:
        print("¡Ya tenemos un ganador! No se pueden eliminar más jugadores.")
        return
    
    if num > activos:
        print(f"¡No puedo eliminar a {num} jugadores! Ahora mismo quedan {activos} activos. ¡Nos quedamos sin ganador!")
        return
    
    print(f"Vamos a eliminar a {num} jugadores.")
    
    if activos - num == 1:
        print("Queda un solo jugador activo. ¡Ya tenemos ganador!")
    elif activos - num == 0:
        print("¡No puedo eliminar a todos los jugadores! Necesitamos un ganador.")
        return
    else:
        print(f"Quedan {activos - num} jugadores activos")
    
    activos_list = [k for k, v in jugadores.items() if v]
    eliminar = random.sample(activos_list, num)
    
    for jugador in eliminar:
        jugadores[jugador] = False
def verJugadores(jugadores, columnas):
    """Muestra el tablero de jugadores"""
    activos = numJugadoresActivos(jugadores)
    print("-" * columnas * 7)
    print(f"Jugadores activos: {activos}")
    print("-" * columnas * 7)
    
    num = 1
    for clave in sorted(jugadores.keys()):
        if jugadores[clave]:
            print(f"{clave:03d}", end=" ")
        else:
            print("---", end=" ")
        num += 1
        if num > columnas:
            print()
            num = 1
    print()
    print("-" * columnas * 7)
# se valorará mas si lo haces con un diccionario
jugadores = {}
# pero si te sientes mas seguro puedes hacerlo con una lista
#jugadores=[]
# número de jugadores
numJugadores = 456
# columnas del tablero de jugadores
columnas = 12
# inicializa los datos de tu lista o de tu diccionario
inicializaJuego(jugadores, numJugadores)
# muestra el tablero con los jugadores en consola deberían de aparecer los 456
verJugadores(jugadores, columnas)
# elimina 150 jugadores al azar
eliminarJugadores(jugadores, 200)
# mostramos de nuevo el tablero. ahora ya hay jugadores eliminados
verJugadores(jugadores, columnas)
# elimina otros 200 jugadores al azar
eliminarJugadores(jugadores, 150)
# trata de eliminar otros 200 jugadores al azar, pero no puede porque no quedan
eliminarJugadores(jugadores, 200)
#elimina 105 jugadores. Ya sólo queda 1. Tenemos ganador
eliminarJugadores(jugadores, 105)
# muestra por última vez el tablero de jugadores. Sóm può quedar uno
verJugadores(jugadores, columnas)