class Carta:
    PALOS = ["Corazones", "Diamantes", "Treboles", "Picas"]
    VALORES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor
    
    def __str__(self):
        return f"{self.valor} de {self.palo}"

class Mazo:
    def __init__(self):
        self.cartas = [Carta(p, v) for p in Carta.PALOS for v in Carta.VALORES]
    
    def mezclar(self):
        import random
        random.shuffle(self.cartas)
    
    def mostrar(self):
        for c in self.cartas:
            print(c)

mazo = Mazo()
mazo.mezclar()
print("=== Primeras 5 cartas ===")
for c in mazo.cartas[:5]:
    print(c)
