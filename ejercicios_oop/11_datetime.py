from datetime import datetime, timedelta

class Tarea:
    def __init__(self, nombre, prioridad, fecha_limite=None):
        self.nombre = nombre
        self.prioridad = prioridad
        self.fecha_limite = fecha_limite or datetime.now() + timedelta(days=7)
        self.completada = False
    
    def __str__(self):
        estado = "✓" if self.completada else "✗"
        return f"[{estado}] {self.nombre} (Prioridad: {self.prioridad})"

class GestorTareas:
    def __init__(self):
        self.tareas = []
    
    def agregar(self, tarea):
        self.tareas.append(tarea)
    
    def listar(self):
        for t in sorted(self.tareas, key=lambda x: x.prioridad, reverse=True):
            print(t)
    
    def completar(self, nombre):
        for t in self.tareas:
            if t.nombre == nombre:
                t.completada = True

gt = GestorTareas()
gt.agregar(Tarea("Estudiar Python", 3))
gt.agregar(Tarea("Hacer ejercicio", 2))
gt.agregar(Tarea("Leer libro", 1))
gt.listar()
print("\n=== Completar 'Estudiar' ===")
gt.completar("Estudiar Python")
gt.listar()
