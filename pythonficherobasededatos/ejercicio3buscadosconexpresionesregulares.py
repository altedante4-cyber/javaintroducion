#buscar en "log.txt" todas las lineas que contengan una ip(formato 192.168.1.1) una fecha YYYY-MM-DD  y la palabra error
#guarda solo esas lineas en errore

import re

def extraer_errores_red(nombre_entrada , nombre_salida):
	""" Extre lineas con ip , fecha y erro """


	#patrones regex
	patron_ip = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'  # IP simple
    	patron_fecha = r'\d{4}-\d{2}-\d{2}'


	lineas_extraidas =  []

	try:
		with open(nombre_entrada , "r" , encoding="utf-8") as archivo:
			for num_lineas , linea in enumerate(archivo,1):
				#buscar ip , fecha y erro en la misma linea

				tiene_ip = re.search(patron_ip, linea)
				tiene_fecha = re.search(patron_fecha,linea)
				tiene_error= "Error" in linea

				if tiene_ip and tiene_fecha and tiene_error:
					lineas_extraidas.append(f"linea{num_linea}:{linea.strip()}")

	except FileNotFoundError:
		print(f"Error no existe {nombre_entrada}")
		return 
	except Exception as e :
		print(f"Error leyendo archivos :{e}")
		return

	#guardar resultado

	try:
		with open(nombre_salida,"w",encoding="utf-8") as salida:
			if lineas_extraidas:
				salida.write("\n".join(lineas_extraidas))

				print(f"se encontraron{len(lineas_extraidas)} errores de red")
				print(f"guadados en {nombre_salida}")
			else:
				salida.write("no se encontraron lineas con ip , fecha y error")
				print("no se encotraron coincidencias")

	except Exception as e:
		print(f"Error guardando archivo {e}")

#probar

extraer_errores_red("log.txt","errores_red.txt")
