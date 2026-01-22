

estudiantes = []


for _ in range(int(input())):
        name = input()
        score = float(input())

        estudiantes.append([name,score])



#obtenemos la calificacion

estudiantes.sort(key=lambda x: x[1])


#encontrar la segunda calificacion mas baja

minima_calificaion = estudiantes[0][1]

segunda_calificacion = None


for nombre , calif in estudiantes:
        
        if calif > minima_calificaion:

            segunda_calificacion = minima_calificaion

            break
        

#si todos tienen la misma califciacion, tomar la siguiente

if segunda_calificacion is None :
        segunda_calificacion = minima_calificaion


#recolectar y    ordenar nombres

nombres_segundos = []

for nombre,calif in estudiantes:
    if calif == segunda_calificacion:
        nombres_segundos.append(nombre)


# ordenar alfabeticamente e imprimir

nombres_segundos.sort()

for nombre in nombres_segundos :
      print(nombre)

      
