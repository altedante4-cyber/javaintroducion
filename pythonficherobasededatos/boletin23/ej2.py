def estadisticas(nombre_archivo):

	try:
		with open(nombre_archivo , "r" , encoding="utf-8") as fichero:
			guardar = fichero.readlines()


		lista_nueva =[]
		
		for i in guardar:

			for j in i.split("\n") :
				lista_nueva.append(j)
				
		
		lista = [x.strip() for x in lista_nueva  if x.strip() ]
		cont = 0 
		for i in lista:
		
			for j in i:
				if j == " ":
					cont += 1
					
		lineas_blanco = guardar.count("\n")
		numero_lineas = len(guardar)
		texto_completo = "".join(guardar)
		
		for i in "\n ,.":
			texto_completo = texto_completo.replace(i,"")

		print(f"Numero de lineas {numero_lineas}")
		print(f"Lineas en blanco: {lineas_blanco}")
		print(f"Cantidad de caracteres sin contar los espacios : {len(texto_completo)}")
		print(f"Cantidad de espacios: {cont}")

		
	except FileNotFoundError:
		print("EL archivo no existe")

	except Exception:
		print("Ocurrio un error inesperado")



estadisticas("ficheros1.txt")	
