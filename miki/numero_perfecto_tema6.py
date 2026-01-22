def esamigo(num1:int )->bool:
    contador_divisores_uno = 0
    for i in range(1,num1):
        if num1 % i == 0:
            contador_divisores_uno += i






    if contador_divisores_uno == num1 :
        return True
    return False




while True:
    usuario = input("Ingresa un numero: ")

    if usuario.isdigit() and int(usuario) > 0 :
        numero_final = int(usuario)
        break
    else:
        print("Vuelva a ingresar el valor ")


if esamigo(numero_final) :
    print("El numero es perfecto")
else :
    print("El numero no es perfecto")