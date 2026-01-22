letra = input("ingrese la letra")

if letra.count(' ') < 1:
    print("incorrecto tienen que tener mas de un espacio ")
else:

    letras  = 0
    for i in letra:

        if i != '.':

            letras += letra.count(i)

    print(letras)



