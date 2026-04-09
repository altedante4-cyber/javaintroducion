from collections import deque

class ColaAcciones:
    def __init__(self):
        self.cola = deque()
    
    def encolar(self, accion):
        self.cola.append(accion)
    
    def desencolar(self):
        return self.cola.popleft() if self.cola else None
    
    def __str__(self):
        return " -> ".join(self.cola)

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cola_acciones = ColaAcciones()
    
    def agregar_accion(self, accion):
        self.cola_acciones.encolar(accion)
    
    def ejecutar(self):
        while self.cola_acciones.cola:
            accion = self.cola_acciones.desencolar()
            print(f"{self.nombre}: {accion}")

j = Jugador("Heroe")
j.agregar_accion("Coger espada")
j.agregar_accion("Atacar goblin")
j.agregar_accion("Recoger tesoro")
j.ejecutar()
