class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio
    
    @property
    def nombre(self):
        return self._nombre.upper()
    
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor

p = Producto("camisa", 50)
print(f"Nombre: {p.nombre}")
print(f"Precio: {p.precio}")
p.precio = 75
print(f"Nuevo precio: {p.precio}")
