from abc import ABC, abstractmethod

class Habilidad(ABC):
    @abstractmethod
    def usar(self, usuario, objetivo):
        pass

class Fuego(Habilidad):
    def usar(self, usuario, objetivo):
        return f"{usuario} lanza fuego a {objetivo} (30 dmg)"

class Hielo(Habilidad):
    def usar(self, usuario, objetivo):
        return f"{usuario} lanza hielo a {objetivo} (25 dmg)"

class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habilidades = []
    
    def agregar_habilidad(self, habilidad):
        self.habilidades.append(habilidad)
    
    def usar_habilidad(self, indice, objetivo):
        if 0 <= indice < len(self.habilidades):
            return self.habilidades[indice].usar(self.nombre, objetivo)
        return "Habilidad no encontrada"

p = Personaje("Mago")
p.agregar_habilidad(Fuego())
p.agregar_habilidad(Hielo())

print(p.usar_habilidad(0, "Dragón"))
print(p.usar_habilidad(1, "Goblin"))
