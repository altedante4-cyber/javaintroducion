
def nuevoCliente(nombre_dicionario:dict , apellido_persona:str , nombre_persona:str , edad:int ):
    encontrado = False 
    for clave , valor in nombre_dicionario.items():

            apellido , nombre = clave.split(",")

            if apellido == apellido_persona and nombre_persona == nombre  :
                    encontrado = True
                    break

    if encontrado:
        repuesta = int(input("quiere sobreescribir la edad 1:si o 2:no "))

        if repuesta == 1 :
            nombre_junto = apellido_persona +","+nombre_persona
         
            nombre_dicionario[nombre_junto]=edad 
        
    if not encontrado:
            nombre_junto = apellido_persona +","+nombre_persona
            nombre_dicionario[nombre_junto]=edad 
            print("agregado")         
    
        
def cumpleCliente(nombre_dicionario:dict ,nombre_cliente , apellido_cliente ):
     encontrado = False 
     edad = 0 
     for clave ,valor in nombre_dicionario.items():
          apellido , nombre = clave.split(",")

          if nombre == nombre_cliente and apellido_cliente == apellido:
               edad = valor 
               encontrado = True 
               break 
     if encontrado:
        nombre_completo = apellido_cliente +","+nombre_cliente
        nombre_dicionario[nombre_completo] = edad + 1 
     else:
          print("el cliente no existe ") 
clientes = {"Chuleton,Jose":35 , "Tosidad,Ruben":27 , "Rupto,Francisco":44 , "Coton,Carmelo":56 }



cumpleCliente(clientes,"mikael","Chuleton")
print(clientes)

lista_convertida = []


for clave , valor in clientes.items():

    lista_convertida.append([clave,valor])


lista_aux = []
for i in lista_convertida:
    
    a = i[0].split(",")
    
    lista_aux.append(a[1].strip())



lista_aux.sort()#nombre ya ordenados

#tenercuidado con los espacis en los diciionarios que pueden dar un error

lista_bu = []
for i in range(len(lista_aux)) :    
    for j in range(len(lista_convertida)):

        a = lista_convertida[j][0].split(",")
        if a[1] == lista_aux[i] :
            lista_bu.append(lista_convertida[j])





for i in lista_bu:
    a = i[0].split(",")
   
    print(f"{a[1]} {a[0]} ({i[1]})")
