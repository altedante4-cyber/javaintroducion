
try:
    fichero = open("fichero.txt","at" )
        #w => siempre empiesa desde el principio siel ficheor no  existe lo borra por completo 
        # a => empesamos a agregar desde el final del ultimo contenido  si el fichero no existe crea uno nuevo  

    fichero.write("HOLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        
    #siempre hay que cerrar el fichero 
except Exception:
    print("Error")
finally:
    fichero.close()

#otra manera de hacerlo


try:
    with open("fichero.txt","a") as f :
        sueldo =4304
        texto = "Tu sueldo es " + str(sueldo) + " euros \n "
        fichero.write(texto)
    #con esto evito   poner el close es decir olvidarme cerrar el fichero 
    
except:
    print("Error")
    