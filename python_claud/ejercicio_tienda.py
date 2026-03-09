"""
Ejercicio: Sistema de Gestión de Tienda
Nivel: Medio

Crea un sistema de gestión para una tienda con las siguientes características:
"""

class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __repr__(self):
        return f"{self.nombre} (Stock: {self.stock}) - ${self.precio:.2f}"


class Carrito:
    def __init__(self):
        self.items = {}

    def agregar_producto(self, producto, cantidad):
        if cantidad > producto.stock:
            raise ValueError(f"Stock insuficiente para {producto.nombre}")
        if producto.codigo in self.items:
            self.items[producto.codigo]["cantidad"] += cantidad
        else:
            self.items[producto.codigo] = {"producto": producto, "cantidad": cantidad}
        producto.stock -= cantidad

    def eliminar_producto(self, codigo):
        if codigo in self.items:
            producto = self.items[codigo]["producto"]
            cantidad = self.items[codigo]["cantidad"]
            producto.stock += cantidad
            del self.items[codigo]

    def calcular_total(self):
        return sum(item["producto"].precio * item["cantidad"] for item in self.items.values())

    def mostrar_carrito(self):
        print("\n=== Carrito de Compras ===")
        for item in self.items.values():
            p = item["producto"]
            c = item["cantidad"]
            print(f"{p.nombre} x{c} = ${p.precio * c:.2f}")
        print(f"Total: ${self.calcular_total():.2f}")


class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = {}
        self.ventas = []

    def agregar_producto(self, producto):
        self.productos[producto.codigo] = producto

    def buscar_producto(self, codigo):
        return self.productos.get(codigo)

    def mostrar_inventario(self):
        print(f"\n=== Inventario de {self.nombre} ===")
        for p in self.productos.values():
            print(f"{p.codigo}: {p}")

    def realizar_venta(self, carrito):
        if not carrito.items:
            raise ValueError("El carrito está vacío")
        
        total = carrito.calcular_total()
        self.ventas.append({"carrito": dict(carrito.items), "total": total})
        return total


# === Programa principal ===
if __name__ == "__main__":
    tienda = Tienda("Mi Tienda Python")
    
    tienda.agregar_producto(Producto("001", "Laptop", 999.99, 5))
    tienda.agregar_producto(Producto("002", "Mouse", 29.99, 20))
    tienda.agregar_producto(Producto("003", "Teclado", 49.99, 15))
    tienda.agregar_producto(Producto("004", "Monitor", 299.99, 8))
    
    print("Bienvenido a la tienda!")
    tienda.mostrar_inventario()
    
    carrito = Carrito()
    
    p1 = tienda.buscar_producto("001")
    p2 = tienda.buscar_producto("002")
    p3 = tienda.buscar_producto("003")
    
    carrito.agregar_producto(p1, 1)
    carrito.agregar_producto(p2, 2)
    carrito.agregar_producto(p3, 1)
    
    carrito.mostrar_carrito()
    
    total = tienda.realizar_venta(carrito)
    print(f"\nVenta realizada! Total: ${total:.2f}")
    
    print("\n--- Inventario después de la venta ---")
    tienda.mostrar_inventario()
