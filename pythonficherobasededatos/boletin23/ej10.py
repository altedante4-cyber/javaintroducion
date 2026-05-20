def analisis(fichero):
    cont_inva = 0
    lista_n =[] 
    suma =0
    try:
        with open(fichero , "r" , encoding="utf-8") as f :
            for i in f:
                a = i.strip().split()

                try:
                       k = [ float(x) for x in a ]

                       for  p in k :
                            suma += p 
                            lista_n.append(p)
                     

                except Exception:
                     cont_inva += 1


        print(f"Numero de datos validos {len(lista_n)}")
        print(f"NUmero de datos invalidos {cont_inva}")
        print(f"Minimo: {min(lista_n)}")
        print(f"Maximo :{max(lista_n)}")
        print(f"Media aritmetica: {suma / len(lista_n)}")
    
    except Exception as p:
            print("Ocurrio un error a leer el documento ")


analisis("fichero10.txt")
