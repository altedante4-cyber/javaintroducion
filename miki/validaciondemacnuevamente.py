def validarmac(mac:str)-> bool:

    #tiene que tener 6 bytes para ser una mac valida es decir  que un byte es conformado por 2 elementos 2 + 2 + 2 + 2 + 2 + 2
    # si la longitud es mayor que 6 return false
    # que cade dos elementos no puede superar 255 en suma es decir FF
    # si vienen con . les hacemos un replace con dos puntos
    mac_sin_puntos = mac.split(":")
    cifras_validas = {
        "a":"10",
        "b":"11",
        "c":"12",
        "d":"13",
        "e":"14",
        "f":"15",
    }


    for valor in mac_sin_puntos:
        suma = 0
        mac_valida_sum = False
        primer_char = valor[0]
        segundo_char = valor[1]

        if primer_char in cifras_validas:
            primer_valor = cifras_validas[primer_char]
        else:
            primer_valor = int(primer_char)

        if segundo_char in cifras_validas:
            segundo_valor = cifras_validas[segundo_char]
        else:
            segundo_valor = int(segundo_char)

    # calcular valor de byte

            valor_byte = primer_valor * 16 + segundo_valor
            suma += valor_byte
        if suma > 255 :
            mac_valida_sum = True
        if primer_valor not in cifras_validas:
            mac_valida_sum = True
        if segundo_valor not in cifras_validas:
            mac_valida_sum = True
    if mac_valida_sum:
        return False
    return True



def mostrarmac(*mac):

    for i in mac:
        if validarmac(i):
            print(i)



mostrarmac("F4:8E:38:AF:F4:1C")