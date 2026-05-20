def fibonaci(num):

    if num < 2 :
         print("No se puede ")
         return
    if type(num) != int :
         print("no es entero ")
         return 
    
    lista = []

    lista.append(0)
    lista.append(1)
    for i in range(num):

        a = 0 
        b = 1
        c = ""
        for j in range(i):
            c = a + b 
            a = b
            b = c
    
        if c != "":
            lista.append(c)


    try:
        with open("fibonacci.txt","w", encoding="utf-8") as f :
             
            i = 0 
            lista_temp=[]
            while i < num:
                  a = lista[i]
                  lista_temp.append(str(a))
                  i += 1

            f.write(",".join(lista_temp))
    except FileNotFoundError:
            print("El archivo no se encontro")
    
    except Exception:
            print("hubo problemas con el archivo ")


user = int(input("Ingrese el numero de fibonaci"))
fibonaci(user)




