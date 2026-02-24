def mover_punto(posicion_actual, desplazamiento):
    # posicion_actual es una tupla (x, y)
    nueva_x = posicion_actual[0] + desplazamiento[0]
    nueva_y = posicion_actual[1] + desplazamiento[1]
    return (nueva_x, nueva_y)

pos = (10, 5)
pos = mover_punto(pos, (2, 2)) # Resultado: (12, 7)