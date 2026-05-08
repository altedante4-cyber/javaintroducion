try:
    with open("fichero8.txt" , "r" , encoding="utf-8") as f:

        entrada= f.readlines()

    lista_bolean = []
    num = 0
    for i in entrada:

        a = i.splitlines()
        
        encontrado = True 

        for j in a:

            if ";" in j :
                lineas = j.split(";")

                nombre , apellido = lineas[0].split(",")

                valido = all([ x for x in nombre.isalpha() ])
                print(valido)
                

except :
    print("Error en la lectura ")