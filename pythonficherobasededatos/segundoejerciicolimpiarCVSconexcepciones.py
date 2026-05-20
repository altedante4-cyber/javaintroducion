#lee datos.csv donde cada linea tiene nombre,edad si edad no es numero escribe esa linea en errores.log Escribe en mayores.txt
#los nombre de quiernes tienen >= 18 años 

def procesar_csv(nombre_entrada,nombre_salida,nombre_log):
	"""separ mayores de edad y registra errore"""

	try:
		with open(nombre_entrada ,"r", encoding="utf-8") as entrada:
			lineas = entrada.readlines()


			for i in lineas:
				print(i) 

	except FileNotFoundError:
		print(f"no se encuentra{nombre_entrada}")

		return 

	mayores = []
	menores = []

	for num_linea,linea in enumerate(lineas,1):
		linea = linea.strip()


		if not linea: #saltar lineas vacias
			continue

		partes = linea.split(",")

		if len(partes) != 2 :
			errores.append(f"lineas{num_linea}: Formato invalido > {linea}")
			continue

		nombre,edad_str = partes[0].strip(),partes[1].strip()


		try:
			edad = int(edad_str)

			if edad >= 18:
				mayores.append(f"{nombre} - {edad} años")

		except ValueError:
			errores.append(f"linea{num_linea} edad no numerica {edad_str}' > {linea}")


	#escribir la salida

	try:
		with open(nombre_salida ,"w",encoding="utf-8") as salida:
			salida.write("\n".join(mayores))

		with open(nombre_log,"w",encoding="utf-8") as log:
			if errores:
				log.write("\n".join(errores))
			else:
				log.write("no se encontraron errores")

		print(f"{len(mayores)} mayores de edad guardados en {nombre_salida}")
		print(f"{len(errores)} errores registrados en {nombre_log}'")

	except Exception as e:
		print(f"Error al escribir archivos : {e}")


#probar 

procesar_csv("datos.csv","mayores.txt","errores.log")


