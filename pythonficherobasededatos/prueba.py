tablero =[[x for x in range(3)] for i in range(3)]

cont = 0 

for i in range(len(tablero)):
    print("---------------")

    for j in range(len(tablero)):
        
        print(tablero[i][j] , "|" , end="")
        cont += 1
    
    if cont == 3 :
        print()
        cont=0