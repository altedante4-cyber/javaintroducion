class JugarRPG:
    @classmethod
    def crear_personaje(cls, nombre, tipo):
        if tipo == "mago":
            return cls.Mago(nombre)
        elif tipo == "guerrero":
            return cls.Guerrero(nombre)
        return cls.Persona(nombre)
    
    class Persona:
        def __init__(self, nombre):
            self.nombre = nombre
            self.salud = 100
        
        def ataque(self):
            return 10
    
    class Mago(Persona):
        def __init__(self, nombre):
            super().__init__(nombre)
            self.mana = 50
        
        def ataque(self):
            return self.mana // 2
    
    class Guerrero(Persona):
        def __init__(self, nombre):
            super().__init__(nombre)
            self.fuerza = 20
        
        def ataque(self):
            return self.fuerza

p1 = JugarRPG.crear_personaje("Gandalf", "mago")
p2 = JugarRPG.crear_personaje("Conan", "guerrero")
print(f"{p1.nombre}: Ataque {p1.ataque()}")
print(f"{p2.nombre}: Ataque {p2.ataque()}")
