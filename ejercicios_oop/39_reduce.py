from functools import reduce

class Carrito:
    def __init__(self):
        self.productos = []
    
    def agregar(self, nombre, precio):
        self.productos.append({"nombre": nombre, "precio": precio})
    
    def total(self):
        return reduce(lambda acc, p: acc + p["precio"], self.productos, 0)
    
    def descuento(self, porcentaje):
        return self.total() * (1 - porcentaje / 100)

carrito = Carrito()
carrito.agregar("Espada", 100)
carrito.agregar("Escudo", 50)
carrito.agregar("Pociones", 25)

print(f"Total: ${carrito.total()}")
print(f"Con 10% descuento: ${carrito.descuento(10):.2f}")
