def transformar(mensaje,desplazamiento , modo='cifrar'):
    #si descriramos invertirmo el desplzamiento
    if modo =='descifrar':
        desplazamiento = -desplazamiento
    resultado = []

    for char in mensaje:
        if char.isalpha():
            #determinamos el punto de inicio (base)dependiendo si es mayusucula o minusculas
            inicio = ord('A') if char.isupper() else ord('a')
            #convertimos a posicion 0-25 (char-inicio)
            #aplicacmos desplazmiento + modulo 26 para el cilo
            #regresamos a ascci sumando la base
            nuevo_char = chr((ord(char) - inicio + desplazamiento ) % 26 + inicio )
            resultado.append(nuevo_char)
        else:
            #si no es letra(espacio,punto) lo dejamos igual
            resultado.append(char)

    return "".join(resultado)


#menu principla

while True :
    print("\n1.Cifrar , 2.Descifrar,3.Fuerza Bruta 4.Salir")
    opcion = input("Elige una opcion ")

    if opcion == '4': break
    if opcion in ['1','2','3']:
        mensaje = input("mensaje")

        if opcion == '3':
            for i in range(1,26):
                print(f"Desplazamiento {i} : {transformar(mensaje,i,'descifrar')}")
        else:
            desp = int(input("Desplazamiento"))
            modo = 'cifrar' if opcion == '1' else 'descifrar'
            print("Resultado" , transformar(mensaje,desp,modo))