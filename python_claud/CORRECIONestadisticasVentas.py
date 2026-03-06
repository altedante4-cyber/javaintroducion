import random

#definimos los mese de forma clara
MESES = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", 
         "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]


#generamos datos (sin cambios esto esta bien)

datos_ventas ={f'Producto{chr(65+i)}' : [random.randint(50,250)  for _ in range(12)] for i in range(12)}

def mejor_mes(datos):
    #usamos comprension de dicicionario y el metodo index()
    return {prod:MESES[ventas.index(max(ventas))] for prod , ventas in datos.items()}

def producto_estrella(datos):
    #en lugar de crear una lista de diccionarios , buscamos directamente
    #max() con un key personlaizado sobre los items del diccionarios

    return max(datos.items()  , key= lambda item: sum(item[1]))

def mes_mas_rentable(datos):
    #calculamos el total por mes sumando las columnas
    totales_mes = [sum(mes) for mes in zip(*datos.values())]
    return MESES[totales_mes.index(max(totales_mes))]

#jeecucin y reporte

print("Mejor mes por producto:", mejor_mes(datos_ventas))
print("Producto Estrella:", producto_estrella(datos_ventas)[0])
print("Mes más rentable:", mes_mas_rentable(datos_ventas))

print("-" * 40)
print("RANKING DE VENTAS")

ranking = sorted([(sum(v),k)for k , v in datos_ventas.items()] , reverse=True )
for total , prod in ranking:
    print(f"{prod}: {total}")

print("-"*40)
print("Analisis de tendencia")

for prod,ventas in datos_ventas.items():
    primera = sum(ventas[:6])
    segunda = sum(ventas[6:])

    tendencias = "Negativa" if primera > segunda else "Estable/Positiva"
    print(f"{prod:12} | Tendencia: {tendencias}")


# Eliminacion de estructuras intermedias en producto_estrella no hace falta crear una lista de diccionarios [{'clave}]
#puedes operar directamen sobre lso items() del diccionario usando max(datos.items() , key=lambda item sum(item[1])) esto ahorra mucha memoria
#zip(*datos.values()) esta es la tecnica secreta en python para trbaajar con matrices
# al hacer zip(*datos.values()) conviertes las filas(productos ) en columnas (meses)esto permite sumar los meses de todos lso porducto en una sola linea
#3.comprension de listas/diccionarios he reemplazado los bucles  for que solo servian para llenar listas vacias (lista.append(..)) por compresiones son mas rapida y legible
#limpiesa de l informr en lugar de print(*)
#5.correcion de mejor_mes he quitado el match case gigante como tiene una lista con los nombre de los meses (MESES) simplemente acede por indice 
#no te repitas(DRY) siempre que veas un case muy largo o un if con mcahs condiciones es senal de que deberis usar una estructura de datos(como lista mese ) para buscar el valor en lugar de logica de control

