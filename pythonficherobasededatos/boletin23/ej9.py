def validar(nombre_alchivo):
        #lectura limpia del archivo 

        separar ={}

        with open(nombre_alchivo,"r",encoding="utf-8" )as f :
                for linea in f:
                        if ":" in linea:
                             nombre , notas = linea.strip().split(":")

                             #convertimos directamente a lista de floats

                             separar[nombre] = [float(n) for n in notas.split(",")]

        
        lista_apro=[]
        lista_sus=[]
        nota_n={}

        #procesamiento principal(toto en un solo paso)

        for alumno , notas in separar.items():
            #verificamos si aprobo todo 

            if all(n >= 5 for n in notas ):
                   lista_apro.append(alumno)
            
            else:
                    lista_sus.append(alumno)


                    #buscamos los indices de los suspensos(RA)
                    #en lugar de 4 bucles usamos enumerate en una sola linea

                    indices_suspensos =[i for i , nota in enumerate(notas) if nota < 5]
                    nota_n[alumno]=indices_suspensos
    

        # 3. SALIDA DE DATOS
        print("--- Modulo: Redes ---")
        print("Alumnos/as con todo aprobado:")
        print("\n".join(lista_apro) if lista_apro else "Ninguno")
    
        print("\nDetalle de suspensos (Índices de RA):")
        print(nota_n)

validar("redes.txt")