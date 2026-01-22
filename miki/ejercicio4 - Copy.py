def toBinario(num):

    convertir_txt = str(num)
    tiene_float = True
    tiene_numeros = False
    for i in convertir_txt:

        if i == '.' :
            tiene_float = False
        elif i.isdigit():
            tiene_numeros = True


    if tiene_numeros:

        if int(num) >= 0 and  int(num) <= 255 and tiene_float :
            numeros_binarios = []
            contador = 1

            for i in range(8):  # por que son de 8 bits solo
                numeros_binarios.append(contador)
                contador *= 2

            numeros_binarios_reversed = numeros_binarios[::-1]

            numeros_temp = []  # aqui estan todos los numeros menor que 22 en potencias de dos para poder pasar a binario

            for i in range(len(numeros_binarios_reversed)):

                if numeros_binarios_reversed[i] <= num:
                    numeros_temp.append(numeros_binarios_reversed[i])

            suma = 0

            seleccionados = []

            binario = []

            for n in numeros_binarios_reversed:

                if suma + n <= num:
                    suma += n
                    binario.append('1')
                else:
                    binario.append('0')

            binario_devolver = ""
            for i in binario:
                binario_devolver += i


            return binario_devolver




        else:
            return -1
    else:
        return -1




print(toBinario(22))
print(toBinario(129))
print(toBinario(345))
print(toBinario(22.3))
print(toBinario("hola"))
print(toBinario(-2))
