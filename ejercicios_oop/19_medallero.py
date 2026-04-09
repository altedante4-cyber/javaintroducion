class Atleta:
    def __init__(self, nombre, sport):
        self.nombre = nombre
        self.sport = sport
        self.medallas = {"oro": 0, "plata": 0, "bronce": 0}
    
    @property
    def total_medallas(self):
        return sum(self.medallas.values())
    
    def agregar_medalla(self, tipo):
        if tipo in self.medallas:
            self.medallas[tipo] += 1
    
    def __str__(self):
        return f"{self.nombre} ({self.sport}) - {self.total_medallas} medallas"

atletismo = [Atleta("Usain", "atletismo"), Atleta("Carl Lewis", "atletismo")]
natacion = [Atleta("Phelps", "natacion")]

atleta = atletismo[0]
atleta.agregar_medalla("oro")
atleta.agregar_medalla("oro")
atleta.agregar_medalla("bronce")

print(atleta)
print(f"Oros: {atleta.medallas['oro']}")
