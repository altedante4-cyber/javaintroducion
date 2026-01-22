#7GENERADOR DE MATRICULAS ALEATORIAS
#Genera una matrícula de coche ficticia con el formato "LL NNN LL" (L=Letra, N=Número). Las letras deben ser mayúsculas aleatorias y los números deben ser dígitos aleatorios del 0 al 9. Usa random.choice() o random.randint() según sea apropiado.

import random


#Generado de maticuals "LL NNN LL"

#formato:
# L = letra mayuscula aleatoria
# N = numero del 0 al 9

#Paso 1 Objetivo final

#pregunta clave
#Que quiero que haga el progrma
#Respuesta => Generar y mostrar una matricula aleatoria con ese formato

#Paso2 Indentificar tareas grandes
#piensa en grandes acciones que necesita hacer el progrma 
#Elegir letras aleatorias
#Elegir numeros aleatorios
#combinar letras y numeros en formato correcto
#mostrar la matricula

#paso3 dividir en subproblemas concretos
#subproblema 1 ==> letras iniciales 
#elegir 2 letras mayusculas aleatorias para el inicio
#preguntas
#como representa las letras
#como selecciona una letra al azar

#subproblema numeros del medio
#elegir 3 digitos aleatorias (0=9)
#preguntas
#como genro numeros al azar
#como los uno para formar 3 digitos juntos

#subproblema 3 letras finales
#elegir 2 letras mayusculas aleatorias para el final
#similar al subproblema 1

#subproblema 4 combinar todo
#unir las letras iniciales,los numeros y las letras finales en el fomrato LL NN LL
#pregunta
#como agrego espacios entre los grupos

#subproblema 5 mostrar el resultado 
#impoirmir la matricula generasda

letras = ['A','E','I','O','U','Q','R','T']

selecion = random.sample(letras ,2 )

namber = ""
for i in range(3):
    numeros = random.randint(0,9)

    namber += str(numeros)


final = random.sample(letras,2)


formato_leter = "".join(x  for x in selecion)
formato_leter_final = "".join(x for x in final)


print(f"{formato_leter} {namber}  {formato_leter_final}")
