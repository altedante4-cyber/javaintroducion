from collections import namedtuple

Carta = namedtuple("Carta", ["palo", "valor"])

class JuegoCartas:
    PALOS = ["Corazones", "Diamantes", "Treboles", "Picas"]
    VALORES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    def __init__(self):
        self.mano = []
    
    def generar_mano(self):
        import random
        self.mano = [
            Carta(random.choice(self.PALOS), random.choice(self.VALORES))
            for _ in range(5)
        ]
    
    def __str__(self):
        return " | ".join(f"{c.valor}-{c.palo[:3]}" for c in self.mano)

juego = JuegoCartas()
juego.generar_mano()
print(f"Mano: {juego}")
