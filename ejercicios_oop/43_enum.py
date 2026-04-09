from enum import Enum, auto

class TipoArma(Enum):
    ESPADA = auto()
    ARCO = auto()
    BACULO = auto()
    HACHA = auto()

class Arma:
    def __init__(self, nombre, tipo, dano):
        self.nombre = nombre
        self.tipo = tipo
        self.dano = dano
    
    def __str__(self):
        return f"{self.nombre} ({self.tipo.name}) - Daño: {self.dano}"

armas = [
    Arma("Excalibur", TipoArma.ESPADA, 50),
    Arma("Arco Largo", TipoArma.ARCO, 30),
    Arma("Varita", TipoArma.BACULO, 25)
]

for a in armas:
    print(a)

print(f"\nTipos disponibles: {[t.name for t in TipoArma]}")
