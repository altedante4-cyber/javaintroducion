def matricula(matricula):

    letras_no_validas = ['Ñ','n',"Q","q","A","a","E","e","I","i","O","o","U","u"]

    contador_numeros = 0
    contador_letras = 0
    contador_espacio = 0
    contador_caracteres_guion = 0
    letras_cadenas = []

    # for para contar cuántos números, letras, espacios y guiones hay
    for i in matricula:

        if i.isnumeric():
            contador_numeros += 1

        elif i.isalpha():
            contador_letras += 1
        elif i.isspace():
            contador_espacio += 1

        elif i == '-':
            contador_caracteres_guion += 1



    for i in matricula:
        if i.isalpha():
            letras_cadenas.append(i)

    tiene_letra_validas = True
    for j in letras_cadenas:
        if j in letras_no_validas:  # si la letra está prohibida
            tiene_letra_validas = False  # marca como no válida
            break  # rompe el bucle, no hace falta seguir revisando

    # Caso de que no contenga espacio ni guion
    if contador_espacio == 0 and contador_caracteres_guion == 0 and tiene_letra_validas and contador_numeros == 4 and contador_letras == 3:
            return True
    elif  contador_espacio == 1 and contador_caracteres_guion == 0 and tiene_letra_validas and contador_numeros == 4 and contador_letras == 3:
            return True
    elif  contador_espacio == 0 and contador_caracteres_guion == 1 and tiene_letra_validas and contador_numeros == 4 and contador_letras == 3:
            return True
    else:
        return False

def matriculasValidas(*args):
    matriculas_validas = 0
    matricula_no_validas = 0
    for i in args:
        if matricula(i):
            print(f"{i} es valida")
            matriculas_validas += 1
        else:
            print(f"{i} no valida")
            matricula_no_validas += 1
    print()
    print(f"Matriculas validas: {matriculas_validas}")
    print(f"Matriculas no validas : {matricula_no_validas}")



matriculasValidas("22CDR", "7521-MXP" , "1224MN")
print()
matriculasValidas("5432 – BCF", "3456BAC")

matriculasValidas("ABC-1234")