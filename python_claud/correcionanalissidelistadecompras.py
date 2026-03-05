def total_compra(productos:list):

    #forma pythoni sum() con un generador

    return sum(item['cantidad'] * item['precio'] for item in productos)
def aplicar_descuento(total: float , porcentaje:int ):
    #Es el mejor que esta funcion reciba el toat ya calculado

    if total > 50 :
        return total * (1- porcentaje / 100 )
    return total 

def prodcuto_mas_caro(productos:list ):
    #mas con key es la forma mas profesional de encontra un elemento en una lista de dicts
    if not productos : return None # es decir si esta vacia la lista  
    mas_caro = max(productos,key=lambda p:p['precio'])
    return mas_caro['producto']

#entrada de datos

lista_compras = []


for _ in range(2):
    nombre = input("Productos")
    cant = int(input("Cantidad"))
    prec = float(input("precio unitario"))

    lista_compras.append({

        "producto":nombre,
        "cantidad":cant,
        "precio":prec 
    })

#calculos
total_sin = total_compra(lista_compras)
total_con = aplicar_descuento(total_sin , 10 )
caro = prodcuto_mas_caro(lista_compras)

#ticket formateado

print("\n "+ "="*40 )
print(f"{'TICKET DE COMPRA':^40}")
print("="*40)
for p in lista_compras:
    subtotal = p['cantidad'] * p['precio']
    #usamos alineacion < (izquierda)

    print(f"{p['producto']:<15} x{p['cantidad']:>2} {p['precio']:>10.2f}Eur | Sub: {subtotal:>8.2f}Eur")

print("-"*40)
print(f"{'TOTAL (sin desc): ':<25} {total_sin:>12.2f}Eur")

if total_sin > 50 :
    print(f"{'TOTAL CON DTO. 10% ':<25} {total_con:12.2f}Eu")

print(f"\nProducto estrella (mas caro) {caro.upper()}")
print("="*40)