from datetime import datetime

class MixinLogger:
    def log(self, mensaje):
        print(f"[LOG] {datetime.now()} - {mensaje}")

class Jugador(MixinLogger):
    def __init__(self, nombre):
        self.nombre = nombre
        self.salud = 100
    
    def recibir_dano(self, dano):
        self.salud -= dano
        self.log(f"{self.nombre} recibió {dano} de daño")
        if self.salud <= 0:
            self.log(f"{self.nombre} ha muerto")

j = Jugador("Héroe")
j.recibir_dano(30)
j.recibir_dano(50)
j.recibir_dano(30)
