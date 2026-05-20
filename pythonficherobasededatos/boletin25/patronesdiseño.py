# Tu objetivo es convertir esta lista:
letras = ["p", "a", "t", "r", "o", "n"]

# En esta lista:
# ["n", "o", "r", "t", "a", "p"]

inicio = 0 
final= len(letras) -1

while inicio < final :
        letras[inicio] , letras[final] = letras[final] , letras[inicio]

        inicio += 1
        final -= 1



print(letras)
