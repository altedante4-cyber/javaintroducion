
pedir_id = input("Introduce IDs de transaccion").split(",")

lista_id_enteros = []

for i in pedir_id:
    lista_id_enteros.append(int(i))



contador = 0

lista_seter = set()
for i in lista_id_enteros:

    if i not in lista_seter:
        lista_seter.add(i)
    else:
        contador += 1

#covertir a tuple para devovlerlo

lsita_tuple = tuple(lista_seter)

print(f"IDs unicos: {lsita_tuple}")
print(f"Duplicados eliminados : {contador}")

#aqui aprende que si le pasan una lista de numeros primer
#convertimos  la nerada del usuario a  una lista  luego
# hacemos un bucle for para iterar sobre esa lista he ir comparadno con la lista
#seter para ver si esta o no en l alista si esta  el contador se incrrementa
# sin el numero no esta el cojntador no se incrementa pero el numero se anadde
#por ultimo para mosttarr convertimos en tuple

