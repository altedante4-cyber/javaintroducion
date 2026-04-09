class Artefacto:
    def __init__(self, nombre):
        self.nombre = nombre

class Arma(Artefacto):
    def __init__(self, nombre, dano):
        super().__init__(nombre)
        self.dano = dano

class Magico(Artefacto):
    def __init__(self, nombre, mana):
        super().__init__(nombre)
        self.mana = mana

class EspadaMagica(Arma, Magico):
    def __init__(self, nombre, dano, mana):
        Arma.__init__(self, nombre, dano)
        Magico.__init__(self, nombre, mana)
    
    def __str__(self):
        return f"{self.nombre} - Daño: {self.dano} - Mana: {self.mana}"

espada = EspadaMagica("Excalibur", 50, 100)
print(espada)
print(f"MRO: {EspadaMagica.__mro__}")
