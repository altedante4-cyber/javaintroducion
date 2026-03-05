def contar_palabras(texto_str):

    #1.limpiesa y preparacion

    palabras = texto_str.lower().split()


    #2.conteo eficiente usando un diccionario

    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra]= frecuencia.get(palabra,0) + 1 

    
    #3.ordenar por valor(frecuencia ) de mayor a menor
    #usamos la pista: sorted devuelve una lista de tuplas

    ordenado = sorted(frecuencia.items() , key=lambda x: x[1] , reverse=True )

    #calculos finales
    total_palabras = len(palabras)
    unicas = len(frecuencia) #cantidad de llaves distintas
    
    #5mostrar resultados

    print("\n ----Resultados- ---  ")
    print(f"Total paalbras: {total_palabras} | Unicas: {unicas}")


    print("\n Top 5 palabras mas repetida ")

    #tomamos solo los primeros 5 elementos de la lista ordenada

    for palabra , cuenta in ordenado[:5]:
        print(f"{palabra} : {cuenta}")

#Ejecucion

entrada = input("Escribe una frase o parrafo: ")
contar_palabras(entrada)

#CONCEPTOS A TENER ENCUENTA = =======================

#Frecuencia.get(palabra,0) + 1  esta es la forma pro de llenar diccionarios si la palabra no existe devuelve 0 y le suma 1 al valor actual es muchas mas rapido que count
#ordenador[:5]: => usamos slicing de listas para obtener unicamente lso 5 primeros puestos del ranking
#len(frecuencia) esto nos da el numero de palabras diferente que se encontraron en el texto 

#Estructura de datos
# si quieres ignorar signos de puntuacion (puntos,comsas) podrias anadir un replace (".", "").replace(",","") antes del split