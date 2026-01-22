def validar_ip(ip):
        """
        Valida una dirección IPv4 y determina su clase/máscara

        Args:
            ip (str): Dirección IP a validar

        Returns:
            tuple: (es_valida, mensaje, mascara)
                   es_valida: True/False
                   mensaje: Texto descriptivo

        """

        # PROGRAMA MEJORADO (10/10) - Manteniendo tu estilo

        # 1. Pedir la IP


ip = input("Introduce una direccion IP: ")

# 2. Verificar que no tenga letras (como hacías)
tiene_letras = False
for k in ip:
    if k.isalpha():
        tiene_letras = True
        break

if tiene_letras:
    print("Direccion no valida")
else:
    # 3. Dividir por puntos
    partes = ip.split(".")

    # 4. VERIFICACIÓN NUEVA: Tiene que tener exactamente 4 partes
    if len(partes) != 4:
        print("Direccion no valida")
    else:
        # 5. Verificar que todas las partes tengan algo
        # (no puede haber partes vacías como en "192.168..1")
        hay_parte_vacia = False
        for parte in partes:
            if parte == "":
                hay_parte_vacia = True
                break

        if hay_parte_vacia:
            print("Direccion no valida")
        else:
            # 6. Verificar que sean números válidos (0-255)
            # IMPORTANTE: Ahora con verificación de que se puede convertir a int
            ip_valida = True
            numeros = []  # Para guardar los números convertidos

            for parte in partes:
                # Verificar que todos los caracteres sean dígitos
                # (por si hay símbolos como +, -, etc.)
                es_numero = True
                for caracter in parte:
                    if not caracter.isdigit():
                        es_numero = False
                        break

                if not es_numero:
                    ip_valida = False
                    break

                # Verificar que no empiece con 0 si tiene más de un dígito
                # (ej: "01" no es válido, pero "0" sí)
                if len(parte) > 1 and parte[0] == '0':
                    ip_valida = False
                    break

                # Convertir a número y verificar rango
                numero = int(parte)
                if numero < 0 or numero > 255:
                    ip_valida = False
                    break

                numeros.append(numero)

            if ip_valida:
                # 7. Determinar clase basada en el primer número
                primer_numero = numeros[0]

                if primer_numero >= 0 and primer_numero <= 127:
                    print(f"{ip}/8")
                elif primer_numero >= 128 and primer_numero <= 191:
                    print(f"{ip}/16")
                elif primer_numero >= 192 and primer_numero <= 223:
                    print(f"{ip}/24")
                elif primer_numero >= 224 and primer_numero <= 255:
                    print("Direccion reservada")
                else:
                    # Esto no debería pasar por las validaciones anteriores
                    print("Direccion no valida")
            else:
                print("Direccion no valida")

