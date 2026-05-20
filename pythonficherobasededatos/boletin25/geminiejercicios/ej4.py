def validar_producto(archivo1,archivo2):

    try:
        with open(archivo1,"r",encoding="utf-8")as p , open(archivo2,"r",encoding="utf-8") as k :
                 entrada1 = p.readlines()
                 entrada2 = k.readlines()
        dicionario_real = {}
        dicionario_teorico = {}
        a = len(entrada1)
        b = len(entrada2)
        for j , i in enumerate(entrada1,start=1):
              clave , valor = i.split(":")
              if j == a :
                dicionario_real[clave] = valor
              else:
                dicionario_real[clave] = valor[:-1]
        for j , i in enumerate(entrada2,start=1):
              clave , valor = i.split(":")
              if j == b :
                dicionario_teorico[clave] = valor
              else:
                dicionario_teorico[clave] = valor[:-1]
        dicionario_falta = []
        for clave ,valor in dicionario_real.items(): #lo que se ha contado
            
            if clave not in dicionario_teorico:
                dicionario_falta.append(clave)

        
        # ver discrepacias de cantidades 
        productos_que_no_coinciden_cantidad =  []
        for clave , valor in dicionario_real.items():
            for cla , val in dicionario_teorico.items():
                 if clave == cla :
                     if val != valor:
                         
                         productos_que_no_coinciden_cantidad.append([cla,val])

        
        print("-"*50)
        print(f"Productos no coincidentes {"".join(dicionario_falta)}")                 
        print(f"Productos no coincide con la cantidad \n{"\n".join(" ".join(x)for x in productos_que_no_coinciden_cantidad)}")
                
               
        
        



    
    except Exception as e :
        print(e)


validar_producto("stock_real.txt","stock_teorico.txt")