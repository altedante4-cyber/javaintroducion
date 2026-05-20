try :

    with open("soluciones.txt" , "r" , encoding="utf-8") as f:
        solution = f.readlines()
         

        
except Exception :
     print("Error en el fichero de soluciones ")


try:
    with open("respuestas.txt" , "r" , encoding="utf-8") as e :

        respu = e.readlines()

        limpiar = [x.replace("\n" , "").strip() for  x in respu if x.strip()]
        alumno={}

        for j in limpiar:
            a , b = j.split(":")
            
            alumno[a]=b


        lista_soluciones= [x for x in solution]
        lista_sin=lista_soluciones[0]
        separado = [x.strip() for x in lista_sin.split(",")]
        agregados = []
        for clave , valor in alumno.items():
              a = [x.strip() for x in valor.split(",")]
              suma = 0
              cont = 0  
              for j , k in zip(a,separado):

                      if cont != 10 and j == k :
                           suma += 1
                      else:
                            suma -= 0.3
                     
                      cont += 1

              agregados.append({
                    "nombre":clave ,
                    "suma" : suma                            
                  })

              
        for i in agregados:
             print(f"{i["nombre"]}:{i["suma"]}")

except Exception as e:
    print(e)