import random

def generar_jugadores():
    
    lista_jugadores = []

    for i in range(1,456):
        lista_jugadores.append(i)


    lista_jugadores_diccionario = {}


    for i in lista_jugadores:
        vivo = "Vivo" 
        lista_jugadores_diccionario[i] = vivo 


    return lista_jugadores_diccionario

#la funcion random.sample() es una funcion del modulo estandar random de python
# sirve para selecionar elementos aleatroios sin repetir de una secuencia 

# en que consiste 
# la funcion tiene esta forma basicca

#random.sample(poblacion, k )
# poblcaicion => lista , tupla,cadena o cualquier secuencia
# k => cantidad de elemtos que quieres selecionar
# devuelve una lista nuva con k elementos elegidos sin reemplazo no se reptien 

# tomar el 30 %
#  import random 
# lista = [1,2,3,4,5]
# porcentaje = 0.30
# k = int(len(lista) * porcentaje )

def jugar_ronda(diccionario_jugadores:dict ):


    #1.filtramos quienes estan vivor ahora misimo

    vivos_actuales = [ num for num , estado in diccionario_jugadores.items() if estado == "Vivo" ]

    #2.Calculamos el 50 % de los que quedan vivos

    k = len(vivos_actuales) // 2 

     #3.si queda mas de uno , elegimos a los que van a moriri

    if k > 0 :

        victimas = random.sample(vivos_actuales,k)
        for num in victimas:
            diccionario_jugadores[num] = "Eliminado"
        
    
    return diccionario_jugadores





def obtener_supervivientes(diccionario_jugadores):

    #que recorra el didccionario y guarde en una lista solo los numeros de los jugadores que siguen
    lista_vivor = [  clave  for clave , valor in diccionario_jugadores.items() if valor != "Eliminado" ]

    return lista_vivor


jugadores = generar_jugadores()

 # que esta pasando aqui en python cuando pasa un diccionario a un a funcion y lo modificas el diccionari
    # original cambia tu funcio n jugar_ronda devuelve el dicionario completo (con los vivods y los elimiadnos por len(guaradar )) siepre va impirmir 455 por que el didicioanri o sigue
    # 455 porque el didionario sigue teniedno 455 llave solo que algunas dicen eliminado y otras vivo
     # para que el juego funcion en cada ronda solo debes intenetar eliminar a los que todavia estar vivor no alos que ya muerieron

     #ERRO EN JUGAR ROND

     #ACTUALMENTA HACEE STO

     #MUESTRO = random.sample(list(diccioniario_jugador.key()),k)
     #problema esats eligiendo victimas de todo la lista inicial 
     # si el jugador 5 ya estaba eliminado tu codigo odria voler a elegirlo para  eliminarlo esto hara que el juego nunca terminen
     # o  que el numero de muertos  sea incorrecto
     # la solucin (codigo corregedio)
     #debes filtra quiernees estan  vivor antes de pedir la muestra aleatroia aqui tienes como deberia
     #quedar tu logica para queel while funciones
    


while len(obtener_supervivientes(jugadores)) > 1 :

    jugar_ronda(jugadores)

    #ahora si contamos cuantos quedan vivos de verdad

    quedan_vivos = obtener_supervivientes(jugadores)
    print(f"Ronda terminada Jugadores restantes {len(quedan_vivos)}")


# al salir del bucle el que quede en la lista es el ganador

ganador = obtener_supervivientes(jugadores)
print(f"El ganador es el jugador numero {ganador[0]}")

