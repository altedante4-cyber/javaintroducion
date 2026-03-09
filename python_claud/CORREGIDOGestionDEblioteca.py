class Libro:
    def __init__(self, codigo, titulo, autor, año, disponibilidad=True):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.disponibilidad = disponibilidad

    def __repr__(self):
        return f"{self.titulo} ({self.autor}), {self.año}"


class Usuario:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.libros_prestados = []


class Biblioteca:
    def __init__(self):
        self.inventario_de_libros = {}
        self.historial_de_prestamos = []
        self.usuarios_registrados = {}

    def agregar_libro(self, libro):
        if libro.codigo in self.inventario_de_libros:
            return False
        self.inventario_de_libros[libro.codigo] = libro
        return True

    def eliminar_libro(self, codigo):
        if codigo in self.inventario_de_libros:
            del self.inventario_de_libros[codigo]
            return True
        return False

    def registrar_usuario(self, usuario):
        if usuario.codigo in self.usuarios_registrados:
            return False
        self.usuarios_registrados[usuario.codigo] = usuario
        return True

    def prestar_libro(self, codigo_usuario, codigo_libro):
        if codigo_usuario not in self.usuarios_registrados:
            raise ValueError("Usuario no registrado")
        if codigo_libro not in self.inventario_de_libros:
            raise ValueError("Libro no encontrado")

        libro = self.inventario_de_libros[codigo_libro]
        if not libro.disponibilidad:
            raise ValueError("El libro no está disponible")

        usuario = self.usuarios_registrados[codigo_usuario]
        libro.disponibilidad = False
        usuario.libros_prestados.append(libro)

        self.historial_de_prestamos.append({
            "usuario": usuario,
            "libro": libro,
            "accion": "prestado"
        })
        return True

    def devolver_libro(self, codigo_usuario, codigo_libro):
        if codigo_usuario not in self.usuarios_registrados:
            raise ValueError("Usuario no registrado")

        usuario = self.usuarios_registrados[codigo_usuario]

        if codigo_libro not in self.inventario_de_libros:
            raise ValueError("Libro no encontrado")

        libro = self.inventario_de_libros[codigo_libro]

        if libro not in usuario.libros_prestados:
            raise ValueError("El usuario no tiene este libro prestado")

        libro.disponibilidad = True
        usuario.libros_prestados.remove(libro)

        self.historial_de_prestamos.append({
            "usuario": usuario,
            "libro": libro,
            "accion": "devuelto"
        })
        return True

    def mostrar_historial(self):
        print("\n=== Historial ===")
        for registro in self.historial_de_prestamos:
            print(f"{registro['usuario'].nombre} {registro['accion']} '{registro['libro'].titulo}'")

    def mostrar_disponibles(self):
        print("\n=== Libros disponibles ===")
        for libro in self.inventario_de_libros.values():
            if libro.disponibilidad:
                print(f"{libro.titulo} - {libro.autor} ({libro.año})")


# === Prueba ===
biblioteca = Biblioteca()
biblioteca.agregar_libro(Libro("L001", "Python para todos", "Juan Pérez", 2020))
biblioteca.agregar_libro(Libro("L002", "Clean Code", "Robert Martin", 2008))
biblioteca.registrar_usuario(Usuario("U001", "María García"))
biblioteca.prestar_libro("U001", "L001")
biblioteca.mostrar_historial()
biblioteca.devolver_libro("U001", "L001")
biblioteca.mostrar_historial()
biblioteca.mostrar_disponibles()