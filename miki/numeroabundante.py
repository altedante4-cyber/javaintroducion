def validar_abundante(numero):

    sumar = 0


    for i in range(1,numero):

        if numero % i == 0:
            sumar += i


    if sumar > numero:
        return True
    else:
        return False


def mostrar_abundante(num1:int , num2:int)->bool:

    lista = []
    for i in range(num1 ,num2+1):

        if validar_abundante(i):
            lista.append(i)

    return lista



resultado = mostrar_abundante(10,20)
print(resultado)