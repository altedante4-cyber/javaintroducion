def validar_punto(palabra:str):

    es_punto = len(palabra.split(".")) > 1 

    if es_punto:
        return True
    
    return False





palabras = input("Introduce el texto  ")



if not validar_punto(palabras):

    #guardar los valores del split en un array

    array_split = palabras.split(" ")

    array_palabras = []

    

    print(array_palabras)

        

        



else:

    print("tiene punto ")