def validar_matricula_moto(matricula : str ):

    letras_no_validas = ['Ñ','Q','A','E','I','O','U']

    tiene_guion = False
    tiene_espacio = False
    if matricula.count('-') != 2 and not tiene_espacio :
        tiene_guion = True
        return False
    elif matricula.count(' ') != 2 and not tiene_guion :
        tiene_espacio = True
        return False


    if len(matricula) != 9 or tiene_guion or not tiene_espacio :
        return False

    #validar patron :
    matricula_split = matricula.split('-')
    for i in range(len(matricula_split)):
         a = matricula_split[0]
         b = matricula_split[1]
         c = matricula_split[2]

    if not a.isalpha() and b.isdigit() and c.isalpha():
        return False

    if matricula in letras_no_validas:
        return False
    else:
        return True




  elif len(matricula) != 9 or not tiene_guion or  tiene_espacio :
        return False

        #validar patron :
        matricula_split = matricula.split('-')
    for i in range(len(matricula_split)):
         a = matricula_split[0]
         b = matricula_split[1]
         c = matricula_split[2]

    if not a.isalpha() and b.isdigit() and c.isalpha():
        return False

    if matricula in letras_no_validas:
        return False
    else:
        return True



print(validar_matricula_moto("AB-123-CD"))