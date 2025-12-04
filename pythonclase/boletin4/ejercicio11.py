frase = input("introduce una frase")


fraseNueva = ""



for posicion in range(0,len(frase)):
    if posicion != len(frase) - 1 :
        if frase[posicion] == " " or frase[posicion + 1 ] == " ":

            fraseNueva =fraseNueva + frase[posicion]
        else:

            fraseNueva = fraseNueva + frase[posicion] + '-'

    else:
        
        fraseNueva =fraseNueva + frase[posicion]



print(fraseNueva)


