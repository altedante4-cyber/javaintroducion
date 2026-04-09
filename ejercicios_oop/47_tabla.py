from datetime import datetime, timedelta

class Tabla:
    def __init__(self, columnas):
        self.columnas = columnas
        self.filas = []
    
    def agregar_fila(self, datos):
        if len(datos) != len(self.columnas):
            raise ValueError("Datos no coinciden con columnas")
        self.filas.append(datos)
    
    def __str__(self):
        widths = [max(len(str(row[i])) for row in [self.columnas] + self.filas) for i in range(len(self.columnas))]
        header = " | ".join(f"{self.columnas[i]:<{widths[i]}}" for i in range(len(self.columnas)))
        separator = "-+-".join("-" * w for w in widths)
        rows = "\n".join(" | ".join(f"{str(self.filas[r][c]):<{widths[c]}}" for c in range(len(self.columnas))) for r in range(len(self.filas)))
        return f"{header}\n{separator}\n{rows}"

class Ranking:
    def __init__(self):
        self.tabla = Tabla(["Jugador", "Puntos", "Fecha"])
    
    def agregar_puntuacion(self, jugador, puntos):
        fecha = datetime.now().strftime("%Y-%m-%d")
        self.tabla.agregar_fila([jugador, puntos, fecha])
    
    def mostrar(self):
        print(self.tabla)

r = Ranking()
r.agregar_puntuacion("Alice", 1500)
r.agregar_puntuacion("Bob", 1200)
r.agregar_puntuacion("Charlie", 1800)
r.mostrar()
