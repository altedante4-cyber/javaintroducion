from datetime import datetime, timedelta

def ejercicio_1():
    """Taller de coches: Registro y 6 revisiones cada 200 días."""
    print("\n--- Ejercicio 1: Taller de Coches ---")
    
    # Tomamos la fecha y hora actual
    ahora = datetime.now()
    
    # Formateamos la salida inicial según el ejemplo
    # El ejemplo dice: "4 del 02 de 2026 a las 17:47"
    # %d del %m de %Y a las %H:%M
    print(f"Registro y primera cita: {ahora.strftime('%-d del %m de %Y a las %H:%M')}")
    print("Siguientes citas:")
    
    intervalo = timedelta(days=200)
    fecha_cita = ahora
    
    for i in range(1, 7):
        fecha_cita += intervalo
        # El ejemplo muestra formatos variados (algunos con del, otros con /)
        # Vamos a usar un formato consistente como el del ejemplo: "23 del 08 de 2026"
        print(f"{i} - {fecha_cita.strftime('%-d del %m de %Y')}")

def ejercicio_2_y_3():
    """Manejo de fechas en listas, validación con excepciones y comparación con hoy."""
    print("\n--- Ejercicio 2 y 3: Validación y Comparación de Fechas ---")
    
    lista_cadenas = ["13/02/25", "hola carmela", "12 34 56", "14/06/2026", "bra, bra", "56/13/26"]
    
    # Formatos posibles según el enunciado (dd/mm/yy y dd/mm/YYYY)
    formatos = ["%d/%m/%y", "%d/%m/%Y"]
    
    fechas_correctas_anteriores = []
    fechas_correctas_posteriores = []
    fechas_incorrectas = []
    
    hoy = datetime.now()
    
    for cadena in lista_cadenas:
        fecha_objeto = None
        # Intentamos parsear con cada formato posible
        for fmt in formatos:
            try:
                fecha_objeto = datetime.strptime(cadena, fmt)
                # Si llegamos aquí, el parseo fue exitoso
                break 
            except ValueError:
                continue
        
        if fecha_objeto:
            # Ejercicio 3: Separar por anteriores/posteriores a hoy
            if fecha_objeto < hoy:
                fechas_correctas_anteriores.append(cadena)
            else:
                fechas_correctas_posteriores.append(cadena)
        else:
            # Ejercicio 2: Incorrectas
            fechas_incorrectas.append(cadena)
            
    # Salida Ejercicio 2
    print("\n[Ejercicio 2] Clasificación por validez:")
    print("Fechas correctas:")
    for f in (fechas_correctas_anteriores + fechas_correctas_posteriores):
        print(f'"{f}"')
    
    print("\nFechas incorrectas:")
    for f in fechas_incorrectas:
        print(f'"{f}"')
        
    # Salida Ejercicio 3
    print("\n[Ejercicio 3] Clasificación por comparación con hoy:")
    print("Fechas correctas ANTERIORES a hoy:")
    for f in fechas_correctas_anteriores:
        print(f'"{f}"')
        
    print("\nFechas correctas POSTERIORES a hoy:")
    for f in fechas_correctas_posteriores:
        print(f'"{f}"')

def main():
    ejercicio_1()
    ejercicio_2_y_3()

if __name__ == "__main__":
    main()
