from datetime import time , datetime , date , timedelta 
def generar_recibo(nombre_coche , dias_alquiler):

    posicion = 0 
    for i in range(len(flota)):
        encontrado = False

        if nombre_coche == flota[i][0]:
            posicion = i 
            encontrado = True   
            break;

    if encontrado :
        
        precio_total = flota[posicion][3] * dias_alquiler 
        fecha_de_devolucion = datetime.now().date() + dias_alquiler  

        


def mostrar_inventario(lista_coches):

        print("-"*95)
        print(f"{'ESTADO DE LA FLOTA - ECORENT':<5} | {'Fecha: ':<5} {datetime.now().date()} | {'Hora':<5} {datetime.now().time()}")
        print("-"*95)
        print(f"{'MODELO':<20} | {'BATERIA':<5} | {'AUTONOMIA':<5} | {'PRECIO/DIA':<5} | {'ESTADO':<5}")
        print("-"*95)
        for i in range(len(flota)):
            print(f"{flota[i][0]:<20} | {flota[i][1]:<5}| {flota[i][2]:<5} | { flota[i][3]:<5} | {flota[i][4]:<5}")






flota = [
    ["Tesla Model 3", 85, 450, 55.50, 0],
    ["Renault Zoe", 40, 210, 25.00, 1],
    ["Hyundai Ioniq 5", 92, 480, 60.00, 0],
    ["Fiat 500e", 30, 150, 20.00, 0],
    ["Porsche Taycan", 75, 390, 120.00, 1]
    ]


mostrar_inventario(flota)