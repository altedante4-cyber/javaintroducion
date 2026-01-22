cadena1 = input("Introduce la primera cadena ")
cadena2 = input("Introduce la subcadena cadena ")

longitud = len(cadena2)
recolectar_aparicion = []
encontrado = False
for j in range(len(cadena1)):

    recolectar_aparicion.append(cadena1[j:j+longitud])


encontrado = False



if cadena2 == recolectar_aparicion[0]:
    print("Palabra encontrada")
else:
    print("Palabra no encontrada")


#otra forma de hacerlo pero mas eficas es de la siguiente manera

if cadena1.startswith(cadena2):
    print("Palabra encontrada")
else:
    print("Palabra no encontrada")