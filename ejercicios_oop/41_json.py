import json

class Mission:
    def __init__(self, id, nombre, dificultad, recompensa):
        self.id = id
        self.nombre = nombre
        self.dificultad = dificultad
        self.recompensa = recompensa
    
    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "dificultad": self.dificultad, "recompensa": self.recompensa}
    
    def __str__(self):
        return f"{self.nombre} (Dif: {self.dificultad}) - Recompensa: {self.recompensa}"

class MissionManager:
    def __init__(self):
        self.misiones = []
    
    def agregar(self, mission):
        self.misiones.append(mission)
    
    def guardar_json(self, archivo):
        with open(archivo, "w") as f:
            json.dump([m.to_dict() for m in self.misiones], f, indent=2)
    
    def cargar_json(self, archivo):
        with open(archivo, "r") as f:
            datos = json.load(f)
            self.misiones = [Mission(**d) for d in datos]
    
    def __str__(self):
        return "\n".join(str(m) for m in self.misiones)

mm = MissionManager()
mm.agregar(Mission(1, "Derrotar dragón", "Difícil", 500))
mm.agregar(Mission(2, "Recoger hierbas", "Fácil", 50))
mm.guardar_json("misiones.json")

mm2 = MissionManager()
mm2.cargar_json("misiones.json")
print(mm2)
