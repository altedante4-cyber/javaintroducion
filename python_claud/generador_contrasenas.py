import string 
import random

def generar_contrasena(longitud:int ,mayusculas:str , numeros:str , especiales:str ):
    lista_generar = "" 

    
    if mayusculas == "si":
        lista_generar += string.ascii_uppercase
    if  numeros == "si" : 
        lista_generar += string.digits
    if especiales == "si":
        lista_generar += string.punctuation
    # Verificar que haya al menos un tipo seleccionado
    if lista_generar == "":
        return None
    
    lista_nueva = list(lista_generar)
    contrasena_generada = []

    for i in range(longitud):
            
        ale = random.choice(lista_nueva)

        contrasena_generada.append(ale)
        
    return "".join(contrasena_generada)
    
def evaluar_fortalesa(contrasena:str):
    seguridad = ""

    #como el enunciado no dice la validacion sobre que tiene que tener una contrasena fuerte pues no lo inventamos
    tiene_mayuscula = False
    tiene_numeros = False
    tiene_caracteres_especiales = False

    if contrasena.isdigit():
        tiene_numeros = True 
    if contrasena.isalpha():
        tiene_mayuscula = True 
    
    if len(contrasena) >= 8 and tiene_numeros and tiene_mayuscula :
        seguridad += "Fuerte"
    else:
        seguridad += "Debil"

    
    return seguridad 
    

longitud = int(input("Ingrese la longitud "))
mayusculas = input("Mayusculas : si o no ")
numeros = input("Numeros : si o no ")
especiales = input("Especiales si o no ")

a =  generar_contrasena(longitud,mayusculas,numeros,especiales)
b = evaluar_fortalesa(a)

print(a)
print(b)


