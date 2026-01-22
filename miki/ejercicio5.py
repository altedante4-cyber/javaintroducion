def divisoresComunes(num1, num2):


    tiene_float = False

    for i in str(num1):
        if i == ".":
            tiene_float = True
    for i in str(num2):
        if i == ".":
            tiene_float = True


    if not tiene_float:
        array1 = []
        array2 = []

        array3_iguales = []
        for i in range(1,num1 + 1):
            if num1 % i == 0:
                array1.append(i)

        for i in range(1,num2 + 1):
            if num2 % i == 0:
                array2.append(i)


        for i in array1:

            if i in array2:
                array3_iguales.append(i)





        if len(array3_iguales) == 1 :
            return (f"El unico divisor comun de {num1} y {num2} es {",".join(str(i)for i in array3_iguales)}")
        else:
            return (f"Los divisores comunes de {num1} y {num2} son {",".join(str(i) for i in array3_iguales)}")
    else:
        return ("No puedo calcular los divisores comunes de esos numeros ")


print(divisoresComunes(22.5,0))