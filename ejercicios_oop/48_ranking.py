from datetime import datetime

class Ranking:
    def __init__(self):
        self.datos = {}
    
    def actualizar(self, jugador, puntos):
        if jugador in self.datos:
            self.datos[jugador]["puntos"] += puntos
            self.datos[jugador]["partidas"] += 1
        else:
            self.datos[jugador] = {"puntos": puntos, "partidas": 1, "fecha": datetime.now()}
    
    def top(self, n=3):
        return sorted(self.datos.items(), key=lambda x: x[1]["puntos"], reverse=True)[:n]
    
    def __str__(self):
        return f"{'Jugador':<12} {'Puntos':<10} {'Partidas':<10} {'Fecha'}\n" + \
               "\n".join(f"{j:<12} {d['puntos']:<10} {d['partidas']:<10} {d['fecha'].strftime('%Y-%m-%d')}" 
                        for j, d in self.datos.items())

r = Ranking()
r.actualizar("Alice", 100)
r.actualizar("Bob", 50)
r.actualizar("Alice", 75)
r.actualizar("Charlie", 120)

print(r)
print("\n=== Top 2 ===")
for j, d in r.top(2):
    print(f"{j}: {d['puntos']} puntos")
