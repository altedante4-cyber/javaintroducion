def validacion(nombre:str , apellido:str ):

    listas = []
    for clave in clientes.items():

        ape , nom = clave.split(",")

        listas.apped([nom,ape])    


    for i in listas:
        a = i[0] #nomnbre 
        b = i[1] #apellido 

        if a == nombre  and b == apellido:
            return True 
        
    return False 

clientes = { "Chuletón, José": 35, "Tosidad, Rubén": 27, "Rupto, Francisco": 44, "Cotón,Carmelo": 56 ,"hola,peredo" : 20 }

nombre = input("Ingrese el nombre ")
apelido = input("Ingrese el apellido ")
edad = int(input("Introduce la edad "))


if validacion(nombre , apelido):
    print("se encuentra ya en la base de datos ")

if not validacion(nombre , apelido):
    
    print("registrado")

