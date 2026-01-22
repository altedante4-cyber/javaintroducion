import random

def validarganador(usuario:str,ordenador:str)->bool:

    gana_usuario = False
    gana_maquina = False
    empate = False


    if usuario == ordenador:
        empate = True
    elif usuario == "tijera" and ordenador == "papel":
        gana_usuario = True
    elif usuario == "tijera" and ordenador == "piedra":
        gana_maquina = True
    elif usuario == "piedra" and ordenador == "tijera":
        gana_usuario = True
    elif usuario == "piedra" and ordenador == "papel":
        gana_maquina = True
    elif usuario == "papel"  and ordenador == "piedra":
        gana_usuario = True
    elif usuario == "papel" and ordenador == "tijera":
        gana_maquina = True


    return gana_usuario , gana_maquina , empate

ganado = False
lista_jugo = ["piedra", "papel", "tijera"]

partidas = 3

contador_puntos_usuario = 0
contador_puntos_maquina = 0
while partidas > 0:
        opcion = input("Ingrese piedra , papel , tijera").strip().lower()
        elegir_palabra_ordenador = random.choice(lista_jugo)


        if opcion not in lista_jugo:
            print("Error ingrese un formato valido ")
            continue




        es_ganado_user  , es_ganador_maquina , es_empate = validarganador(opcion,elegir_palabra_ordenador)
        print(opcion)
        print(elegir_palabra_ordenador)

        if es_ganado_user:
            print("gana usuario")
            contador_puntos_usuario += 1
        elif es_ganador_maquina:
            print("gana maquina")
            contador_puntos_maquina += 1
        elif es_empate:
            print("empate")
        else:
            print("error")

        partidas -= 1


if contador_puntos_usuario > contador_puntos_maquina:
    print("Partida terminada y gana el usuario")
elif contador_puntos_usuario < contador_puntos_maquina:
    print("Partida terminada y gana el maquina")
else:
    print("Termino en empate tecnico ")







