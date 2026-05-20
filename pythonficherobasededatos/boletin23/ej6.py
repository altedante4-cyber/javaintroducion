class Persona:
		def __init__(self,nombre,apellido ,edad ):
				self.__nombre = nombre
				self.__apellido = apellido 
				self.__edad = edad  
		
		
		def __str__(self):
			return f"{self.__nombre} {self.__apellido} {self.__edad}"



lista_personas=[]
def leer(agenda):
	with open(agenda,"r",encoding="utf-8") as f :
		ej = f.readlines()

	limpiar= [x.split("\n") for x in ej ]
	
	limp=[]

	for i in limpiar:
		for j in i :
			limp.append(j)

	lip = [x.strip()  for x in limp if x.strip() ]
	nov = [x.split(",") for x in lip ]

	c =[]
	for i in nov:

		for j in i :
			a = j.split()

			if len(a) == 2:
					nom1 = a[0]
					nom2 = a[1]
					c.append(nom1+nom2)
			else:
					c.append(j)

	temp=[]

	cont = 0 

	for i in range(len(c)):

		temp.append(c[i])
		cont += 1

	
	
		if cont == 3:
			if temp[0].isalpha() and temp[1].isalpha() and temp[2].isdigit():
				p = Persona(temp[0],temp[1],temp[2])
				lista_personas.append(p)
			cont = 0
			temp.clear()


leer("agenda.txt")


for i in lista_personas:
	print(i.__str__())




