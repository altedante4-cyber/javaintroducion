def primera(nombre_fichero,caracter):
	""" lineas fichero , cuantas veces aparece el caracter"""

	try:
		with open(nombre_fichero,"r" , encoding="utf-8") as fichero:
			guardar = fichero.readlines()
	
		nuevo = "\n".join(guardar)

		print(f"El fichero tiene {len(guardar)} lineas")
		print(f"La palabra {caracter} aparece {nuevo.count(caracter)} veces" )
		
	except FileNotFoundError:
		print(f"El fichero {nombre_fichero} no existe")

	except Exception:
		print("Ocurrio un erro")



user = input("Ingrese el nombre fichero")
user_cara= input("ingrese el caracter a buscar")


primera(user,user_cara)
