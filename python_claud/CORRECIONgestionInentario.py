def estado_producto(stock , minimo  ):

    """ funcion auxiliar para determinarl el estado del producto"""

    if stock == 0 : return "SIN STOCK"
    if stock <=  minimo : return "BAJO"

    return "OK"

def agregar_stock(inventario , producto,cantidad):

    if producto in inventario:
        inventario[producto]['stock'] += cantidad 
    
    return False


def retirar_stock(inventario,producto,cantidad):
    if producto in inventario and inventario[producto]['stock'] >= cantidad :
        inventario[producto]['stock'] -= cantidad 
        return True 
    
    return  False 

def alertar_minimo(inventario):
    return [prod for prod , info in inventario.items() if info['stock'] <= info['minimo']]

def valor_total_inventario(inventario):
    #calculamos (precio * stock) por cada producto

    return sum(item['precio'] * item['stock'] for item  in inventario.values())

def mostrar_informe(inventario):
    print(f"{'Producto':<15} | {'Estado':<10} | {'Valor Total':<10}:")

    print("-"*40)

    for nombre , info in inventario.items():
        estado = estado_producto(info['stock'],info['minimo'])
        valor = info['stock'] * info['precio']
        print(f"{nombre:<15} | {estado:<10} | ${valor:>8.2f}")

    print(f"\nValor total del alamacen : ${valor_total_inventario(inventario):.2f}")
    