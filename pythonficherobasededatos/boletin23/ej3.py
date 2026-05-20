def contar(nombre_fichero):
	try:
		with open(nombre_fichero , "r", encoding="utf-8" ) as fichero:
			a =  fichero.readlines()


		x = [ x.split() for x in a ]

		lista = []
		
		for i in x:
			for k in i :
				lista.append(k)
				
		print(len(lista))		
			
	except Exception as e:
		print("Error hubo un errror")
		
	 

contar("datos.txt")
