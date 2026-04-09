from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(self, nombre, nivel=1):
        self.nombre = nombre
        self.nivel = nivel
        self.salud = 100
    
    @abstractmethod
    def accion_especial(self) -> str:
        pass
    
    def __str__(self):
        return f"{self.nombre} - Nivel: {self.nivel} - Salud: {self.salud}"

class Mago(Personaje):
    def accion_especial(self):
        return f"{self.nombre} lanza bola de fuego"

class Guerrero(Personaje):
    def accion_especial(self):
        return f"{self.nombre} ejecuta corte doble"

personajes = [Mago("Gandalf", 10), Guerrero("Conan", 8)]
for p in personajes:
    print(p)
    print(p.accion_especial())
