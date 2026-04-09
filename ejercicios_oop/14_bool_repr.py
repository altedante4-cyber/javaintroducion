class Enemigo:
    def __init__(self, nombre, salud, dano):
        self.nombre = nombre
        self.salud = salud
        self.dano = dano
        self.esta_vivo = salud > 0
    
    def __bool__(self):
        return self.esta_vivo
    
    def __repr__(enemigo):
        return f"Enemigo({enemigo.nombre}, salud={enemigo.salud})"

enemigos = [
    Enemigo("Goblin", 30, 5),
    Enemigo("Dragón", 100, 20),
    Enemigo("Esqueleto", 15, 3)
]

print("=== Enemigos vivos ===")
for e in filter(bool, enemigos):
    print(repr(e))
