class Jugador:
    def __init__(self, nombre, puntuaciones):
        self.nombre = nombre
        self.puntuaciones = puntuaciones
    
    @property
    def mejor_puntuacion(self):
        return max(self.puntuaciones)
    
    @property
    def promedio(self):
        return sum(self.puntuaciones) / len(self.puntuaciones)

class GestorJugadores:
    @classmethod
    def mejores_puntuaciones(cls, jugadores, top=3):
        return sorted(jugadores, key=lambda j: j.mejor_puntuacion, reverse=True)[:top]
    
    @classmethod
    def promedio_mas_alto(cls, jugadores):
        return max(jugadores, key=lambda j: j.promedio)

jugadores = [
    Jugador("Alice", [100, 90, 85]),
    Jugador("Bob", [95, 100, 80]),
    Jugador("Charlie", [70, 75, 90])
]

print("=== Top 3 mejores puntuaciones ===")
for j in GestorJugadores.mejores_puntuaciones(jugadores):
    print(f"{j.nombre}: {j.mejor_puntuacion}")

print(f"\nMejor promedio: {GestorJugadores.promedio_mas_alto(jugadores).nombre}")
