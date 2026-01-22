# Pedimos el número
numero = input("Introduce un numero: ")

# Convertimos el número en lista de dígitos para mantener el orden
array_numeros = list(numero)

# Para mantener el orden de aparición, usaremos una lista para los vistos
digitos_vistos = []
lista_auxiliar = []

for d in array_numeros:
    # Solo procesamos el dígito si no lo hemos contado ya
    if d not in digitos_vistos:
        contador = 0
        for x in array_numeros:
            if x == d:
                contador += 1

        lista_auxiliar.append([d, contador])
        digitos_vistos.append(d)  # Marcamos como procesado

# Mostramos el resultado
print("Tu número tiene:")
for digito, cantidad in lista_auxiliar:
    if cantidad == 1:
        print(f"{cantidad} número {digito}")
    else:
        print(f"{cantidad} números {digito}")