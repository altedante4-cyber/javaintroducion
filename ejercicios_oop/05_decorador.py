def decorador_log(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Ejecutando: {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f"[LOG] Finalizado: {func.__name__}")
        return resultado
    return wrapper

@decorador_log
def calcular_area(radio):
    return 3.14159 * radio ** 2

@decorador_log
def saludar(nombre):
    return f"Hola {nombre}"

print(calcular_area(5))
print(saludar("Mario"))
