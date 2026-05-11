
try:
<<<<<<< HEAD
    fichero = open("fichero.txt","at" ):
        #w => siempre empiesa desde el principio
        # a => empesamos a agregar desde el final del ultimo contenido 
=======
    fichero = open("fichero.txt","at" )
        #w => siempre empiesa desde el principio siel ficheor no  existe lo borra por completo 
        # a => empesamos a agregar desde el final del ultimo contenido  si el fichero no existe crea uno nuevo  

    fichero.write("HOLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        
    #siempre hay que cerrar el fichero 
>>>>>>> 5206c623ef7e1f2e31e5854442919b4541342ccc
except Exception:
    print("Error")
finally:
    fichero.close()
<<<<<<< HEAD
    

=======

#otra manera de hacerlo


try:
    with open("fichero.txt","a") as f :
        sueldo =4304
        texto = "Tu sueldo es " + str(sueldo) + " euros \n "
        fichero.write(texto)
    #con esto evito   poner el close es decir olvidarme cerrar el fichero 
    
except:
    print("Error")
    
>>>>>>> 5206c623ef7e1f2e31e5854442919b4541342ccc
