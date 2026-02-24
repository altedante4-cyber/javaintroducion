def validacion_usuario():

    #mostrar el  precio en dos decimales segun los kilos que quiera

    try:
        frut = input("?Que fruta quiers comprar ")
        kil =  input("Cuantos kilos quieres ? ")


        encontrado = False 
        guardar_precio = 0 

        for fruta , precio in frutas.items():

            if fruta == frut:
                encontrado = True 
                guardar_precio += float(kil) * precio 
                break 

        if encontrado :
            print(guardar_precio)

        print("Lo siento mucho pero no vendemos esa fruta ")


    except:

        print("No has introducido bien la cantidad que quieres  ")





frutas = {
    "Aguacate":4.35,
    "Mandarina":2.60,
    "Kiwi":3.75,
    "Naranja": 1.80
}

validacion_usuario()


