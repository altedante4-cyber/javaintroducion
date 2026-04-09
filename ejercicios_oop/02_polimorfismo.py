class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def sonido(self):
        return "Sonido genérico"

class Perro(Animal):
    def sonido(self):
        return "Guau guau"

class Gato(Animal):
    def sonido(self):
        return "Miau miau"

animales = [Perro("Rex"), Gato("Michi"), Animal("Animal")]
for a in animales:
    print(f"{a.nombre}: {a.sonido()}")
