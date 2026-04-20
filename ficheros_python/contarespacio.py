cursor = open("fichero.txt","rt")

cont = 0 
for linea in cursor:
     print(linea[0])
     