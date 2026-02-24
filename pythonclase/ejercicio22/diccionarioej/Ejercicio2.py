def validar_notas(notas:list):

    modulos_resuperar = []
    encontrado = False 
    for modulo , nota in notas.items():

        if nota < 5 :
            encontrado = True 
            modulos_resuperar.append([modulo,nota])
    
    nota_media = 0 

    for i in notas.values():
        nota_media += i 

    if encontrado :
        for i in modulos_resuperar:
            a  = i[0]
            b = i[1]

            print(f"{a} con un {b}")


        print(f"La nota media obtenida es de { nota_media / 6:.2f}")

    else:
        print("El alumno non tiene que recuperar ningun modulo ")
        print(f"La nota media obtenida es de { nota_media / 6:.2f}")
        

notas ={
    "Redes":5,
    "Python":5.15,
    "Marcas":6.30,
    "FOL":8.80,
    "Sistemas":5,
    "Bases de Datos" : 7.00
}


#mostrar que modulos tienen que recuperar
#nota que tiene en esos modulos
#mostrar la nota mdia con dos decimales 




validar_notas(notas)
