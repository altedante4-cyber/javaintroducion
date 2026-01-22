
vocales = ["a","e","i","o","u"]
letras = input("ingrese la letras")

#tenemos que contar en cada palabra si tiene 4 vocales la palabra nos vales


letras_separada = letras.split(' ')


array_letras = []

for palabra in letras_separada:

    contador = 0

    for letra in palabra:

        if letra in vocales:
            contador += 1

    if contador > 4:
        array_letras.append(palabra)

print(array_letras)

#aprende para reinicir el contador se pone dentro del for lo que hace el primer for es que recorre
#la palabra el segundo for es el que trabaja  y agrega la palabra el primer for solo recorre els tring


