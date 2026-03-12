import random 
def  inicializaJuego(jugadores,columnas):
    print("-"*50)
    print("Jugadores activos : 256 ")
    print("-"*50)

    if not jugadores:
        jugadores.update({i: True for i in range(1, 456 + 1)})
    
    contador = 0

    for clave , valor  in jugadores.items():

        if valor:
            print(f"{clave:03d}", end = " ")
        else:
            print(f"---", end = " ")

        contador += 1 

        if contador % columnas == 0 :
            print() 





def elminarJugadores(jugadores,num_eliminar):
    
    list_clave = [clave for clave in jugadores.keys()]

   
    

    a = random.sample(list_clave,num_eliminar)    
    for clave in a:
        jugadores[clave] = False


    jugadores_activos = [clave for clave ,valor in jugadores.items()  if valor ]
    if num_eliminar > len(jugadores_activos): print(f"No puedo  eliminar a {num_eliminar} jugadores Ahora mismo quedan 106 activos !Nos quedamos sin ganador")
    if len(jugadores_activos) == 1 : print("Vamos a eliminar a {num_eliminar}. \n Queda un solo jugador activo  Ya tenemos ganador")
   
    print(f"Vamos a eliminar a {num_eliminar} jugadores")
    print(f"Quedan {len(jugadores_activos)} jugadores activos ")
    
jugadores = {}
numJugadores = 456
columnas = 12 

inicializaJuego(jugadores,12)

elminarJugadores(jugadores,444)
inicializaJuego(jugadores,12)



