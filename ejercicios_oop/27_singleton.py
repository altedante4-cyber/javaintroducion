class SingletonMeta(type):
    _instancias = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instancias:
            cls._instancias[cls] = super().__call__(*args, **kwargs)
        return cls._instancias[cls]

class Configuracion(metaclass=SingletonMeta):
    def __init__(self):
        self.juego = "RPG"
        self.dificultad = "normal"
    
    def __str__(self):
        return f"Juego: {self.juego}, Dificultad: {self.dificultad}"

c1 = Configuracion()
c2 = Configuracion()
c1.dificultad = "dificil"

print(f"c1: {c1}")
print(f"c2: {c2}")
print(f"¿Son la misma instancia?: {c1 is c2}")
