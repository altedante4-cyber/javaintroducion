class Objeto:
    def __init__(self, nombre, peso, valor):
        self.nombre = nombre
        self.peso = peso
        self.valor = valor
    
    def __str__(self):
        return f"{self.nombre} (Peso: {self.peso}, Valor: {self.valor})"

class CofreTesoro:
    def __init__(self):
        self.objetos = []
    
    def agregar(self, obj):
        self.objetos.append(obj)
    
    def __str__(self):
        return "\n".join(str(o) for o in self.objetos)
    
    def __len__(self):
        return len(self.objetos)
    
    def __iter__(self):
        return iter(self.objetos)
    
    def filtro(self, condicion):
        return [o for o in self.objetos if condicion(o)]

cofre = CofreTesoro()
cofre.agregar(Objeto("Oro", 10, 1000))
cofre.agregar(Objeto("Rubí", 1, 500))
cofre.agregar(Objeto("Espada", 5, 200))

print("=== Todo el tesoro ===")
print(cofre)

print("\n=== Objetos con valor > 300 ===")
for o in cofre.filtro(lambda o: o.valor > 300):
    print(o)
