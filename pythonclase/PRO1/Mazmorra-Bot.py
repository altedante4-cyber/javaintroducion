import random 

def atacar(atacante , defensor ):


    #==============CODIGO POR MI ==============

    # # de atacante necesitamos el ataque que tiene para hacir infringir danio en el defensor

    # ataque = int(jugador["ataque"]) # aqui defiinimos el numero de ataque que tiene nuestro jugador 
    # defensor["vida"] = defensor["vida"]  - ataque 

    # if defensor["vida"] < ataque :
    #     print(">> [ATAQUE]  Corte Final ")
    #     print(f">> DAno cuasado: {ataque} . El Orco ha caido ")
    #     print("VICTORIA  HAS DERROTADO AL ORCO Y sobrevivido con 84 de vida ")
    # else:


    # #lo que me esta costando es saber actualisar el valor  
    #     print(f">> [ATAQUE] {atacante["nombre"]} golpea a {defensor["nombre"]}")
    #     print(f">> Dano causado {ataque} Vida restan del {defensor["vida"]}")
    #     print(f">> [TURNO ENEMIGO] EL {defensor["nombre"]} te devuelve el golpe ")
    #     ataque_densor = int(defensor["ataque"])
    #     atacante["vida"] = atacante["vida"] - ataque_densor 
    #     print(f">> Dano recibido {ataque_densor} Vida restan del {atacante["vida"]}")
    #     print()

    #     print(f"JUGADOR: {jugador["nombre"]} [Vida: {atacante["vida"]} |  Pociones: {jugador["pociones"]}")
    #     print(f"ENEMIGO: {enemigo["nombre"]} [Vida: {defensor["vida"]}]")

    
    #     print()

    #=============CODIGIO IA


    #samoas los parametros no las variables globales
    numero = random.randint(0,11) 
    danio = numero
    
    if numero == 10:
        print(">> GOLPE CRITICO DANIO MULTPLICADO")
        danio *= 2 

             
    defensor["vida"] -= danio 

    print(f">> [ATAQUE] {atacante['nombre']}golpea a {defensor['nombre']} por {danio} de dano   ")

    if defensor["vida"] <= 0:
        defensor["vida"] = 0 # para que no salgan numero negativos
        print(f">> !{defensor['nombre']} ha caido")
    else:
        #el enemigo solo devuelve el golpe si sigue vivo
        danio_enemigo = defensor["ataque"]
        atacante["vida"] -= danio_enemigo
        print(f">> [TURNO ENEMIGO] {defensor['nombre']} responde con {danio_enemigo} de dano  ")

        if atacante["vida"] < 0 : atacante["vida"] = 0 


def tienda(entidad):

    #tienda donde el jugador puedo comprar oro si gana la partida # solo si tiene mas de 30


    if entidad["oro"] >= 30 :
        
        comprar= int(input("Desea comprar oro 1.si 2.no "))

        match(comprar):

            case 1 :

                entidad["oro"] += random.randint(20,50)
                print("comprado correctamente")
                print(entidad)
            case 2 :
                print("saliendo ")


    



     


def ganar_oro(entidad):
    #cada vez que el jugador gane un combate (cuadno el enemigo muera) suma un valor aleatorio de oro(entre 20 y 50)
    # a una nuevea clave en el diccionario del jugador llamada "oro"
    valor_aleatorio = random.randint(20,50)

    if esta_vivo(entidad):
        entidad["oro"]  += valor_aleatorio
        print(entidad)

def usar_posicion(entidad):
    
    if (entidad["nombre"] == "Aragorn"):
        #necesitamos incremetar su vida 
        entidad["vida"] += 20 
        entidad["pociones"] -= 1 
    else:
        print("No que da pociones")




def esta_vivo(entidad):

    if (entidad["vida"]) > 0 :
        return True 
    else:
        return False 
    







jugador = {"nombre": "Aragorn", "vida": 100, "ataque": 15, "pociones": 3 , "oro":0}

enemigo = {"nombre": "Orco", "vida": 60, "ataque": 12}



print("!COMIENZA EL COMBATE ")
print("*"*30)


while  esta_vivo(jugador) and esta_vivo(enemigo) :

    

    print("Que quieres hacer ")
    print("1. Atacar ")
    print("2.Curarse ")
    opcion = int(input("Selecciona(1-2) : "))

    match(opcion):
        case 1 :

            atacar(jugador,enemigo)
        case 2:
            usar_posicion(jugador)



if esta_vivo(jugador) :  #con esto lo que quiero decir es que si el jugador2 esta muerto por ley el jugador1 tiene que estar vivo
    ganar_oro(jugador)
    tienda(jugador)
else:
    print("Has sido derrotado ....... GAME OVER")




#================ ESTO ES LA FORMA DE CONVERTIR UN VALUES EN UN ENTERO ES MUY TEDIOSOS HACI QUE NO 
# valor = list(sacar_ataque_jugador.values())[0] #convierte la vista a lista y toma el pirmer elemento 
# valor_entero = int(valor)
# print(valor_entero)
#================= OTRA FORMA DE CONVERTIR A ENTERO DE LA MANERA MAS FACIL 

