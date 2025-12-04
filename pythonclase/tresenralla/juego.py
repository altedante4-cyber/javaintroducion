import random 


tablero = [[x for x in range(0,4)] for x in range(3)]

posiciones_validas = ['1','2','3','4','5','6','7','8','9']



turno = 'X'
numJugador = 1 

contador = 0

while contador <= 9 :



        posicion  = int(input(f"ingrese la posicion str{numJugador} {turno}"))
        if numJugador == 1 :
            turno = "o"
            numJugador = 2
        else:

            turno = 'X'
            numJugador = 1 
        for i in range(len(tablero)):

            if posicion not in posiciones_validas:

                print("posicion invalida")

            if posicion == 1 and turno == 'X':

                tablero[0][0] = 'x'

            elif posicion == 2 and turno == 'X':

                tablero[0][1] = 'x'
            elif posicion == 3 and turno == 'X':

                tablero[0][2] = 'x'
        
            elif posicion == 4 and turno == 'X':

                tablero[0][3] = 'x'

            elif posicion == 5 and turno == 'X':

                tablero[1][0] = 'x'






        for fila in tablero:

            print(fila)    



        contador += 1 



