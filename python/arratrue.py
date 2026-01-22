

estudiantes = []


for _ in range(int(input())):
            name = input()
            score = float(input())

            estudiantes.append(name)
            estudiantes.append(score)





notas = [x for x in estudiantes if isinstance(x , float)]


ordenados = sorted(notas)


min1 = ordenados[1]
print(min1)

min2 = ordenados[2]
print(min2)

nombres_estudiantes = []

for i in range(0,len(estudiantes),2 ):
        
        nombre = estudiantes[i]
        notas = estudiantes[i + 1]

        if notas == min1 :
                nombres_estudiantes.append(nombre)
        
        elif notas == min2:
                nombres_estudiantes.append(nombre)



        

for n in sorted(nombres_estudiantes):
        print(n)

        






        

                
                










