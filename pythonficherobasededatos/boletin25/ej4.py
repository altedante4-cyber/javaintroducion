def invertir(fichero , fichero_escribir):

    try:
        with open(fichero,"r" , encoding="utf-8") as f:

            guardar = f.readlines()

        i = len(guardar) -1
    
        lista_invertida=[]
        while i >= 0 :
        
            a = guardar[i]
            lista_invertida.append(a[::-1])

            i -= 1

        try:
            with open(fichero_escribir,"w",encoding="utf-8") as  escribir:

                    escribir.write("".join(lista_invertida))
        except Exception:
                print("Ocurrio un error en la escritura")
    except Exception:
        print("Ocurrio un error inesperado ")




invertir("fichero1.txt","fichero2.txt")
