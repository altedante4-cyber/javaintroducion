from abc import ABCMeta , abstractmethod

class Producto:

    def __init__(self,codigo,nombre,precio_base ,stock ):
        
        if stock <= 0 : return print("error: stock invalido ")
        if precio_base < 0 : return print("error: stock invalido ")
        self.codigo =codigo
        self.nombre = nombre
        self.precio_base = precio_base
        self.stock =stock 


class Electronica(Producto):

    def __init__(self,codigo,nombre,precio_base,stock,garantia_meses,marca):

        super().__init__(codigo,nombre,precio_base,stock)
        self.garantia_meses = garantia_meses
        self.marca = marca

    def descuento_stock(self):
        if self.stock > 50 : return self.precio_base - (self.precio_base * 1.15 )
        if self.stock > 20 : return self.precio_base - (self.precio_base * 1.10)
        if self.stock > 0 : return self.precio_base - (self.precio_base * 0.05)
        if self.stock == 0 : return self.precio_base - (self.precio_base* 1.20)

class Alimentacion(Producto):

    def __init__(self,codigo,nombre,precio_base , stock , fecha_caducidad , es_ecologico):
        super().__init__(codigo,nombre,precio_base,stock)
        self.fecha_caducidad = fecha_caducidad
        self.es_ecologico = es_ecologico
    
    def descuento_proximidad(self):

        descuento_total = self.precio_base
        if date.today() + timedelta(days=3) : descuento_total = self.precio_base
        if date.today() + timedelta(days=1) or date.today() + timedelta(days=2) : return descuento_total -(descuento_total * 1.30)
        if date.today(): descuento_total - (descuento_total * 1.50)
        


class Ropa(Producto):

    def __init__(self,codigo,nombre,precio_base,stock,talla,temporada):
        super().__init__(codigo,nombre,precio_base,stock)
        tallas_correctas =["XS","S","M","L","XL"]
        temporada_valida=["primavera","verano","otonio","invierno"]

        if talla not in tallas_correctas : return print("talla no correcta")
        if temporada not in temporada_valida : return print("temporada incorrecta")

        self.talla = talla
        self.temporada = temporada
    
    def descuento_por_temporada(self):
        if self.temporada == "invierno" : self.precio_base = self.precio_base
        if self.temporada == "otoño" : self.precio_base - (self.precio_base * 1.25)
        if self.temporada != "invierno" or self.temporada != "otoño" : self.precio_base - (self.precio_base * 1.15)


    


class Carrito:
    lista_comprar = []
    def __init__(self,producto,cantidad):

        Carrito.lista_comprar.append([producto,cantidad])
    
    def calcular_precio(self):
        total = 0
        for producto, cantidad in Carrito.lista_comprar:
            total += producto.precio_base * cantidad
        return total
    
    def aplicar_descuentos(self):
        total = 0
        for producto, cantidad in Carrito.lista_comprar:
            precio = producto.precio_base * cantidad
            
            # Aplicar descuento según tipo de producto
            if isinstance(producto, Electronica):
                descuento = producto.descuento_stock()
                precio -= descuento
            elif isinstance(producto, Alimentacion):
                descuento = producto.descuento_proximidad()
                precio -= descuento
            elif isinstance(producto, Ropa):
                descuento = producto.descuento_por_temporada()
                precio -= descuento
            
            total += precio
        return total


if __name__ == "__main__":
    from datetime import date, timedelta

    print("=== Prueba clase Electronica ===")
    # Stock > 50: 15%
    ele1 = Electronica("E001", "Laptop", 1000, 60, 24, "Dell")
    print(f"Producto: {ele1.nombre}, Stock: {ele1.stock}, Precio: {ele1.precio_base}")
    print(f"Descuento stock > 50 (15%): {ele1.descuento_stock()}")
    
    # Stock > 20: 10%
    ele2 = Electronica("E002", "Celular", 500, 30, 12, "Samsung")
    print(f"Producto: {ele2.nombre}, Stock: {ele2.stock}, Precio: {ele2.precio_base}")
    print(f"Descuento stock > 20 (10%): {ele2.descuento_stock()}")
    
    # Stock > 0: 5%
    ele3 = Electronica("E003", "Tablet", 300, 10, 12, "Apple")
    print(f"Producto: {ele3.nombre}, Stock: {ele3.stock}, Precio: {ele3.precio_base}")
    print(f"Descuento stock > 0 (5%): {ele3.descuento_stock()}")
    
    # Stock == 0: 20%
    ele4 = Electronica("E004", "Auriculares", 100, 5, 12, "Sony")
    print(f"Producto: {ele4.nombre}, Stock: {ele4.stock}, Precio: {ele4.precio_base}")
    print(f"Descuento stock == 0 (20%): {ele4.descuento_stock()}")

    print("\n=== Prueba clase Alimentacion ===")
    # Caduca en 3+ días: 0%
    ali1 = Alimentacion("A001", "Leche", 2, 10, date.today() + timedelta(days=5), False)
    print(f"Producto: {ali1.nombre}, Caduca: {ali1.fecha_caducidad}, Precio: {ali1.precio_base}")
    
    # Caduca en 1-2 días: 30%
    ali2 = Alimentacion("A002", "Yogur", 3, 20, date.today() + timedelta(days=2), True)
    print(f"Producto: {ali2.nombre}, Caduca: {ali2.fecha_caducidad}, Precio: {ali2.precio_base}")
    
    # Caduca hoy: 50%
    ali3 = Alimentacion("A003", "Pan", 1.5, 15, date.today(), False)
    print(f"Producto: {ali3.nombre}, Caduca: {ali3.fecha_caducidad}, Precio: {ali3.precio_base}")
    
    # Caduca ya (antes de hoy): 70%
    ali4 = Alimentacion("A004", "Queso", 5, 8, date.today() - timedelta(days=1), True)
    print(f"Producto: {ali4.nombre}, Caduca: {ali4.fecha_caducidad}, Precio: {ali4.precio_base}")

    print("\n=== Prueba clase Ropa ===")
    # Temporada actual (primavera): 0%
    ropa1 = Ropa("R001", "Camisa", 50, 30, "M", "primavera")
    print(f"Producto: {ropa1.nombre}, Talla: {ropa1.talla}, Temporada: {ropa1.temporada}, Precio: {ropa1.precio_base}")
    
    # Temporada pasada (invierno si es primavera): 25%
    ropa2 = Ropa("R002", "Abrigo", 120, 15, "L", "invierno")
    print(f"Producto: {ropa2.nombre}, Talla: {ropa2.talla}, Temporada: {ropa2.temporada}, Precio: {ropa2.precio_base}")
    
    # Otra temporada: 15%
    ropa3 = Ropa("R003", "Vestido", 80, 25, "S", "verano")
    print(f"Producto: {ropa3.nombre}, Talla: {ropa3.talla}, Temporada: {ropa3.temporada}, Precio: {ropa3.precio_base}")
    
    # Talla inválida
    print("Talla inválida:", end=" ")
    ropa4 = Ropa("R004", "Pantalón", 60, 10, "XXL", "otoño")

    print("\n=== Prueba clase Carrito ===")
    Carrito.lista_comprar = []  # Limpiar lista
    c1 = Carrito(ele1, 2)
    c2 = Carrito(ali2, 5)
    c3 = Carrito(ropa1, 1)
    print(f"Productos en carrito: {len(Carrito.lista_comprar)}")
    for prod, cant in Carrito.lista_comprar:
        print(f"  - {prod.nombre}, Cantidad: {cant}")
    
    print(f"\nPrecio base total: {c1.calcular_precio()}")
