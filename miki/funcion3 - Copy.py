def divisorescomunes(num , num2 ):

    if type(num) == int and num > 0 and type(num2) == int and num2 > 0  :

        numeros = set()

        for i in range(1,num + 1):

            if num % i == 0  :
                numeros.add(i)

        b = set()
        for i in range(1,num2 + 1 ):

            if num2 % i == 0:
                b.add(i)


        numeros_comunes = numeros & b

        numeros_ordenador = ", ".join(str(i) for i in sorted(numeros_comunes))
        numeros_unicos = ", ".join(str(i) for i in numeros_comunes)

        if len(numeros_comunes) == 1 :
            return f"El unico divisor comun de {num} y {num2} es : {numeros_ordenador} "

        else:

            return f"Los divisores comunes de {num} y {num2} son :  {numeros_unicos} "
    else:
        return "No puedo calcular los diviores comunes de esos numeros"



print(divisorescomunes(22,16))
print(divisorescomunes(33,17))
print(divisorescomunes(22.5,0))
