from datetime import datetime

class Partida:
    def __init__(self, jugador, duracion):
        self.jugador = jugador
        self.duracion = duracion
        self.fecha = datetime.now()
    
    def __str__(self):
        return f"{self.jugador} - {self.duracion}min - {self.fecha.strftime('%H:%M:%S')}"

class Estadisticas:
    def __init__(self):
        self.partidas = []
    
    def agregar_partida(self, partida):
        self.partidas.append(partida)
    
    def calcular_estadisticas(self):
        if not self.partidas:
            return {"total": 0, "media": 0, "max": 0, "min": 0}
        
        duraciones = [p.duracion for p in self.partidas]
        return {
            "total": len(self.partidas),
            "media": sum(duraciones) / len(duraciones),
            "max": max(duraciones),
            "min": min(duraciones),
            "total_tiempo": sum(duraciones)
        }
    
    def filtrar_jugador(self, jugador):
        return [p for p in self.partidas if p.jugador == jugador]
    
    def __str__(self):
        stats = self.calcular_estadisticas()
        return f"""
=== ESTADÍSTICAS ===
Partidas jugadas: {stats['total']}
Tiempo medio: {stats['media']:.1f} min
Partida más larga: {stats['max']} min
Partida más corta: {stats['min']} min
Tiempo total: {stats['total_tiempo']} min
"""

e = Estadisticas()
e.agregar_partida(Partida("Alice", 30))
e.agregar_partida(Partida("Bob", 45))
e.agregar_partida(Partida("Alice", 20))
e.agregar_partida(Partida("Charlie", 60))

print(e)
print("=== Partidas de Alice ===")
for p in e.filtrar_jugador("Alice"):
    print(p)
