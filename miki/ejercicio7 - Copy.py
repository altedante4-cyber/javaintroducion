def comprobarmac(mac):

    punto = False
    array_hexadecimal = ['A', 'B', 'C', 'D', 'E', 'F']
    mayuscula = False

    # Verificar mayúsculas
    for i in mac:
        if i.isupper():
            mayuscula = True
            break

    # Verificar si contiene punto
    for i in mac:
        if i == ".":
            punto = True
            break

    formato_correcto_punto = False
    separar_punto = mac.split(".")

    for i in range(len(separar_punto)):
        if len(separar_punto[i]) == 4:
            formato_correcto_punto = True

    if punto and mayuscula and formato_correcto_punto:

        almacenar_resultador_punto = []

        for bloque in separar_punto:
            a = bloque[0]
            b = bloque[1]
            c = bloque[2]
            d = bloque[3]

            vale_a = int(a, 16)
            vale_b = int(b, 16)
            vale_c = int(c, 16)
            vale_d = int(d, 16)

            resultado = (vale_a * pow(16, 4)) + (vale_b * pow(16, 2)) + (vale_c * 16) + vale_d
            almacenar_resultador_punto.append(resultado)

        mac_valida_punto = True
        for i in almacenar_resultador_punto:
            if i <= 510:
                mac_valida_punto = False
                break

        return mac_valida_punto

    if not punto:

        separar = mac.split(":")
        almacenar_resultador = []
        formato_correcto = False

        for i in range(len(separar)):
            if len(separar[i]) == 2:
                formato_correcto = True

        if formato_correcto:

            for bloque in separar:
                a = bloque[0]
                b = bloque[1]

                vale_a = int(a, 16)
                vale_b = int(b, 16)

                resultado = (vale_a * 16) + vale_b
                almacenar_resultador.append(resultado)

            mac_valida = False
            for i in almacenar_resultador:
                if i <= 255:
                    mac_valida = True
                    break

            return mac_valida

    return False

#con esta funcion estamos recorriendo todas las mac para verificarr si son validas o no

def macsValidas2(*args):

    for i in args:
        if  comprobarmac(i):
            return True
    return False


def macsValidas(*args):
    contador_macs_validas = 0
    contador_macs_no_validas= 0

    for i in args:
        if macsValidas2(i):
            print(f"{i} valida")
            contador_macs_validas += 1
        else:
            print(f"{i} no es  valida")
            contador_macs_no_validas += 1


    print(f"MACs validas: {contador_macs_validas}")
    print(f"MACs no validas: {contador_macs_no_validas}")







macsValidas("F4:8E:38:AF:F4:1C", "7521-MXP")




