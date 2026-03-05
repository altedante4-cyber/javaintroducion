def agregar_contacto():
    # la clave es el nombre y el telefono es el valor 

    nombre = input("Ingrese su nombre ")
    telefono = input("Ingrese su telefono ")

    if  existe_pila(nombre):
        validar = int(input(("Existe esas credenciales en la base de datos desea sobre escribri 1.si o 2.no ")))
        
        match validar:

            case 1 :
                agenda[nombre] = telefono 
                print("valor sobre escrito")
            case 2 :
                print("gracias , no se ha registrado nada ")
            case _:
                print("VALOR INVALIDO ")


        
    agenda[nombre] = telefono
    print("agregado correctamente ")
    
def existe_pila(nombre):
    # solucion simple para verificar si existe un dato o no 

    #busca directamente en la llaves del diccionario
    if nombre in agenda:
        return True 
    
    return False 
    # de la forma que lo estaba haciendo es de la siguiente
    #for clave in agenda.keys():
     ##      return True 
   # return False 

def buscar_contacto():
    
    nombre = input("Ingrese el nombre del usuario ")

    if existe_pila(nombre):

        print(agenda.get(nombre))
    else:
        print("no existe")



        


def eliminar_contacto():
    nombre = input("Ingrese el nombre del usuario ")
    
    #if nombre not in agenda:
     #       print(f"Error: El usuario '{nombre}' no existe ")
      #      return #salimos de la funcion para evistar errores     

    if not existe_pila(nombre):
        print("No existe el usuario para eliminarlo")
        return  # <-- iportan sin esto el codigo sigue y da el KeyError
    #si llego aqui es porque si existe
    agenda.pop(nombre)
    print("eliminado correctamente")

   #si elusuario no existe impirmes un mensaje de eeror pero el programa no se detiene python sigue ejeecutnado la siguiente line(agenda.pop(nombre))
   #y como el nombre no esta en el diccionario lanza el keyError

   #Uso de pop() en diccionarios
   #para eliminar un elemento de un diccionario po rus clave la isntaxis correcta es agrenda.pop(clave) si la clave no existe lanzara el error a menos que le des un valor por defecto
def listar_contactos():

    for nombre in sorted(agenda):
        print(nombre , agenda[nombre])

    #aprendi a como listar los contactos alfabeticamente  con sorted lo que hacemos es iterar con la clave sobre agenda mostramos la clave que es el nombre
    # y luego mostrar el valor atraves de la clave agenda[nombre



agenda = {}

opcion = 0

while opcion != 5 :
    
    opcion = int(input("\n 1.Agregar contacto \n 2.Buscar contacto \n 3.Eliminar contacto \n 4.listar_contactos \n 5.salir "))

    match opcion :
        case 1:
            agregar_contacto()
        case 2:
            buscar_contacto()
        case 3 :
            eliminar_contacto()
        case 4:
              listar_contactos()
        case 5 :
            print("saliendo. ... . . ")
        case _:
            print("Valor invalido ")

    