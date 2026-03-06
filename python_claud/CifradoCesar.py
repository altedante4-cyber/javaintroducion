def cifrar(mensaje,desplazamiento):

    cifrado_numerico = [ ord(i)+desplazamiento  for i in mensaje ]

    resultado =[chr(i) for i  in cifrado_numerico ]

    return "".join(resultado)



def decifrar(mensaje, desplazamiento):
    cifrado_numerico = [ ord(i)-desplazamiento  for i in mensaje ]

    resultado =[chr(i) for i  in cifrado_numerico ]

    return "".join(resultado)
    


opcion = 0 

while opcion != 4 :

    print(f"\n 1.CIFRAR , 2.DESCIFRAR , 3.ROPER EL CIFRADO  , 4.SALIR")
    
    try:
         opcion =int(input("ingrese opcion : "))
         if opcion  not in [1,2,3,4]:
            print("errror")

    except ValueError:
        print("ERROR")
    
    match opcion:
        case 1 :

            mens = input("Ingrese el mensaje")
            numero_desp = int(input("Ingrese el numero desplazamiento "))
            
            print(cifrar(mens,numero_desp))
            print("===mensaje cifrado correctamente")
        case 2:
            mens = input("Ingrese el mensaje")
            numero_desp = int(input("Ingrese el numero desplazamiento "))
            
            print(decifrar(mens,numero_desp))
            print("===mensaje decifrado correctamente")

        case 3 :
            #en el caso que no se pamos el desplazamiento fuerza bruta 

            mens = input("Ingrese el mensaje ")
            lista_de_desplazamiento = []

            #iteramos 25 vees (del 1 al 25)

            for i in range(1,26):
                palabra_transformada = ""

                #por cada vuelta recorrems cada letra de la palabra original

                for letra in mens:
                    #obtenemos el valor ascci le sumamos el desplazamiento (i)
                    #convertirmos de nuevo a caracter 

                    nueva_letra = chr(ord(letra)-i)
                    palabra_transformada += nueva_letra

                #guardamos la palabra acumulada en nuestra lista 
                lista_de_desplazamiento.append(palabra_transformada)
            
            print(lista_de_desplazamiento)





#explicacion de los puntos clave
#1.range(1,26) este bucle externo contorla cuantas veces realizamos el desplazamiento completo
#palabra_transfromada ="" es nuestra variable temporal es muy iportante que se reinicie vacia al prinipio de cada vuelta (dentro del primer for) 
#para que ada palabra en la lista sea independiente
#ord(letra)+i aqui es donde ocurre la magia ord()convierte la letra en un numero le sumammos i el nuevo de vueta  y luego chr(
# lo conveierte de neuvo en el caracter desplazado)
#.append() al final de cada vuelta del bucle principal guardamos la cadena resultante en la liista final






