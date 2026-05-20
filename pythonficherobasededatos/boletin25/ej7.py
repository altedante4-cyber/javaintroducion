def validar_solo_letras(t):

    for i in t:
        if type(i) != str:
            return False
    
    return True 

def validar_puesto_trabajo(t):

    for j in t:

        if j.isalpha():
            return True
    
    return False 
def validar_salario(salario):

    try:
        convertir = float(salario)
        return True
    
    except:
           return False 

try:
    with open("origen.txt","r",encoding="utf-8") as f:
        entrada = f.readlines()

    valido = [] 
    for i in entrada:
        a = i.splitlines()
        
        for j in a:
            
            a = j.count(";")

            if a >= 2:
                valido.append(j)


    lista_temp_validas = []
    for i in valido:

        a = i.split(";")

        nombre , apellido = a[0].split(",")
        puesto_trabajo = a[1].strip()
        salario_mensual = a[2]

      

        if validar_solo_letras(nombre) and validar_solo_letras(apellido) and  validar_puesto_trabajo(puesto_trabajo) and  validar_salario(salario_mensual):
            lista_temp_validas.append(i)


    lista_agregar= []
    for i in lista_temp_validas:
        a = i.split(";")
        nombre , apellido = a[0].split(",")
        try:

            num = int(input(f"{nombre}{apellido}¿Cual es su edad ? "))
            
            if num >= 18 and num <= 67:
                nuevo = f"{i};{num}"

                lista_agregar.append(nuevo)
            else:
                 raise ValueError("Menor de edad ")   
        except ValueError as e :
            if str(e) == "Menor de edad ":
                 print("Error es menor de edad")
            else:
                print("Error: Ingrese un numero por favor ")
         
        try:
             with open("origen.txt","w",encoding="utf-8")as p :
                p.write("\n".join(lista_agregar))
        except:
             print("error ")

    try:
            with open("ficherovalido.txt","w",encoding="utf-8") as f:

                 f.write("\n".join(lista_temp_validas))

    except :
                print("No se puedo escribir en el fichero ")
        


                
        
    

        
    

except :
    print("Error")