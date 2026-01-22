def validarperfecto(a):

    lista_divisores = []
    for i in range(1,a):
        if a % i == 0:
            lista_divisores.append(i)

    if sum(lista_divisores) == a:
        return True
    return False


usuario = int(input("Ingrese un numero "))

if validarperfecto(usuario):
    print("es perfecto")

while not validarperfecto(usuario):

      user = int(input("vuelve a intentarlo"))

      if validarperfecto(user):
          print("Es un numero perfecto")
          break





