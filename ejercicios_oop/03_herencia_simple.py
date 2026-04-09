class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def descripcion(self):
        return f"{self.marca} {self.modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas
    
    def descripcion(self):
        return f"{super().descripcion()} - {self.puertas} puertas"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada
    
    def descripcion(self):
        return f"{super().descripcion()} - {self.cilindrada}cc"

print(Coche("Ford", "Mustang", 2).descripcion())
print(Moto("Yamaha", "R1", 1000).descripcion())
