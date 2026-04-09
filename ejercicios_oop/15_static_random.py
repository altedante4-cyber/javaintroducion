class Moneda:
    @staticmethod
    def lanzar():
        import random
        return random.choice(["Cara", "Cruz"])

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.saldo = 100
    
    def jugar(self):
        resultado = Moneda.lanzar()
        if resultado == "Cara":
            self.saldo += 10
            print(f"{self.nombre}: ¡Ganó! Saldo: {self.saldo}")
        else:
            self.saldo -= 10
            print(f"{self.nombre}: Perdió. Saldo: {self.saldo}")

jugadores = [Jugador("Alice"), Jugador("Bob")]
for _ in range(5):
    for j in jugadores:
        j.jugar()
    print("-" * 20)
