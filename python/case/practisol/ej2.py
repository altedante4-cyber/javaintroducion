#2Generador de Contrasenas ficticias
#crea una lista con letras minusculas otra con numeros y otr con simbolos
#genera una contrasena de longitud 8 tomando elementos aleatorios de estas listas y combinandolos


#1.identificar tareas necesarias (acciones generales)

#Acciones generales del ejercicio

#1.Crear listas con letras , numeros y simbolos
#2.Elegir elementos al azar de esas listas
#3.Combinar esos eleemntos en una sola contrasena
#Asegurar que la longitud de la contrasena sea 8 


#2.CONVERTIR CADA ACCION EN SUBPROBLEMAS ESPECIFICOS

#ahora debes dividir cada accion en paisitos ma detallados y concretos

#SUBPROBLEMA 1:Crear listas de caracteres

#Crear una lista de letras minusculas
#Crear una lista de numeros
#Crear una lista de simbolos


#Seleccionar elementos aleatorios

#Elegir un caracter aleatorio de cualquiera de las tres listas
#Repetir esa seleccion hasta reunir 8 caracters

#SUBPROBLEMA contruir la contrasena

#Guardar los caracters selecionados 
#Unirlos en una cadena de texto

#SUBPROBLEMA 4 ENTREGAR LA CONTRASENA

#Mostrar la contrasena generada al usuario

#Resultado final (resumen sintettco)
#Crear listas de letras,numeros y simbolsos
#Elegir aleatoriamente un caracter de caulquiera de las listas
#Repetir la seleccion hasta tener 8 caracteres
#Combinar los caracteres en una sola cadena
#Mostrar la contrasena generada
import random 
num = [0,1,2,3,4,5,6,7,8,9]
letras = ['a','e','i','o','u']
simbolos = ["!", "@", "#"]


conbinacion = [*num,*letras,*simbolos]

contrasena = random.sample(conbinacion , 8)



print("".join(str(x) for x in contrasena))
#generador de contrasena mejorado que siempre incluya al menos un numero

import random
numeros = [0,1,2,3,4,5,6,7,8,9]
letras = ['a','e','i','o','u']
simbolos =['!' ,'@','#']

#1 al menos un elemento de cada tipo

obligatodios = [

    random.choice(numeros),
    random.choice(letras),
    random.choice(simbolos)
]

#2crear una lista combinada con todos los caracteres posibles

combinacion_total = [*numeros,*letras,*simbolos]

#3 completar hasta tener 8 caracteres

restantes = random.sample(combinacion_total , 8 - len(obligatodios))

#4 unir obligatorios + restantes

contrasena = obligatodios + restantes

#5 mezclar para que no siempre empiece con numero-letra-simbolo

random.shuffle(contrasena)

#6convertir cada elemento a string y unirlos

resultado = "".join(str(x) for x in contrasena)

print(resultado)


