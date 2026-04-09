from collections import defaultdict

class Tienda:
    def __init__(self):
        self.productos = defaultdict(lambda: {"precio": 0, "stock": 0})
    
    def agregar_producto(self, nombre, precio, stock):
        self.productos[nombre]["precio"] = precio
        self.productos[nombre]["stock"] = stock
    
    def __str__(self):
        return f"{'Producto':<15} {'Precio':<10} {'Stock':<10}\n" + \
               "\n".join(f"{k:<15} ${v['precio']:<9} {v['stock']:<10}" 
                        for k, v in self.productos.items())
    
    def stock_total(self):
        return sum(v["stock"] for v in self.productos.values())
    
    def valor_total(self):
        return sum(v["precio"] * v["stock"] for v in self.productos.values())

tienda = Tienda()
tienda.agregar_producto("Espada", 100, 5)
tienda.agregar_producto("Escudo", 50, 10)
tienda.agregar_producto("Pocion", 25, 50)

print(tienda)
print(f"\nStock total: {tienda.stock_total()}")
print(f"Valor inventario: ${tienda.valor_total()}")
