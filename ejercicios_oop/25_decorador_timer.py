def timer(func):
    import time
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        print(f"{func.__name__} tardó {time.time() - inicio:.4f}s")
        return resultado
    return wrapper

@timer
def juego_lento():
    import random
    suma = sum(random.randint(1, 100) for _ in range(100000))
    return suma

@timer
def juego_rapido():
    return sum(range(1000))

print(juego_lento())
print(juego_rapido())
