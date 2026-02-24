def valida_factura(num:int):
     
    for i in valores.keys():
          
          if i == num:
               return True
    
    return False 
terminado = False

recaudado = 0 
pendiente_cobro = 0 
valores = {}

while not terminado :

    print(f"Recaudado : {recaudado} ")
    print(f"Pendiente de cobro : {pendiente_cobro} ")

    opcion = input("Quiere anadir una opcion nueva factura (A) , pagarla(P) o terminar (T)? ")
    existe = False  
    match(opcion):
          
        case 'A':
                factura = int(input("Introduce el numero e la factura  "))
                if(valida_factura(factura)):
                    print("Ya existe factura")                    
                
                if(not valida_factura(factura)):
                    coste = float(input("Introduce el coste de la factura "))
                 
                    pendiente_cobro += coste 
                    valores[factura] = coste 
                
                


        case 'P':
            encontrado = False 
            pagar = int(input("Introduce el numero de factura a pagar "))
            
            if valida_factura(pagar):
                 del valores[pagar]
                 recaudado += pendiente_cobro 
                 pendiente_cobro = 0 
                 print("Factura pagada ")
            else:
                 print("No existe esa factura")
        case 'T':
            terminado  = True 
    

