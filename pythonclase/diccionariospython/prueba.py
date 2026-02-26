palabra = "Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera"


palabra_split = palabra.split(" ")



no_repetidos = []

for i in palabra_split:

    if i not in no_repetidos:

        no_repetidos.append(i)


dicionario_clave = {}
for i in no_repetidos:

    dicionario_clave[i]=palabra_split.count(i)


print(dicionario_clave)





