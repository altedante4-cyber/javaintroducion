
n = int(input()) 


    
tallas_disponible = list(map(int,input().split()))


inventorio = {}

for talla in tallas_disponible:

    if talla in inventorio:
        inventorio[talla]  += 1
    
    else:
        inventorio[talla] = 1

X = int(input())

ganancia = 0

# ... (código anterior sin cambios) ...

for i in range(X):

    linea_cliente = input().split()

    if len(linea_cliente) == 2 :

        talla_deseada = int(linea_cliente[0])
        precio  = int(linea_cliente[1])


        if talla_deseada in inventorio and inventorio[talla_deseada] > 0 :
            
            # 1. Reducir el stock
            inventorio[talla_deseada] -= 1
            
            # 2. SUMAR LA GANANCIA (¡Esta es la línea que faltaba!)
            ganancia += precio 

print(ganancia)