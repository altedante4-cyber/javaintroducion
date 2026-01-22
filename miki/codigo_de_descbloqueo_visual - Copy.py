def codigo_desbloqueo(codigo):

        #convertimos a una lista de string los eneteors

        NXTX = list(str(codigo))

        #le agremgamos a una lista de enteros para poder iterar sobre el

        codigo_entero = [] #esto es una lista de neteros
        for i in range(len(NXTX)):
                codigo_entero.append(NXTX[int(i)]) #le especificamos que esa lista lo queremos de enteros


        for i in range(4):
            for j in range(10):
                print('.' , end = '')
                if i == 0 and j == int(codigo_entero[0])-1 :
                    print('#' , end = '')
                elif i == 1 and j == int(codigo_entero[1])-1 :
                    print('#' , end = '')
                elif i == 2 and j == int(codigo_entero[2])-1 :
                    print('#' , end = '')
                elif i == 3 and j == int(codigo_entero[3])-1 :
                    print('#' , end = '')



            print()









print(codigo_desbloqueo(3157))