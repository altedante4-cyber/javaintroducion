lenguaje = "python"
alumno = "pepe"
edad = 24

print("HOla", "me llamo" , alumno , "tengo",edad, "anios y estoy estudiando" , lenguaje)

print("HOla", "me llamo %s tengo %d anios y estoy estudiando %s " %(alumno, edad, lenguaje))



# %s => es un string
# %d => es un entero
# %f => float

print(f"Hola , me llamo {alumno} tengo {edad} anios y estoy  estudiando {lenguaje}")

#nos permite  tabular los numeros tambien nos permite anadir decimales a los numeros
n1 = 34.567
n2 = 1234.55678
print(f"Los numeros son {n1:.2f} y {n2:.2f}")

# en el caso que el nuemero no tengo decimales  les agrega dos ceros

n3 = 34
print(f"Los numeros son {n3:.2f} y {n2:.2f}")


#nos permite calcular por centaje automaticamente de la siguiente manera

n4 = 0.34
n2= 0.55555678
print(f"Los numeros son {n4:.2%} y {n2:.2%}")

poblacion = 7854876213
print(f"la poblacion del pais es de {poblacion:,} habitantes")
lista = [234,45,765,6,562,33,1245,56]

for n in lista:
    print(f"{n:5d}") # lo que hace es tabular  pero tenemos que poner la longitud mayor que el numero mas grande que  el numero que tiene mayor longitud  es decir el 1234 es de mayor longitud y tenemos que ponerlo


# SI TUVIERAMOS DECIRMALES EN NUESTRA LISTA ALO HARIAMOS DE LA SIGUIENTE MANERA
lista = [234,45.55,765,6.1,562,33.134,1245,56.1234]

for n in lista:
    print(f"{n:7.2f}")  # es el 7 es el total de la cadena del numero   y el 2 es la parte decirma y   por eemplo 1245,56  en total son  7 y  tiene dos decimales


# tambien tiene la funcion de formateo  de textoo

print(f"A la izquiierda: *** {lenguaje:<20}***") # se le van a dedicfar veite espacios y se le va a formatear a la izquierda
print(f"A la derecha: *** {lenguaje:>20}---") # se le van a dedicfar veite espacios y se le va a formatear a la izquierda
print(f"AL centro : *** {lenguaje:^20}***") # se le van a dedicfar veite espacios y se le va a formatear a la izquierda


nombre = "Michael Axel"
apellido = "Aguiar Peredo"
telefono = 494585
libro = "El hobbit"
fechaDevolucion = "12/03/2026"

fechaLibro = f"""
Nombre : {nombre}
Apellido : {apellido}
Telefono : {telefono}
Libro : {libro} - Fecha de devolucion: {fechaDevolucion}

"""

print(fechaLibro)

Libro : {{{libro}}} - Fecha de devolucion: {fechaDevolucion} # triple llave para ver las llaves dentro de la varaibel

