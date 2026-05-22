#inicialisa los datos de tu lista o de tu diccionario 
import random 
def inicializaJuego(jugadores,numJugadores):
    
    for i in range(numJugadores):
        jugadores[i]= True 

#elimina 150 jugadores al azar

def numJugadoresActivos(jugadores):

    return sum( x for x in jugadores.values() if x  )


def eliminarJugadores(jugadores,numJugadoresEliminar):
    lista_activos = [x  for x in jugadores.values() if x ]
    #validar si numjugadore es mayor a jugadores activos salir

    if len(lista_activos) < numJugadoresEliminar:
        print(f"!No puedo eliminar a {numJugadoresEliminar} ahora mismo quedan {len(lista_activos)} activos nos quedamos sin ganador")
        return
    
    jugadores_activos = [ x   for x , valor  in jugadores.items() if valor ]
    eliminar_aleatorio = random.sample(jugadores_activos , k=numJugadoresEliminar)
    for i in eliminar_aleatorio:
        jugadores[i] = False

    if len(lista_activos) - len(eliminar_aleatorio) == 1 :
        print(f"Vamos a eliminar a {numJugadoresEliminar} jugadores")
        print(f"Queda un solo jugador activo !Ya tenemos ganador ")
    else:
        print(f"Vamos a elmimnar a {numJugadoresEliminar} jugadores ")
        print(f"Quedan {len(lista_activos) - len(eliminar_aleatorio)} activos ")


    
    
    #seran elegidor al azar
     
def verJugadores(jugadores,columnas):
    cont = 0 
    for clave ,valor in jugadores.items():

        if  cont % columnas == 0 :
            print()

        if valor :
            print(f"{clave:03} ",end="")
        else:
            print("___",end=" ")

        cont += 1

        



jugadores = {}
numJugadores = 456
columnas = 12

inicializaJuego(jugadores,numJugadores)
eliminarJugadores(jugadores,12)
verJugadores(jugadores,12)

activos = numJugadoresActivos(jugadores)
print("\nJUgadores activos: ",activos )