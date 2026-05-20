tablero =[[x for x in range(3)] for i in range(3)]

def colocar(pos,jugador):
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            
            match pos :
                case  1 :
                          tablero[0][0] = "x" if jugador else "o"
                case  2 :
                          tablero[0][1] = "x" if jugador else "o"

                case 3 : 
                        tablero [0][2] = "x" if jugador else "o"
                
                case 4 :
                        tablero[1][0] = "x" if jugador else "o"

                case 5 : 
                        tablero [1][1] = "x" if jugador else "o"

                case 6 :
                        tablero[1][2] = "x" if jugador else "o"
                
                case 7 : 
                        tablero[2][0] = "x" if jugador else "o"
                case 8 :
                        tablero[2][1]="x"  if jugador else "o"
                case 9:
                        tablero[2][2] ="x" if jugador else "o"
                
                 
def mostrar_tablero():
    cont = 0 

    for i in range(len(tablero)):
        print("---------------")

        for j in range(len(tablero)):
        
            print(tablero[i][j] , "|" , end="")
            cont += 1
    
        if cont == 3 :
            print()
            cont=0


try:
    with open("tablero.txt","w",encoding="utf-8") as f:

        ganado = True
        jugador = True 
        while ganado:
            user = int(input("Introuduce la posicion "))
            colocar(user,jugador)
            if jugador:
                  jugador = False
            else:
                  jugador = True 
            mostrar_tablero()

        for j in tablero:
              f.write(str(j))

            






except Exception  as e :
    print(e)