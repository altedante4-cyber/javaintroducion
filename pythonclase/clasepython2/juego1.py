"""
Docstring for juego1
Juego encuentra el tesoro en la tupla
Creamos una tupla con varios elementos:

tesoro = ("oro", "plata", "joya", "mapa", "espada")


Tu misión es adivinar la posición de un tesoro que yo elija. Por ejemplo, si quiero que encuentres "mapa":

# Mostrar el tesoro en la tupla
print(tesoro[3])


Aquí, el índice 3 es la posición de "mapa" (recordemos que Python empieza a contar desde 0).

Después de esto, podemos hacer retos como:

¿Cuál es el primer tesoro?

¿Cuál es el último?

¿Cuántos tesoros hay en total?
"""

tesoro = ("oro", "plata", "joya", "mapa", "espada")

user = input("ingrese el tesoro que vaya a buscar").lower()


contador = 0 

for i in tesoro:

    if i == user:
        
        
        print(f"fue encontrado en la posicion {contador}")

    else:

        contador += 1 
    







