def leer(nombre_archivo):
	with open(nombre_archivo , "r" , encoding="utf-8") as f:
		guardar = f.readlines()

	lista_nueva=[ x.split("\n") for x in guardar ]

	lista_limpiar =[]


	for i in lista_nueva:
		for k in i:
			lista_limpiar.append(k)


	k = [x.strip() for x in lista_limpiar if x.strip() ]

	list=[]
	for i in range(0,len(k),2):
		list.append(k[i:i+2])

	cont_h = 0
	cont_m=0
	promedio=0 		
	for i in list:
	    if i[0].lower() == "mujer":
	    	cont_m += 1
	    else:
	    	cont_h += 1
				
	for j in list:
		promedio += float(j[1])
	
	persona= cont_h + cont_m 
	print(f"Hombre:{cont_h}")
	print(f"Mujeres:{cont_m}")
	print(f"Estatura promedio { promedio / persona  }")		
		
leer("estadisticas.txt")

	
