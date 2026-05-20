#lee el archivo texto.txt cuenta cuantas palabras tiene muestra las 5 palabras mas largas  maneja que el archivo no exista
def analizar_texto(nombre_archivo):
	"cuenta palarbas y muestras las 5 mas largas"
	try:
		with open(nombre_archivo , "r" , encoding="utf-8") as archivo:
			contenido = archivo.read()


	
		#limpiar y separar palabras

		#reemplazar signos de puntuacion por espacios

		for signo in ".,!?;:()\"'":
			contenido = contenido.replace(signo," ")


		palabras = contenido.split() #separa por espacios

	
		if not palabras:
			print("el archivo esta vacio")
			return

		#ordenar por longitud ( de mayor a menor)

		palabras_ordenadas = sorted(palabras, key=len, reverse=True)
		palabras_largas = palabras_ordenadas[:5]

		print(f"total de palarbas:{len(palabras)}")

	except FileNotFoundError:
		print(f"Error:No se encontro el archivo '{nombre_archivo}'")

	except Exception as e:
		print(f"Error inesperado {e}")

	#escribir el resultado en un archivo 

	try:
		with open("mio.txt" , "w" , encoding="utf-8" ) as mioarchivo:
			mioarchivo.write("\n".join(palabras_largas))

	except Exception as e:
		print("NO se pudo agregar")
	

#probar

analizar_texto("texto.txt") 


