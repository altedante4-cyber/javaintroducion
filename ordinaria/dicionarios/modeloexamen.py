texto = "Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera"
temp = texto.split()


dico = {}

for i in temp:
    dico[i] = dico.get(i,0)+1

print(dico)