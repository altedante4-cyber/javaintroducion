class Libro:

    def __init__(self,codigo,titulo,autor,año,disponibilidad):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.disponibilidad = disponibilidad


class Usuario:

    def __init__(self,codigo,nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.libros_prestados = []
        self.usuario_registrado = []

    def registrar_usuario(self,codigo,nombre):
        self.usuario_registrado.append(codigo)


class Biblioteca:

    def __init__(self,inventario_de_libros , historial_de_prestamos):
        self.inventario_de_libros = []
        self.historial_de_prestamos = []

    def agregar_libros(self,libro):
        self.inventario_de_libros.append(libro)

    def eliminar_libro(self,libro):

        if not self.inventario_de_libros:
            raise ValueError("Esta vacio el inventario")

        if libro in self.inventario_de_libros:
            self.inventario_de_libros.remove(libro)
            return True

        print("No se pudo eliminar el libro")
        return False


    def prestar_libro(self,usuario,libro):

        if libro.disponibilidad != "Disponible":
            raise ValueError("El libro no esta disponible")

        if usuario.codigo not in usuario.usuario_registrado:
            raise ValueError("Usuario no registrado")

        libro.disponibilidad = "No disponible"

        self.historial_de_prestamos.append([usuario, libro])

        return True


    def mostrar_biblioteca(self):

        for libro in self.inventario_de_libros:
            print(libro.titulo, "-", libro.autor)

    def mostrar_historial_prestamo(self):

        for  usuario , libro  in self.historial_de_prestamos:
            print(usuario.nombre , libro.disponibilidad )

    def devolver_libro(self,libro):

         #primer paso cambiar el estado del libro a devolver de No disponiible a disponible 

        #comprobamos que exactamente estaba prestado

        for  i in self.historial_de_prestamos:
            
            if libro.disponibilidad == "No disponible":
                libro.disponibilidad = "Disponible"
                return True 
        
        print("NO encontrado")
        return False 

    def mostrar_libro_disponibles(self):

        if not self.inventario_de_libros:
            raise ValueError("la lista esta vacia")
        
        

        for libro in self.inventario_de_libros:

            if libro.disponibilidad == "Disponible":
                print(vars(libro))
        
# crear biblioteca
biblio = Biblioteca([], [])

# usuario
user1 = Usuario("1234","michael")
user1.registrar_usuario("1234","mika")

# libro
libro1 = Libro("1", "Hola", "Autor1", 2020, "Disponible")

# agregar libro
biblio.agregar_libros(libro1)

# prestar libro
if biblio.prestar_libro(user1,libro1):
    print("Prestamo registrado correctamente")


biblio.mostrar_historial_prestamo()

#devolvemos el libro

if biblio.devolver_libro(libro1):
    print("se ha devuelto correctamente")



biblio.mostrar_historial_prestamo()



# mostrar biblioteca
biblio.mostrar_biblioteca()


biblio.mostrar_libro_disponibles()
