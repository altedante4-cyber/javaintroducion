
entrada = input("ingrese una contrasena")

minimo_largo = False 
Mayuscula = False
Digitos = False


if len(entrada) >= 8:
     minimo_largo = True 


for char in entrada:
     
     if char.isupper() :
          Mayuscula = True 

     if char.isdigit():
          Digitos = True 

     
     #si ya encontramos lo que buscamos podemos salir del bucle

     if Mayuscula and Digitos :
          break
     

# Condición 1: Si NO cumple el largo mínimo (Regla de clasificación 3)
if not minimo_largo:
        print("Clasificación: Muy Débil (El largo mínimo es 8 caracteres).")
    
    # Condición 2: Si cumple largo Y mayúscula Y dígito (Regla de clasificación 2)
elif minimo_largo and Mayuscula and Digitos:
    print("Clasificación: Fuerte.")
        
    # Condición 3: Si cumple solo el largo (Regla de clasificación 1)
elif minimo_largo: # Sabemos que no es 'Fuerte', así que si solo cumple largo, es aceptable.
        print("Clasificación: Aceptable (Podría mejorar con mayúsculas y dígitos).")
     