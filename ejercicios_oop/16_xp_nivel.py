class Jugador:
    def __init__(self, nombre, nivel=1):
        self.nombre = nombre
        self.nivel = nivel
        self.experiencia = 0
    
    def ganar_exp(self, cantidad):
        self.experiencia += cantidad
        while self.experiencia >= self.nivel * 100:
            self.experiencia -= self.nivel * 100
            self.nivel += 1
            print(f"¡{self.nombre} subió a nivel {self.nivel}!")

j = Jugador("Heroe")
for i in range(10):
    j.ganar_exp(50)
print(f"Nivel final: {j.nivel}, XP: {j.experiencia}")
