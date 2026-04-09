from dataclasses import dataclass, field

@dataclass
class Jugador:
    nombre: str
    nivel: int = 1
    salud: int = 100
    inventario: list = field(default_factory=list)
    
    def __str__(self):
        return f"{self.nombre} - Nivel {self.nivel} - Salud {self.salud}"

@dataclass
class Mision:
    nombre: str
    recompensa: int
    completada: bool = False

j = Jugador("Héroe", inventario=["espada", "escudo"])
print(j)
print(f"Inventario: {j.inventario}")

m = Mision("Derrotar dragón", 500)
print(m)
