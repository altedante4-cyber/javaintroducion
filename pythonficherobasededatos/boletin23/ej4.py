def compararFicheros(fichero1,fichero2):

	#tiene la misma longitud
	#tiene las misma palabras

	try:
		with open(fichero1 , "r" , encoding="utf-8") as fi1 , open(fichero2,"r" , encoding="utf-8")  as fi2:
			return fi1.read() == fi2.read()
			
	except FileNotFoundError:
		print("Uno de los archivos no existe")
		


if compararFicheros("fichero1.txt" , "fichero2.txt"):
	print("El contenido de los fichero es el mismo")
else:
	print("EL contenido de los ficheros no es el mismo")

	
