class Producto:

    def __init__(self,codigo,nombre, precio,stock,categoria):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock 
        self.categoria = categoria 


    def __repr__(self):
        return f"{self.nombre} (Stok:){self.stock} - ${self.precio:.2f} - {self.categoria}"
    


class Carrito:
    def __init__(self):
        self.items = {}
    
    def agregar_producto(self,producto,cantidad):
   
        if producto is None:
            raise ValueError("POrducto no encontrado ")
        if cantidad > producto.stock :
            raise ValueError(f"STock insuficiente para {producto.nombre}")
        
        if producto.codigo in self.items:
            self.items[producto.codigo]["cantidad"] += cantidad 

        else:
            self.items[producto.codigo]={"producto":producto,"cantidad":cantidad}

            producto.stock -= cantidad

        
    def eliminar_producto(self,codigo):

        if codigo in self.items:
            producto = self.items[codigo]["producto"]
            cantidad = self.items[codigo]["cantidad"]
            producto.stock += cantidad
            del self.items[codigo]

    def calcular_total(self):

        total =  sum(item["producto"].precio * item ["cantidad"] for item in self.items.values())
    
        if total > 500 :
            descuento = total * 0.10
            print(f"Descuento aplicado : ${descuento:.2f}")
            return total - descuento 
        
        return total 
    def mostrar_carrito(self):
        print("\n ==== carrito de comprars === ")
        for item in self.items.values():
            p = item["producto"]
            c = item["cantidad"]
            print(f"{p.nombre} x{c} = ${p.precio * c:.2f}")
        
        print(f"Total ${self.calcular_total():.2f}")


class Tienda:
    def __init__(self , nombre ):

        self.nombre = nombre
        self.producto = {}
        self.ventas = []

    def agregar_producto(self,producto):



        #validar que el codigo de producto no exista al agregarlo

        if producto.codigo not in self.producto:

            self.producto[producto.codigo] = producto 
            return True 
        
        print(f"Ya existe un porducto con codigo {producto.codigo}")
        return False 
    def buscar_producto(self,codigo):
        return self.producto.get(codigo)
    

    def buscar_producto(self,nombre):

        for producto in self.producto.values():
            if producto.nombre.lower() == nombre.lower():
                return producto
        
        return None 
    #si queremos retornar un booleano se hace de la siguiente manera
    # return any(p.nombre.lower() == nombre.lower() for p in self.producto.values())
    def eliminar_producto_tienda(self,codigo):

        if  self.producto.get(codigo):
            del self.producto[codigo]
            return True 
        
        return False 



        
    
    def mostrar_inventario(self):
        print(f"\n== inventario de {self.nombre} == ")
        for p in self.producto.values():
            print(f"{p.codigo}: {p}")

    def realizar_venta(self,carrito):

        if not carrito.items:

            raise ValueError("El carrito esta vacio")
        total = carrito.calcular_total()
        self.ventas.append({"carrito":dict(carrito.items),"total":total })
        return total 

    def mostrar_categoria_productos(self,categoria):

        print(f"\n Productos en categoria: {self,categoria }")
        for producto in self.producto.values():
            if producto.categoria.lower() == categoria.lower():
                print(f"-{producto.nombre}: ${producto.precio}")

if __name__ == "__main__":

    tienda = Tienda("Mi tienda python ")

    tienda.agregar_producto(Producto("001","Laptop",9999.99,5,"ELectronica"))
    tienda.agregar_producto(Producto("002","Mause",9999.99,5 , "cocina"))
    tienda.agregar_producto(Producto("003","Monitor",9999.99,5 , "Electro"))

    print("bienvenido a la tienda")
    tienda.mostrar_inventario()

    carrito = Carrito()

    tienda.mostrar_categoria_productos("ELectronica")


    p1 = tienda.buscar_producto("001")


    carrito.agregar_producto(p1,1)


    carrito.mostrar_carrito()

    total = tienda.realizar_venta(carrito)
    if( tienda.eliminar_producto_tienda("001")):
        print("elimnado de la tienda correctamente")
    else:
        print("no se ha podido encontrar el producto en la tienda ")


    print(f"\n VEnta realizada total ${total:.2f}")

    print("\n---inventario depsues de la venta--- ")

    tienda.mostrar_inventario()    

    
