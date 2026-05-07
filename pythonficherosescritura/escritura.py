
try:
    fichero = open("fichero.txt","at" )as f:
        #w => siempre empiesa desde el principio
        # a => empesamos a agregar desde el final del ultimo contenido 
except Exception:
    print("Error")
finally:
    fichero.close()
    