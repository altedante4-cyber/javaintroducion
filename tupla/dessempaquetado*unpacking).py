# Asignar elementos a variables individuales
persona = ("Juan", 25, "Madrid")
nombre, edad, ciudad = persona

print(nombre) # "Juan"

# Desempaquetado extendido (usando *)
numeros = (1, 2, 3, 4, 5)
primero, *medio, ultimo = numeros
# primero = 1, medio = [2, 3, 4], ultimo = 5