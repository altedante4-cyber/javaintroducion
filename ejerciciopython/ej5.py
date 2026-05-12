def cifrado(nombre_archivo,clave):

    with open(nombre_archivo,"r",encoding="utf-8") as f:
        entrada = f.readlines()


<<<<<<< HEAD
    a = entrada[0].splitlines()

    
    caracter = []    
    for j in a:
        for numero , k in enumerate(j):
            print(numero)
=======
>>>>>>> 5608d6a (subiendo cambios)
                

cifrado("lecturas.txt",2)
