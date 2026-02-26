from datetime  import  time , datetime , timedelta 

def buscar_contacto(nombre:str):

    try:

        posicion = 0

        encontrado = False 
        for i in range(len(lista_contactos)):
    
            for clave ,valor in lista_contactos[i].items():
            
                if valor == nombre :
                    posicion = i 
                    encontrado = True 
                    break 
        
        if encontrado:
            return lista_contactos[posicion]
        else:
            raise KeyError
    except KeyError:
        print("No encontrado usuario ") 

def agregar_contacto(nombre:str , telefono:str , email:str , fecha_nacimiento:str ):

    try:

        if buscar_contacto(nombre):
            raise ValueError

        if not buscar_contacto(nombre):
            contacto = {"nombre":nombre,"telefono":telefono,"email":email,"fecha_nacimiento":fecha_nacimiento}

            lista_contactos.append(contacto)
            print("agregado correctamente")

    except ValueError:
            print("el usuario ya existe en la base de datos  ")
        

def mostrar_nombre():
    for i in lista_contactos:
        for clave , valor in i.items():

            if clave == "nombre":

                print(f"{valor}")

def mostrar_telefono():
    for i in lista_contactos:
        for clave , valor in i.items():

            if clave == "telefono":

                print(f"{valor}")

def mostrar_agenda():

    lista_valores  = []

    for i in lista_contactos:

        for clave , valor in i.items():

            lista_valores.append([clave,valor])
    
    
    
    
    print("-"*50)
    print(f"{'AGENDA DE CONTACTOS':<20} - {'Generada el:':^10} {datetime.now().date()} {datetime.now().time()}")
    print("-"*50)
    print(f"{'NOMBRE':<20} | {'TELEFONO':<5} | {'EMAIL':<5}")
    print("-"*50)
    for i in lista_valores:
        
        nombre = i[0]
        telefono = i[0]
        email = i[0]

        if nombre == "nombre":
            
        
            

        

       

    



contacto1= {
    "nombre": "Ana García",
    "telefono": "666111222",
    "email": "ana@email.com",
    "fecha_nacimiento": "15-03-1990"
}

contacto2= {
    "nombre": "Michael peredo",
    "telefono": "12345",
    "email": "michael@email.com",
    "fecha_nacimiento": "18-04-2044"
}
contacto3= {
    "nombre": "Valeria sapata",
    "telefono": "1234567",
    "email": "Valeria@email.com",
    "fecha_nacimiento": "10-04-3234"
}
lista_contactos = [contacto1,contacto2,contacto3]


mostrar_agenda()