try:
    with open(input() , "r" , encoding="utf-8") as f:
        entrada = f.readlines()
    direccion = {}

    lista_temp=[]
    for i , j in enumerate(entrada):
        a = j.split(",")[-1]
        lista_temp.append(a)


    for i in lista_temp:
        k = i.split()

        direccion[k[-1]]=direccion.get(k[-1],0)+1

    direcion_ip = []
    lista_conexion = []
    lista_unica = []
    for i in lista_temp:
        k = i.split()

        if k[-1]  not in lista_conexion:
            lista_conexion.append(k[-1])
        

        direcion_ip.append([k[-1],k[0]])

    
    for i in lista_conexion:
        temp = []
        for j in direcion_ip:
            if i == j[0] :
                temp.append(j[1])

        lista_unica.append({
             "clave":i ,
             "valor": [x for x in temp ]
        })

    for i in lista_unica:
        print(i)
        



            
              


except Exception as e :
    print(e)