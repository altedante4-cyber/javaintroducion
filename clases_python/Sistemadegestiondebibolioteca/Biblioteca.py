class Biblioteca:
    total_libros = 0
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_libros = []
    
    def agregar_libro(self, titulo, autor):
        self.lista_libros.append((titulo, autor))
        Biblioteca.total_libros += 1
    
    @staticmethod
    def validar_anio(anio):
        return anio >= 1450 and anio <= 2026
    
    @classmethod
    def obtener_total_libros(cls):
        return f"El numero total de libros es {cls.total_libros}"
    
    @classmethod
    def crear_biblioteca_vacia(cls, nombre):
        return cls(nombre)
    

    
    
a = Biblioteca.validar_anio(1500)
b = Biblioteca.validar_anio(1400)

print("Validación a:", a)
print("Validación b:", b)

b1 = Biblioteca("Central")
b1.agregar_libro("Don Quijote", "Cervantes")
b1.agregar_libro("1984", "Orwell")

print("Libro 1 en b1:", b1.lista_libros[0])
print("Libro 2 en b1:", b1.lista_libros[1])

b2 = Biblioteca.crear_biblioteca_vacia("Norte")
b2.agregar_libro("Cien Años", "García Márquez")

print("Libro 1 en b2:", b2.lista_libros[0])

print(Biblioteca.obtener_total_libros())  # "Total de libros: 3"

#error 

#extend([titulo,autor])  correcion => append((titulo,autor))  extend anade elemenots sueltos . append con tupla guard libro completo
#falta @classmethod  correcion = anadido decorador  por que sin el python interpreta cls como parametro normal 

#decorador separado de funcion correcion=> jutno en una linea => python no reconoce el decorador separado

#lihro  libbro 