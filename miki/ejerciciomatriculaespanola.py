def validarmatricula(matricula:str)->bool:

    # no puede contener espacios
    # no puede tener mas de una longitud de 7
    # no puede tener vocales o  ENie o Q


    #si puede  estar separado por un guion  o no tener espacio tambien es valido
    no_permitido = "ñqaeiou"
    if " " in matricula:
        return False

    if "-" in matricula:
        matricula = matricula.replace("-","")

    if len(matricula) != 7:
        return False

    # Primeros 4 dígitos
    cuatro_digitos = matricula[:4].isdigit()

    # Últimas 3 letras
    tres_alpha = matricula[4:].isalpha()

    if not cuatro_digitos or not tres_alpha:
        return False
 # No puede contener vocales, ñ o q
    for c in matricula[4:]: # de la posicion 4 para adelante ver si las letras contineen esas palabras
        if c.lower() in no_permitido:
            return False

    return True

def mostrarmatriculasvalidas(*matricula:str):

    for i in matricula:
        if validarmatricula(i):
            print(i)
        else:
            print("invalida")



mostrarmatriculasvalidas("22CDR","7521-MXP","1224MN")





