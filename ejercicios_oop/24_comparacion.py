from datetime import date, timedelta

class Partida:
    def __init__(self, jugador, duracion_min):
        self.jugador = jugador
        self.duracion = duracion_min
        self.fecha = date.today()
    
    def __lt__(self, other):
        return self.duracion < other.duracion
    
    def __le__(self, other):
        return self.duracion <= other.duracion
    
    def __gt__(self, other):
        return self.duracion > other.duracion
    
    def __ge__(self, other):
        return self.duracion >= other.duracion
    
    def __eq__(self, other):
        return self.duracion == other.duracion
    
    def __str__(self):
        return f"{self.jugador}: {self.duracion} min"

partidas = [
    Partida("Alice", 30),
    Partida("Bob", 45),
    Partida("Charlie", 20)
]

print("=== Ordenadas por duración (menor a mayor) ===")
for p in sorted(partidas):
    print(p)

print(f"\n30 min == 30 min: {Partida('test', 30) == Partida('test2', 30)}")
