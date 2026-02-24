

#que el programa contemple sueldo validos  dado que es  entero y  y float


valido = False

while not valido:
    try:
        entrada = input("INtroudce tu sueldo")
        sueldo = float(entrada)

    except : #esto es de caracter general  pero cunado queremos capturar un  error en expecifico utilzamos por ejemplo el ValueError

        print("Estas introduciendo un sueldo invalido ")
    else:

        valido = True

if valido:
    print("Esto es valido")


