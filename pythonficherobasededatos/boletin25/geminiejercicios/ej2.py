def leerarchivo(nombre):
    valores_finales=[]
    try:
        with open(nombre,"r",encoding="utf-8") as f :
            entrada = f.readlines()

        for j , i in enumerate(entrada):
             a = i.split(",")
             try:
                 convertir = float(a[1]) * 1.10 
                 a[1] = str(convertir)
             except :
                 print("No es un numero ")

             valores_finales.append(a)

    except Exception as e :
        print(e)


    try:
        with open("informe_dolares.csv","w",encoding="utf-8") as k :
                k.write("".join(",".join(x)for x in valores_finales))
    except Exception as p :
                 print(p)
leerarchivo("transacciones.csv")