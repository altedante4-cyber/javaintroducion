# MAL: def mi_funcion(lista=[]): ... (la lista se queda guardada para siempre)

# BIEN: Usar una tupla o None
def procesar_configuracion(opciones=("verbo", "activo")):
    if "verbo" in opciones:
        print("Modo detallado activado")