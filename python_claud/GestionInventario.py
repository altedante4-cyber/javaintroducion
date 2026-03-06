def agregar_stock(inventario , producto,cantidad):
    #return  inventario[producto]['stock'] += cantidad    
    #no lo de arriba
    # en python no se peude usar += dentro de unr eturn 
    #proque += es una asignacion no una expresion que devuevla un valor 
    inventario[producto]['stock'] += cantidad 
    return inventario 

def retirar_stock(inventario,producto,cantidad):

    #que reste solo si hay suficiente 

    if cantidad < 0 :
        return 

    inventario[producto]['stock'] -=cantidad
    
    return inventario 

def alertas_minimo(inventario):

    #devuelva una lista de productos bajo el minimo
    
    for clave , valor in inventario.items():

            if valor['minimo'] < 50 :
                 print(f" {clave} |  {valor['minimo']}")

def valor_total_inventario(inventario):
    #calcule el valor economico total
    
    total = sum([i['precio'] for clave , i in inventario.items() ])         

    print(total)

def mostrar_informe_estado(inventario):
     
     for clave , valor in inventario.items():
          
          if valor['stock'] == 0 :
               print("SIN STOCK")
          elif  valor['stock'] <= valor['minimo']:
               print("BAJO")
          else:
               print("OK")
          
inventario = {
    'Tornillo': {'stock':150, 'minimo':50, 'precio':0.10},
    'Martillo': {'stock':200, 'minimo':20, 'precio':20},
    'Tuerca': {'stock':300, 'minimo':60, 'precio':0.05},
    'Clavo': {'stock':500, 'minimo':100, 'precio':0.03},
    'Destornillador': {'stock':80, 'minimo':15, 'precio':8},
    'Alicate': {'stock':60, 'minimo':10, 'precio':12},
    'Serrucho': {'stock':40, 'minimo':8, 'precio':15},
    'Taladro': {'stock':25, 'minimo':5, 'precio':75},
    'Llave inglesa': {'stock':50, 'minimo':10, 'precio':18},
    'Cinta métrica': {'stock':90, 'minimo':20, 'precio':6}
}


if(agregar_stock(inventario,'Clavo',20)):
    print("agregado correctamente")
else:
    print("no se ha agregado")


alertas_minimo(inventario)

valor_total_inventario(inventario)

mostrar_informe_estado(inventario)