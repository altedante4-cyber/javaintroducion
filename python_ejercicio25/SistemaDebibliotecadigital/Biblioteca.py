from datetime import time , datetime , timedelta 
class Libro:

    def __init__(self,isbn,titulo,autor,anio_publicacion,genero,ejemplares):
        if(len(isbn)!= 13 ): return print("incorrecto") 
        if (anio_publicacion < 1450 or anio_publicacion > 2026 ): return print("nio incorrecto")
        genero_valido = ["ficcion","no-ficcion","ciencia","historia","otro"]
        if (genero not in genero_valido ): return print("genero no valido ")
        if(ejemplares != 1 ): return print("ejemplar invalido ")

        self.isbn = isbn
        self.titulo =titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.genero = genero
        self.ejemplares = ejemplares

    
class Lector:

    def __init__(self,dni,nombre,email,*prestamos_activos):
        
        if(len(dni) != 9 or not ( dni[:8].isdigit() and dni[8].isalpha()) ):return print("dni invalido")
        if any( x for x in email if x == "@"): 
             self.email = email 
        else:
             return print("error email ")
        
        if len(prestamos_activos) < 0 or len(prestamos_activos)> 3 : return print("error prestamos libros")
        self.dni = dni         
        self.nombre = nombre 
        self.prestamos_activos = []


class Prestamo:

    def __init__(self,fecha_inicio , fecha_fin,libro,lector):
        if len(lector.prestamos_activos) > 2:
            return print("Error: El lector ya tiene 3 prestamos activos")
        if libro.ejemplares <= 0:
            return print("Error: No hay ejemplares disponibles")
        
        self.fecha_inicio = datetime.now().date().year
        sacar_fecha= datetime.now()
        self.fecha_fin = sacar_fecha + timedelta(days=4)
        self.libro = libro 
        self.lector = lector
        lector.prestamos_activos.append(self)
        libro.ejemplares -= 1


if __name__ == "__main__":
    print("=== Pruebas clase Libro ===")
    libro1 = Libro("1234567890123", "Cien Años", "García Márquez", 1967, "ficcion", 1)
    if libro1:
        print(f"Libro 1: ISBN={libro1.isbn}, Titulo={libro1.titulo}")
    
    libro2 = Libro("1234567890123", "El Principito", "Saint-Exupéry", 1943, "no-ficcion", 1)
    if libro2:
        print(f"Libro 2: ISBN={libro2.isbn}, Titulo={libro2.titulo}")
    
    print("\n--- Libros invalidos ---")
    print("ISBN corto:", end=" ")
    libro_invalido1 = Libro("123", "Libro", "Autor", 2000, "ficcion", 1)
    print("Año invalido:", end=" ")
    libro_invalido2 = Libro("1234567890123", "Libro", "Autor", 1000, "ficcion", 1)
    print("Genero invalido:", end=" ")
    libro_invalido3 = Libro("1234567890123", "Libro", "Autor", 2020, "comedia", 1)
    print("Ejemplares > 1:", end=" ")
    libro_invalido4 = Libro("1234567890123", "Libro", "Autor", 2020, "ficcion", 5)

    print("\n=== Pruebas clase Lector ===")
    print("--- Lectores validos (8 digitos + 1 letra) ---")
    print("DNI 9 caracteres:", end=" ")
    lector1 = Lector("12345678A", "Juan", "juan@email.com")
    if lector1:
        print(f"OK - DNI={lector1.dni}, Nombre={lector1.nombre}")
    else:
        print("Error")
    
    print("DNI 9 caracteres:", end=" ")
    lector2 = Lector("87654321B", "María", "maria@email.com")
    if lector2:
        print(f"OK - DNI={lector2.dni}, Nombre={lector2.nombre}")
    else:
        print("Error")
    
    print("\n--- Lectores invalidos ---")
    print("DNI corto:", end=" ")
    lector_invalido1 = Lector("1234", "Pedro", "pedro@email.com")
    print("DNI 8 digitos (sin letra):", end=" ")
    lector_invalido2 = Lector("12345678", "Pedro", "pedro@email.com")
    print("DNI 8 digitos + letra:", end=" ")
    lector_invalido3 = Lector("12345678A", "Pedro", "pedro@email.com")
    print("DNI 10 digitos:", end=" ")
    lector_invalido4 = Lector("1234567890", "Pedro", "pedro@email.com")
    print("Email sin @:", end=" ")
    lector_invalido5 = Lector("12345678A", "Pedro", "pedroemail.com")

    print("\n=== Pruebas clase Prestamo ===")
    if libro1 and lector1:
        try:
            prestamo1 = Prestamo("2024-01-01", "2024-01-05", libro1, lector1)
            print(f"Prestamo 1: Libro={prestamo1.libro.titulo}, Lector={prestamo1.lector.nombre}")
            print(f"Fecha inicio: {prestamo1.fecha_inicio}, Fecha fin: {prestamo1.fecha_fin}")
        except Exception as e:
            print(f"Error en prestamo1: {e}")
    else:
        print("No se pudo crear prestamo1 (libro o lector invalido)")
    
    if libro2 and lector2:
        try:
            prestamo2 = Prestamo("2024-02-01", "2024-02-05", libro2, lector2)
            print(f"Prestamo 2: Libro={prestamo2.libro.titulo}, Lector={prestamo2.lector.nombre}")
        except Exception as e:
            print(f"Error en prestamo2: {e}")
    else:
        print("No se pudo crear prestamo2 (libro o lector invalido)")

    print("\n--- Prueba: Lector con 3 prestamos activos ---")
    libro4 = Libro("1234567890124", "Libro A", "Autor A", 2020, "ficcion", 1)
    libro5 = Libro("1234567890125", "Libro B", "Autor B", 2020, "ficcion", 1)
    libro6 = Libro("1234567890126", "Libro C", "Autor C", 2020, "ficcion", 1)
    lector3 = Lector("11111111A", "Carlos", "carlos@email.com")
    if lector3:
        print("Creando prestamos para Carlos...")
        p1 = Prestamo("2024-01-01", "2024-01-05", libro4, lector3)
        print(f"Prestamo 1: {len(lector3.prestamos_activos)} prestamos activos")
        p2 = Prestamo("2024-01-01", "2024-01-05", libro5, lector3)
        print(f"Prestamo 2: {len(lector3.prestamos_activos)} prestamos activos")
        print("Prestamo 3:", end=" ")
        p3 = Prestamo("2024-01-01", "2024-01-05", libro6, lector3)
        print(f"Prestamo 3: {len(lector3.prestamos_activos)} prestamos activos")
        print("Intentando 4to prestamo:", end=" ")
        p4 = Prestamo("2024-01-01", "2024-01-05", libro4, lector3)
        print(f"Final: {len(lector3.prestamos_activos)} prestamos activos")

    print("\n--- Prueba: Ejemplares disponibles ---")
    libro3 = Libro("1234567890123", "Don Quijote", "Cervantes", 1605, "historia", 1)
    lector4 = Lector("22222222A", "Ana", "ana@email.com")
    print(f"Libro 3: {libro3.titulo}, Ejemplares: {libro3.ejemplares}")
    print("Prestamo 1:", end=" ")
    pp1 = Prestamo("2024-01-01", "2024-01-05", libro3, lector4)
    print(f"Ejemplares restantes: {libro3.ejemplares}")
    print("Prestamo 2 (deberia fallar):", end=" ")
    pp2 = Prestamo("2024-01-01", "2024-01-05", libro3, lector4)



            