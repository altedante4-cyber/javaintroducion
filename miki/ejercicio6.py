ip = input("Introduce una direccion IP :")

es_leter = True


for k in ip:
    if k.isalpha():
        es_leter = False

if es_leter:

    ip_sin_puntos = ip.split(".")

    guardar_ip = []

    for i in ip_sin_puntos:
        guardar_ip.append(i)



    ip_valida = True

    #no podemos comparar esto i >= "0" esto da error si o si hay que pasarlo a int
    for i in guardar_ip:
        if int(i) < 0 or int(i) > 255:
            ip_valida = False
            break





    if ip_valida:

        primer_numero = guardar_ip[0]
        if int(primer_numero) >= 0 and int(primer_numero) <= 127:

            print(f"{ip}/8")
        elif int(primer_numero) >= 128 and int(primer_numero) <= 191:
            print(f"{ip}/16")
        elif int(primer_numero) >= 192 and int(primer_numero) <= 223:
            print(f"{ip}/24")
        elif int(primer_numero) >= 224 and int(primer_numero) <= 255:
            print("Direccion reservada")
        else:
            print("Direccion no valida")


    else:
        print("Direccion no valida")
else:
    print("Direccion no valida")