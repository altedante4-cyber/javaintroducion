#ficheor tiene que existir por que si no proboca una exepcion  tambien si esta  enotra ruta   dos tipos de ruta relativo  y ruta absolluta           
try:
    #cursor = open("fichero.txt","rt")
    #texto = cursor.read()
    #cursor.close()
   
    #linea = cursor.readline()
    #lee el archivo linea a linea el de abajo comprueba si hay linea 
    #while(linea)

     #   print(linea,end="")
      #  linea = cursor.readline()
    
    #for linea in cursor:
     #   print(linea,end="")

    #leemos todo el fichero
#    lista = cursor.readlines()
 #   print(lista)

    #caracter = cursor.readline(4):
    #while caracter != "":
     #   print(caracter)
      #  caracter = cursor.readline(4)

   

   # cursor.close()
   with open("fichero.txt","rt") as cursor :
        lista = cursor.readlines()
        print(lista)
except:
    print("error")