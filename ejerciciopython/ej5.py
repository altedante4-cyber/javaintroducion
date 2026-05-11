def cifrado(nombre_archivo,clave):

    with open(nombre_archivo,"r",encoding="utf-8") as f:
        entrada = f.readlines()


    a = entrada[0].splitlines()

    
    caracter = []    
    for j in a:
        for numero , k in enumerate(j):
            print(numero)
                

cifrado("lecturas.txt",2)
