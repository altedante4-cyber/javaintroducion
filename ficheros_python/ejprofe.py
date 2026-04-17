abrir_archivo = open("profesores.txt","rt")

alumnos=[]
profesor=[]

for linea in abrir_archivo:
    #sacamos el invalido 
    valido =True 

    elemento = linea.split(":")
  
    if len(elemento) != 2:
        valido =False
    if elemento[0].lower() != "profesor" or elemento[0] != "alumno":
        valido = False


    if valido:
        if elemento[0].lower() == "alumno" :
            alumnos.append([elemento[0],elemento[1].replace("\n","")])
        else:
            profesor.append([elemento[0],elemento[0].replace("\n","")])



print(alumnos)
print(profesor)