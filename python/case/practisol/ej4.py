#4. Selección Aleatoria de Ganador 🎉
#Tienes una lista de 10 nombres. Usa random.choice() para seleccionar e imprimir dos ganadores diferentes de la lista (asegúrate de que el segundo ganador no sea el mismo que el primero).
#
#
import random 
nombres = ['michael','daniela','jandira','cadmel','rose','maite','sara','raquel','osvaldo','belen','camila']

primter_ganador = random.choice(nombres)

print("primer ganador" , primter_ganador)



#elegir un segundo ganador diferentes
#la manera mas simple es usar un bucle while hasta que se seleccione un nombre distinto

segundo_ganador = random.choice(nombres)



while segundo_ganador == primter_ganador:

    segundo_ganador = random.choice(nombres)

print("segundo ganador" , segundo_ganador)
