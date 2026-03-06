import random 
# def mejor_mes(ventas_producto):
#     #que devuelva el mes con mas ventas(1-12)
#     #mejor se refiere que tenemos que recorrer todos los array y quedarnos con el maximo de cada uno para luego mostrar
#     mejor_ventas_producto = []

#     for posicion , valor_producto_maximo in enumerate(ventas_producto.values()):

#         mejor_ventas_producto.append({
            
#             'valor':max(valor_producto_maximo),
#             'posicion': posicion 

#         }
#         )        

#     #LA unica menra que se esta ocurriendo es agrupando en un nuevo diccionario con clave y valor de mes 
#     #tengo los maximo de cada y su posicion que seria el mes entonces la clave serira el producto y el valor seria el mes 

#     dicionario_mostrar = {}
#     for i in mejor_ventas_producto:

#         match i['posicion']:

#             case 0:
#                 dicionario_mostrar[0]="ENERO"

#             case 1 :
#                 dicionario_mostrar[1]="FEBRERO"
            
#             case 2 :
#                 dicionario_mostrar[2]="MARZO"
            
#             case 3 :
#                 dicionario_mostrar[3]="ABRIL"
            
#             case 4 :
#                 dicionario_mostrar[4]="MAYO"
            
#             case 5 :
#                 dicionario_mostrar[5]="JUNIO"
            
#             case 6 :
#                 dicionario_mostrar[6]="JULIO"

#             case 7 :
#                 dicionario_mostrar[7]="AGOSTO"
           
#             case 8 :
#                 dicionario_mostrar[8]="SEPTIEMBRE"
            
#             case 9 :
#                 dicionario_mostrar[9]="OPTUBRE"
            
#             case 10 :
#                 dicionario_mostrar[10]="NOVIEMBRE"
            
#             case 11 :
#                 dicionario_mostrar[11]="DICIEMBRE"

#     #ya tenemso el diicionario a mostrar  ahora solo tenemos que agregarle el producto que le correcponende

#     for i in ventas_producto.keys():
#         nueva_clave = i.upper()
#         dicionario_mostrar[nueva_clave] =ventas_producto[i]

#     return dicionario_mostrar

# CODIGO CON IA
def mejor_mes(ventas_producto):
    meses = [
        "ENERO","FEBRERO","MARZO","ABRIL","ABIRL","MAYO","JUNIO","JULIO",
        "AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE"
    ]
    diccionario_mostrar = {}

    for producto , ventas in ventas_producto.items():
        posicion_mes = ventas.index(max(ventas)) #posicion del maximo
        mes = meses[posicion_mes]
        diccionario_mostrar[producto.upper()] = mes 
    
    return diccionario_mostrar 

def producto_estrella(datos):
    #que devuelva el producto con mayor total anual 
    
    lista_suma_valores = []


    for clave , valores in datos.items():
        lista_suma_valores.append({
            'clave': clave ,
            'suma': sum(valores)
        })

    sacar_maximo = max(lista_suma_valores , key=lambda x: x['suma']) #aprenderse siempre esto 

    return sacar_maximo 
    





def mes_mas_rentable(datos):
    lista_suma_valores = []


    for i in datos.values():
        lista_suma_valores.append(max(i))

    #devuelve el mes que mas factura por ende tenemos que saber la posicion de cada uno 
    return  max(lista_suma_valores)
    
    
#generar diciconarios con valores aleatorios 

datos_ventas = {
    'Producto A': [random.randint(50, 250) for _ in range(12 )],
    'Producto B': [random.randint(50, 250) for _ in range(12 )],
    'Producto C': [random.randint(50, 250) for _ in range(12 )],
    'Producto D': [random.randint(50, 250) for _ in range(12 )],
    'Producto E': [random.randint(50, 250) for _ in range(12 )],
    'Producto F': [random.randint(50, 250) for _ in range(12 )],
    'Producto G': [random.randint(50, 250) for _ in range(12  )],
    'Producto H': [random.randint(50, 250) for _ in range(12 )],
    'Producto I': [random.randint(50, 250) for _ in range(12)],
    'Producto J': [random.randint(50, 250) for _ in range(12)],
    'Producto K': [random.randint(50, 250) for _ in range(12)],
    'Producto L': [random.randint(50, 250) for _ in range(12)]
}


print(mejor_mes(datos_ventas))

print(producto_estrella(datos_ventas))

print(mes_mas_rentable(datos_ventas))

print("*"*40)
print("INFORME RANKIN DE PRODUCTO POR VENTAS TOTALES ") # es decir los producto que tubierona mayor venta 
lista_ventas_totales_productos = []

for clave , valor  in datos_ventas.items():
    lista_ventas_totales_productos.append({
         "producto":clave,
         "total" : sum(valor)


    }
    )

ordenado = sorted(lista_ventas_totales_productos , key=lambda x: x["total"] , reverse=True) #APRENDERSE ESTE PATORN 


for i in ordenado:
    print(f"{i['producto']} | {i['total']}")


print("*"*40)
print("DETECTAR PRODUCTOS CON TENDENCIA NEGATIVA ")

for clave , valor in datos_ventas.items():

        primera_parte = sum(valor[:6])
        segunda_parte = sum(valor[6:])

        if primera_parte > segunda_parte:
            print(f"tiene tendencia negatica {clave} | {valor}")

        else:
            print(f"No tiene tendencia negativa {clave} | {valor}")
            