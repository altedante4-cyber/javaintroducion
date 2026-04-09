from datetime import datetime, timedelta

class Partido:
    def __init__(self, equipo_local, equipo_visitante, fecha):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.fecha = fecha
        self.goles_local = 0
        self.goles_visitante = 0
    
    def __lt__(self, other):
        return self.fecha < other.fecha
    
    def __str__(self):
        return f"{self.equipo_local} {self.goles_local} - {self.goles_visitante} {self.equipo_visitante} | {self.fecha.strftime('%d/%m')}"

partidos = [
   Partido("Madrid", "Barcelona", datetime(2026, 5, 1)),
    Partido("Sevilla", "Valencia", datetime(2026, 5, 3)),
    Partido("Barcelona", "Sevilla", datetime(2026, 5, 5)),
]

for p in sorted(partidos):
    print(p)
