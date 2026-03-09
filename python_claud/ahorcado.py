import random 

palabras_jugar = ["hola","como","veinte"]

elegir_palabra =  random.choice(palabras_jugar)

array_palabra = ["_"]* len(elegir_palabra) 
ganado = False

while no    t ganado :

    print(" ".join(array_palabra)) #mostramos el progreso del usuario
    usuario=input("ingrese solo una letra: ").lower()

    #verificar si la letra esta en la palabr

    for j in range(len(elegir_palabra)):
        if usuario ==elegir_palabra[j]:
            array_palabra[j] = usuario 

        
    #revirsar si gano 

    if "_" not in array_palabra:
        ganado = True 
        print("ganasta la palabra era " , elegir_palabra )

