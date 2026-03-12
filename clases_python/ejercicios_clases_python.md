# Ejercicios de Clases en Python

---

## Ejercicio 1: Sistema de Gestión de Biblioteca

### Enunciado

Crea una clase `Biblioteca` que gestione libros y usuarios con los siguientes requisitos:

1. **Atributo de clase**: `total_libros` (cuenta cuántos libros existen en total)

2. **Constructor**: Recibe el nombre de la biblioteca y crea una lista vacía de libros

3. **Método de instancia** `agregar_libro(titulo, autor)`: Añade un libro a la biblioteca (incrementa `total_libros`)

4. **Método estático** `validar_anio(anio)`: Recibe un año de publicación y retorna `True` si está entre 1450 y 2026, `False` en caso contrario

5. **Método de clase** `obtener_total_libros()`: Retorna una cadena con el total de libros registrados en todas las bibliotecas

6. **Método de clase alternativo** `crear_biblioteca_vacia(nombre)`: Constructor alternativo que crea una biblioteca sin libros

### Solución

```python
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


# ============ PRUEBAS ============
print(Biblioteca.validar_anio(1500))  # True
print(Biblioteca.validar_anio(1400))   # False

b1 = Biblioteca("Central")
b1.agregar_libro("Don Quijote", "Cervantes")
b1.agregar_libro("1984", "Orwell")

b2 = Biblioteca.crear_biblioteca_vacia("Norte")
b2.agregar_libro("Cien Años", "García Márquez")

print(Biblioteca.obtener_total_libros())  # "El numero total de libros es 3"
```

---

## Ejercicio 2: Sistema de Torneos de Videojuegos

### Enunciado

Crea una clase `Jugador` para gestionar participantes en un torneo de videojuegos.

1. **Atributos de clase**: `contador` (jugadores registrados), `ranking` (lista de todos los jugadores)

2. **Constructor**: Recibe `nombre`, `edad`, `puntuacion` (inicial 1000)

3. **Properties**:
   - `puntuacion`: Permite obtener y modificar puntuación con validación (mín 0, máx 9999)
   - `nombre`: Solo getter (no se puede cambiar nombre después de creado)

4. **Método de instancia** `actualizar_puntuacion(puntos)`: Modifica puntuación (positivos o negativos)

5. **Método estático** `generar_suerte()`: Retorna número aleatorio entre 1 y 100

6. **Método de clase** `obtener_ranking()`: Retorna lista ordenada de jugadores por puntuación (mayor a menor)

7. **Método de clase alternativo** `crear_jugador_random(nombre)`: Crea jugador con edad y puntuación aleatorias

**Bonus**: Implementa `__str__` para mostrar cada jugador formateado como tabla.

### Solución

```python
import random


class Jugador:
    contador = 0
    ranking = []

    def __init__(self, nombre, edad, puntuacion=1000):
        self._nombre = nombre
        self.edad = edad
        self._puntuacion = puntuacion
        Jugador.ranking.append(self)
        Jugador.contador += 1

    @property
    def puntuacion(self):
        return self._puntuacion

    @puntuacion.setter
    def puntuacion(self, valor):
        if valor >= 0 and valor <= 9999:
            self._puntuacion = valor
        else:
            print("Valor de puntuación no válido (debe estar entre 0 y 9999)")

    @property
    def nombre(self):
        return self._nombre

    def actualizar_puntuacion(self, puntos):
        nueva_puntuacion = self._puntuacion + puntos
        if 0 <= nueva_puntuacion <= 9999:
            self._puntuacion = nueva_puntuacion
        else:
            print("La puntuación resultante excede los límites")

    @staticmethod
    def generar_suerte():
        return random.randint(1, 100)

    @classmethod
    def obtener_ranking(cls):
        lista_ordenada = sorted(cls.ranking, key=lambda x: x.puntuacion, reverse=True)
        return lista_ordenada

    @classmethod
    def crear_jugador_random(cls, nombre):
        edad = random.randint(18, 40)
        puntuacion = random.randint(0, 9999)
        return cls(nombre, edad, puntuacion)

    def __str__(self):
        return f"| {self._nombre:<15} | {self.edad:>3} años | {self._puntuacion:>4} pts |"


# ============ PRUEBAS ============
print("=" * 50)
print("CREAR JUGADORES")
print("=" * 50)

j1 = Jugador("Carlos", 25, 1500)
j2 = Jugador.crear_jugador_random("María")
j3 = Jugador("Ana", 30)

print(j1)
print(j2)
print(j3)

print("\n" + "=" * 50)
print("ACTUALIZAR PUNTUACIÓN (+500)")
print("=" * 50)
j1.actualizar_puntuacion(500)
print(f"Nueva puntuación de Carlos: {j1.puntuacion}")

print("\n" + "=" * 50)
print("GENERAR SUERTE")
print("=" * 50)
print(f"Número de suerte: {Jugador.generar_suerte()}")

print("\n" + "=" * 50)
print("RANKING (ordenado por puntuación)")
print("=" * 50)
print("| NOMBRE         | EDAD | PUNTOS |")
print("|" + "-" * 17 + "+" + "-" * 5 + "+" + "-" * 7 + "|")
for jugador in Jugador.obtener_ranking():
    print(jugador)

print("\n" + "=" * 50)
print(f"Total jugadores: {Jugador.contador}")
```

---

## Resumen de Conceptos

| Decorador | Descripción | Parámetro |
|-----------|-------------|-----------|
| `@staticmethod` | Método independiente, no accede a clase ni instancia | Ninguno |
| `@classmethod` | Método de clase, accede a la clase | `cls` |
| `@property` | Getter: permite leer como atributo | - |
| `@nombre.setter` | Setter: permite asignar con validación | - |

### Diferencias clave

- **`extend` vs `append`**: `extend` añade elementos sueltos, `append` añade un elemento completo
- **Atributo con `_`**: Convención Python para indicar "protegido" (no acceso directo)
- **`self` vs `cls`**: `self` = instancia, `cls` = clase entera
