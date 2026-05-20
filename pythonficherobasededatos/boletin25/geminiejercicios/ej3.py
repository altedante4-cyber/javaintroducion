
try:
    with open("codigo_ejemplo.py","r",encoding="utf-8") as p :
            entrada = p.readlines()

    lista_comp = []
    for j in entrada:
         a = j.splitlines()
         for k in a:
              if k.startswith("#"):
                   a.remove(k)
              lista_comp.append(a)


    lista_final = []
    for p in lista_comp:
         for j in p:
              if "#" not  in j :
                  lista_final.append(j)
              else:
                   e = j.split("#")

                   lista_final.append(e[0])
    
    try:
         with open("codigo_nuevo.py","w",encoding="utf-8") as p :
            for k in lista_final:
                 p.write(f"{k}\n")


    except Exception :
         print("no sepuedo escribir ")


                   


                   



              
         
                
except Exception as e:
    print(e)