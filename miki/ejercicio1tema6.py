def esamigo(num1:int , num2:int)->bool:
    contador_divisores_uno = 0
    contador_divisores_dos = 0


    for i in range(1,num1):
        if num1 % i == 0:
            contador_divisores_uno += i



    for j in range(1,num2):
        if num2 % j == 0:
            contador_divisores_dos += j



    if contador_divisores_uno == num2 or contador_divisores_dos == num1:
        return True
    return False



if esamigo(1184,1210):
    print("Es un numero amigo")
else:
    print("No es un numero amigo")
