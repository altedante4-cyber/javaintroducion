import re 





texto = input("Introduce texto ")


#Contar caracteres totales (con y sin epacios ) palabras y oraciones (separados por . ! ? ) primero hay que serpar por esto

separar = re.split(r'[.?!]',texto)
diccionario_separar ={ i : len(i) for i in separar }
#calcular la longitud media de las palabaras y la longitud media de las oraciones => la longitud media de las palabras es el total letras / total de palabras
longitud_media_palabras = sum([ values for calve , values in diccionario_separar.items()]) / len(diccionario_separar)

lista_dic = []
contador_de_oraciones = 0 
for i in diccionario_separar.keys():
    if len(i) > 1 :
       lista_dic.append( i.split(" ")) #devuelve una lista
       contador_de_oraciones +=  1  
    else :
        lista_dic.append(i)

#limpio la lista
for i in range(len(lista_dic)):
    lista_dic[i] = [x for x in lista_dic[i] if x != '']

dicionario_lista_palabras = {}

for i in lista_dic:

    dicionario_lista_palabras[len(i)] = i
        
longitud_media_oraciones = sum([ x for x in dicionario_lista_palabras.keys() ]) / contador_de_oraciones



# la longitud media de oraciones se calcula de la siguiente manera  total palabras  / total de oracioens ejemplo hola mundo => esto es una oracion de 2 palabras como estas hoy tiene 3 palabras
#encontarra las 3 palabras mas largas del texto (sin repetir )

#primero encontramos el maximo  luego vamos iteradon sobre una lista  teniendo como refferencia el maximo el primero que se menro que el maximo es el penultimo y luego hacemos 
# lo mismo con el penultimo el primero que sea menor que el penultimo es antepenultimo ya tenemos las ter palabras 

for lista_palabras in dicionario_lista_palabras.values():
    lista_cam = []

    for palabra in lista_palabras:
        if palabra not in [x[0] for x in lista_cam ]: #evita duplicados
            lista_cam.append([palabra,len(palabra)])

    #encontrar la palabra mas larga 

    max1 = max(lista_cam , key=lambda x: x[1])
    #encontar la sgunda mas larga (primera que sea menor que el maximo )
    max2 = next( (x for x in  lista_cam if x[1] < max1[1]),None)
    #encontrar la tercera mas larga(primera que sea menor que el segundo )
    max3 = next( (x for x in  lista_cam if x[1] < max2[1]),None)

    print("Tres palabras más largas: ")
    print(max1[0] if max1 else None,
          max2[0] if max2 else None,
        max3[0] if max3 else None)

    #explicacion

    #1.lista_cam => lista de sublistas [palabra , longitud ]
    #max(lista_cam , key=lambda x: x[1]) obtiene la palabra con mayor longitud
    #next(x for x in lista_cam ifx[1] < max1[1]) obtiene la primera palabra que sea mas corta que la anteriro 
    # [x[0] for x in lista_cam] sirve para eivtar dupliados de plaabra no de longitud 
    
    #uso del next se usa par tomar el siguietne elemento de un iterados

    #numeros = iter([10,20,30])
    #print(next(numeros)) # imprimer 10
    #print(next(numeros))# imprimer 20
    #prnit(next(numeros)) # imprime 30 
    # uso comun ocn expresiones generadoras

    #supongamos que quieres el pirmer numero par en una lista
    # numeros = [1,3,4,6,7]
    #primero_par = next(x for x in numeros if x % 2 == 0 )
    #print(primero_par)



