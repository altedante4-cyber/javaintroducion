# Conceptos de Programación Orientada a Objetos en Python

## 1. Herencia Normal

Una clase hereda de otra clase padre.

```python
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def hablar(self):
        return f"{self.nombre} está hablando"

class Alumno(Persona):
    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido)
        self.edad = edad
    
    def estudiar(self):
        return f"{self.nombre} está estudiando"

# Uso
alumno = Alumno("Juan", "Pérez", 20)
print(alumno.hablar())  # Juan está hablando
print(alumno.estudiar())  # Juan está estudiando
```

---

## 2. Herencia Múltiple

Una clase hereda de varias clases padre.

```python
class Volador:
    def volar(self):
        return "Volando"

class Nadador:
    def nadar(self):
        return "Nadando"

class SuperHeroe(Volador, Nadador):
    def __init__(self, nombre):
        self.nombre = nombre

# Uso
heroe = SuperHeroe("Superman")
print(heroe.volar())  # Volando
print(heroe.nadar())  # Nadando
```

### Method Resolution Order (MRO)

```python
class A:
    def greet(self):
        return "A"

class B(A):
    def greet(self):
        return "B"

class C(A):
    def greet(self):
        return "C"

class D(B, C):
    pass

# Ver el orden de resolución
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

d = D()
print(d.greet())  # B (primero busca en B)
```

---

## 3. Clases Abstractas

Clases que no pueden ser instanciadas directamente y pueden definir métodos abstractos (sin implementación).

```python
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, color):
        self.color = color
    
    @abstractmethod
    def calcular_area(self):
        pass
    
    def mostrar_color(self):
        return f"Color: {self.color}"

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura, color):
        super().__init__(color)
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

# Uso
rectangulo = Rectangulo(10, 5, "Rojo")
print(rectangulo.calcular_area())  # 50
print(rectangulo.mostrar_color())  # Color: Rojo

# No se puede instanciar la clase abstracta
# figura = FiguraGeometrica("Azul")  # Error
```

---

## 4. Métodos Mágicos (Dunder Methods)

Métodos especiales con doble guion bajo al inicio y al final.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    # Representación textual
    def __str__(self):
        return f"{self.nombre}, {self.edad} años"
    
    # Representación para desarrolladores
    def __repr__(self):
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"
    
    # Longitud
    def __len__(self):
        return len(self.nombre)
    
    # Comparación
    def __eq__(self, other):
        return self.edad == other.edad
    
    def __lt__(self, other):
        return self.edad < other.edad
    
    # Indexación
    def __getitem__(self, index):
        return self.nombre[index]
    
    # Llamable
    def __call__(self):
        return f"{self.nombre} dice hola"

# Uso
p1 = Persona("Ana", 25)
p2 = Persona("Juan", 30)

print(str(p1))          # Ana, 25 años
print(repr(p1))          # Persona(nombre='Ana', edad=25)
print(len(p1))           # 3
print(p1 == p2)          # False
print(p1 < p2)           # True
print(p1[0])             # A
print(p1())              # Ana dice hola
```

### Otros métodos mágicos comunes

| Método | Descripción |
|--------|-------------|
| `__init__` | Constructor |
| `__del__` | Destructor |
| `__add__` | Operador + |
| `__sub__` | Operador - |
| `__mul__` | Operador * |
| `__div__` | Operador / |
| `__iter__` | Para iteración |
| `__next__` | Para iteración |
| `__enter__` | Contexto with |
| `__exit__` | Contexto with |

---

## 5. Property (Decoradores)

Permiten controlar el acceso a atributos como si fueran propiedades.

```python
class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
    
    # Getter
    @property
    def nombre(self):
        return self.__nombre
    
    # Setter
    @nombre.setter
    def nombre(self, valor):
        if len(valor) < 2:
            raise ValueError("Nombre muy corto")
        self.__nombre = valor
    
    # Deleter
    @nombre.deleter
    def nombre(self):
        del self.__nombre

# Uso
p = Persona("Ana")
print(p.nombre)      # Ana (usa el getter)
p.nombre = "María"   # Usa el setter
print(p.nombre)      # María
del p.nombre         # Usa el deleter
```

---

## 6. Visibilidad (Public, Protected, Private)

### Convenciones de Python

```python
class Ejemplo:
    def __init__(self):
        self.publico = "Soy público"      # Accesible desde cualquier lugar
        self._protegido = "Soy protegido"  # Convención: no acceder fuera de la clase
        self.__privado = "Soy privado"      # Name mangling: _Clase__privado
    
    def metodo_publico(self):
        return "Método público"
    
    def _metodo_protegido(self):
        return "Método protegido"
    
    def __metodo_privado(self):
        return "Método privado"

# Uso
e = Ejemplo()
print(e.publico)               # Soy público
print(e._protegido)            # Funciona, pero no es recomendado
# print(e.__privado)          # Error
print(e._Ejemplo__privado)     # Funciona (name mangling)
```

---

## 7. Metaclass

Una metaclass es una clase cuyas instancias son otras clases.

```python
# Metaclass simple
class MiMeta(type):
    def __new__(cls, name, bases, attrs):
        # Agregar un atributo a todas las clases creadas
        attrs['creado_por'] = 'MiMeta'
        return super().__new__(cls, name, bases, attrs)

class MiClase(metaclass=MiMeta):
    pass

# Uso
print(MiClase.creado_por)  # MiMeta

# Ejemplo práctico: singleton con metaclass
class Singleton(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Configuracion(metaclass=Singleton):
    def __init__(self, valor):
        self.valor = valor

# Uso
c1 = Configuracion(100)
c2 = Configuracion(200)
print(c1 is c2)   # True
print(c1.valor)   # 100 (c2 también apunta al mismo objeto)
```

---

## 8. Atributos de Clase vs Instancia

### Atributos de Instancia

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre    # Atributo de instancia
        self.edad = edad        # Atributo de instancia

# Cada objeto tiene su propia copia
p1 = Persona("Ana", 25)
p2 = Persona("Juan", 30)
p1.edad = 26  # Solo afecta a p1
```

### Atributos de Clase

```python
class Persona:
    especie = "Humano"  # Atributo de clase (compartido)
    planeta = "Tierra"
    
    def __init__(self, nombre):
        self.nombre = nombre  # Atributo de instancia

# Todos comparten el mismo atributo
print(Persona.especie)  # Humano
print(Persona.planeta)   # Tierra

p1 = Persona("Ana")
p2 = Persona("Juan")

print(p1.especie)    # Humano
print(p2.especie)    # Humano

# Modificar atributo de clase afecta a todos
Persona.planeta = "Marte"
print(p1.planeta)  # Marte
print(p2.planeta)  # Marte
```

### Sobrescribir atributo de clase en instancia

```python
class Persona:
    especie = "Humano"
    
    def __init__(self, nombre):
        self.nombre = nombre

p1 = Persona("Ana")
p2 = Persona("Juan")

# Sobrescribir solo en p1
p1.especie = "Androide"

print(p1.especie)  # Androide
print(p2.especie)  # Humano
```

### Atributos de Clase Mutables

```python
class Curso:
    estudiantes = []  # ¡Peligroso! Compartido por todas las instancias
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def agregar_estudiante(self, nombre):
        self.estudiantes.append(nombre)

# Problema
c1 = Curso("Matemáticas")
c2 = Curso("Historia")

c1.agregar_estudiante("Ana")
c2.agregar_estudiante("Juan")

print(c1.estudiantes)  # ['Ana', 'Juan'] - ¡Juan está en c1!
print(c2.estudiantes)  # ['Ana', 'Juan']

# Solución: usar atributos de instancia
class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []  # Cada instancia tiene su propia lista
    
    def agregar_estudiante(self, nombre):
        self.estudiantes.append(nombre)

c1 = Curso("Matemáticas")
c2 = Curso("Historia")

c1.agregar_estudiante("Ana")
c2.agregar_estudiante("Juan")

print(c1.estudiantes)  # ['Ana']
print(c2.estudiantes)  # ['Juan']
```

### Contador de instancias

```python
class Persona:
    contador = 0  # Atributo de clase
    
    def __init__(self, nombre):
        self.nombre = nombre
        Persona.contador += 1
    
    @classmethod
    def obtener_contador(cls):
        return cls.contador

p1 = Persona("Ana")
p2 = Persona("Juan")
p3 = Persona("Pedro")

print(Persona.obtener_contador())  # 3
print(p1.contador)                 # 3
print(p2.contador)                 # 3
```

---

## 9. Atributos y Métodos Estáticos

### Métodos Estáticos

```python
class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b
    
    @staticmethod
    def restar(a, b):
        return a - b
    
    @staticmethod
    def es_par(numero):
        return numero % 2 == 0

# Uso sin crear instancia
print(Calculadora.sumar(5, 3))    # 8
print(Calculadora.restar(10, 4))  # 6
print(Calculadora.es_par(4))      # True

# También funciona con instancia
calc = Calculadora()
print(calc.sumar(2, 2))  # 4
```

### Diferencias entre @staticmethod, @classmethod y método normal

```python
class Ejemplo:
    atributo_clase = "Valor clase"
    
    def __init__(self, valor):
        self.valor = valor  # Atributo de instancia
    
    def metodo_normal(self):
        # Tiene acceso a self (instancia)
        return f"Normal: {self.valor}"
    
    @classmethod
    def metodo_clase(cls):
        # Tiene acceso a la clase
        return f"Clase: {cls.atributo_clase}"
    
    @staticmethod
    def metodo_estatico():
        # No tiene acceso a self ni cls
        return "Estático: sin acceso"

e = Ejemplo(10)

print(e.metodo_normal())    # Normal: 10
print(e.metodo_clase())     # Clase: Valor clase
print(e.metodo_estatico())  # Estático: sin acceso

# También funciona desde la clase
print(Ejemplo.metodo_clase())    # Clase: Valor clase
print(Ejemplo.metodo_estatico()) # Estático: sin acceso
# print(Ejemplo.metodo_normal()) # Error, necesita self
```

---

## 10. Herencia Avanzada

### super() con múltiples niveles

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        return "..."

class Mamifero(Animal):
    def __init__(self, nombre, tipo_piel):
        super().__init__(nombre)
        self.tipo_piel = tipo_piel
    
    def amamantar(self):
        return f"{self.nombre} está amamantando"

class Perro(Mamifero):
    def __init__(self, nombre, raza):
        super().__init__(nombre, "Pelaje")
        self.raza = raza
    
    def hablar(self):
        return "Guau!"

perro = Perro("Rex", "Pastor Alemán")
print(perro.nombre)       # Rex
print(perro.tipo_piel)    # Pelaje
print(perro.raza)         # Pastor Alemán
print(perro.hablar())     # Guau!
print(perro.amamantar())  # Rex está amamantando
```

### isinstance() y issubclass()

```python
class Animal:
    pass

class Perro(Animal):
    pass

class Cachorro(Perro):
    pass

c = Cachorro()

print(isinstance(c, Cachorro))    # True
print(isinstance(c, Perro))       # True
print(isinstance(c, Animal))       # True
print(isinstance(c, str))          # False

print(issubclass(Cachorro, Perro))   # True
print(issubclass(Cachorro, Animal))  # True
print(issubclass(Perro, Cachorro))    # False
```

### Mixins (Herencia múltiple práctica)

```python
class Volador:
    def volar(self):
        return f"{self.nombre} vuela"

class Nadador:
    def nadar(self):
        return f"{self.nombre} nada"

class Terrestre:
    def caminar(self):
        return f"{self.nombre} camina"

class Pato(Volador, Nadador, Terrestre):
    def __init__(self, nombre):
        self.nombre = nombre

pato = Pato("Donald")
print(pato.volar())    # Donald vuela
print(pato.nadar())    # Donald nada
print(pato.caminar())  # Donald camina
```

---

## 11. Iteración Pythonic

### Listas

```python
# Iteración básica
numeros = [1, 2, 3, 4, 5]
for n in numeros:
    print(n)

# enumerate - obtener índice y valor
for i, n in enumerate(numeros):
    print(f"Índice {i}: {n}")

# range con inicio y paso
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

# List comprehension
cuadrados = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# List comprehension con condición
pares = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# zip - recorrer múltiples listas
nombres = ["Ana", "Juan", "Pedro"]
edades = [25, 30, 35]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")
```

### Diccionarios

```python
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

# Iterar claves
for clave in persona:
    print(clave)

# Iterar valores
for valor in persona.values():
    print(valor)

# Iterar clave-valor
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Dictionary comprehension
cuadrados = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Filtrar diccionario
mayores = {k: v for k, v in persona.items() if k != "ciudad"}
```

### Tuplas

```python
# Tuplas son inmutables
coordenadas = (10, 20, 30)

# Iterar tupla
for coord in coordenadas:
    print(coord)

# Desempaquetado
x, y, z = coordenadas
print(f"x={x}, y={y}, z={z}")

# enumerate
for i, valor in enumerate(coordenadas):
    print(f"Posición {i}: {valor}")

# Tuple unpacking con *
a, *b, c = (1, 2, 3, 4, 5)
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5
```

### Sets

```python
colores = {"rojo", "verde", "azul"}

# Iterar set
for color in colores:
    print(color)

# Set comprehension
cuadrados_set = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}

# Operaciones de conjuntos
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Unión: {1, 2, 3, 4, 5}
print(a & b)  # Intersección: {3}
print(a - b)  # Diferencia: {1, 2}
print(a ^ b)  # Diferencia simétrica: {1, 2, 4, 5}
```

---

## 12. Validación Pythonic

### all() y any()

```python
numeros = [2, 4, 6, 8, 10]

# all - todos deben cumplir condición
print(all(x % 2 == 0 for x in numeros))  # True (todos pares)

# any - al menos uno cumple condición
print(any(x > 8 for x in numeros))  # True (10 > 8)

# Validar lista no vacía
usuarios = []
print(all(usuarios))  # False (vacía)

# Validar con all en diccionarios
datos = {"nombre": "Ana", "edad": 25, "email": "ana@email.com"}
print(all(datos.values()))  # True (ninguno es vacío)
```

### Checks típicos

```python
# Verificar tipo
print(isinstance("hola", str))      # True
print(isinstance(123, int))         # True
print(isinstance([1, 2], list))     # True

# Verificar contenido en strings
texto = "Hola mundo Python"
print("Python" in texto)       # True
print("java" in texto)         # False

# startswith / endswith
print(texto.startswith("Hola"))   # True
print(texto.endswith("on"))       # True

# Verificar si es número
print("123".isdigit())    # True
print("12a".isdigit())    # False
print("abc".isalpha())    # True

# Verificar mayúsculas/minúsculas
print("hola".islower())   # True
print("HOLA".isupper())   # True
print("Hola".istitle())   # True

# Verificar si es alfanumérico
print("abc123".isalnum())  # True
print("abc 123".isalnum()) # False (espacio)
```

### Validaciones funcionales

```python
from functools import reduce

# Filtrar y validar
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Encontrar primeros que cumplan condición
mayores = list(filter(lambda x: x > 5, numeros))  # [6, 7, 8, 9, 10]

# Mapear validación
valores = ["123", "abc", "456", "def"]
numericos = list(filter(str.isdigit, valores))  # ['123', '456']

# Validar con reduce
def validar_suma(lista, umbral):
    return reduce(lambda a, b: a + b, lista, 0) <= umbral

print(validar_suma([1, 2, 3], 10))  # True (6 <= 10)
print(validar_suma([1, 2, 3], 5))  # False (6 > 5)
```

### Validación con match (Python 3.10+)

```python
def procesar_tipo(dato):
    match dato:
        case int() if dato > 0:
            return f"Entero positivo: {dato}"
        case int():
            return f"Entero negativo: {dato}"
        case str() if len(dato) > 5:
            return f"String largo: {dato}"
        case str():
            return f"String corto: {dato}"
        case list():
            return f"Lista con {len(dato)} elementos"
        case _:
            return "Tipo desconocido"

print(procesar_tipo(10))      # Entero positivo: 10
print(procesar_tipo("hola"))  # String corto: hola
print(procesar_tipo([1,2,3]))# Lista con 3 elementos
```

---

## 13. Strings Pythonic

### Formateo moderno

```python
nombre = "Ana"
edad = 25

# f-strings (recomendado)
print(f"Hola, {nombre}. Tienes {edad} años.")

# Expresiones en f-strings
print(f"El año que viene tendrás {edad + 1} años.")

# F-string con estructuras
datos = {"x": 10, "y": 20}
print(f"Coordenadas: ({datos['x']}, {datos['y']})")

# Format specifiers
pi = 3.14159
print(f"Pi: {pi:.2f}")  # Pi: 3.14
print(f"Pi: {pi:10.2f}")  # Pi:       3.14

# Alineación
print(f"{'izq':<10} | {'centro':^10} | {'der':>10}")
print(f"{'---':<10} | {'---':^10} | {'---':>10}")
```

### Métodos útiles de strings

```python
texto = "  Hola Mundo, Python es genial!  "

# Limpieza
print(texto.strip())      # "Hola Mundo, Python es genial!"
print(texto.lower())      # "  hola mundo, python es genial!  "
print(texto.upper())      # "  HOLA MUNDO, PYTHON ES GENIAL!  "
print(texto.capitalize()) # "  hola mundo, python es genial!  "
print(texto.title())      # "  Hola Mundo, Python Es Genial!  "

# División y unión
palabras = texto.strip().split(" ")  # ['Hola', 'Mundo,', 'Python', 'es', 'genial!']
print("-".join(palabras))  # Hola-Mundo,-Python-es-genial!

# Reemplazo
print(texto.replace("Python", "Java"))  # "  Hola Mundo, Java es genial!  "

# División avanzada
lineas = "uno\ndos\ntres".split("\n")  # ['uno', 'dos', 'tres']

# Partición
"hola@email.com".partition("@")  # ('hola', '@', 'email.com')
```

### Slicing y manipulación

```python
texto = "Python Programación"

# Slicing
print(texto[0:6])     # Python
print(texto[7:])      # Programación
print(texto[-4:])     # ción
print(texto[::2])     # Pto rgaain (cada 2 caracteres)
print(texto[::-1])    # inversión: nóicamargorP nohtyP

# Buscar
print(texto.find("ram"))   # 10 (índice)
print(texto.count("o"))    # 2 (ocurrencias)
print(texto.startswith("Pyt"))  # True

# Validación
print(texto.isalpha())     # False (hay espacios)
print("123".isnumeric())   # True
print("abc".isidentifier()) # True (válido como nombre)
```

---

## 14. Estructuras de Datos Avanzadas

### defaultdict

```python
from collections import defaultdict

# Crea valores por defecto automáticamente
d = defaultdict(list)  # Valor por defecto: lista vacía
d["frutas"].append("manzana")
d["frutas"].append("pera")
d["frutas"].append("uva")
print(d)  # defaultdict(<class 'list'>, {'frutas': ['manzana', 'pera', 'uva']})

d2 = defaultdict(int)  # Valor por defecto: 0
d2["contador"] += 1
d2["contador"] += 1
print(d2)  # defaultdict(<class 'int'>, {'contador': 2})
```

### Counter

```python
from collections import Counter

# Contar elementos
frutas = ["manzana", "pera", "manzana", "uva", "pera", "manzana"]
contador = Counter(frutas)
print(contador)  # Counter({'manzana': 3, 'pera': 2, 'uva': 1})

# Más común
print(contador.most_common(2))  # [('manzana', 3), ('pera', 2)]

# Contar letras en string
letras = Counter("abracadabra")
print(letras)  # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
```

### namedtuple

```python
from collections import namedtuple

# Crear estructura de datos con nombres
Punto = namedtuple('Punto', ['x', 'y'])
Rectangulo = namedtuple('Rectangulo', 'ancho alto')

p = Punto(10, 20)
print(p.x, p.y)      # 10 20
print(p[0], p[1])    # 10 20 (también funciona como tupla)

# Namedtuple con valores por defecto
Pagina = namedtuple('Pagina', ['numero', 'contenido'], defaults=[1, ''])
pag = Pagina(contenido="Hola")
print(pag.numero)  # 1 (valor por defecto)
```

### Deque

```python
from collections import deque

# Cola de doble extremos (más rápido que list para pops)
cola = deque([1, 2, 3])
cola.append(4)      # [1, 2, 3, 4]
cola.appendleft(0)  # [0, 1, 2, 3, 4]
cola.pop()          # Retorna 4, cola = [0, 1, 2, 3]
cola.popleft()      # Retorna 0, cola = [1, 2, 3]

# Limitar tamaño
cola_limitada = deque(maxlen=3)
cola_limitada.append(1)
cola_limitada.append(2)
cola_limitada.append(3)
cola_limitada.append(4)  # Desbordamiento: [2, 3, 4]
```

---

## Resumen Rápido

| Concepto | Palabra clave | Uso principal |
|----------|---------------|----------------|
| Herencia | `class Hija(Padre)` | Reutilizar código |
| Herencia múltiple | `class Hija(Padre1, Padre2)` | Múltiples funcionalidades |
| Abstract | `@abstractmethod` | Definir contratos |
| Property | `@property` | Validación de acceso |
| Visibilidad | `_protegido`, `__privado` | Encapsulamiento |
| Metaclass | `metaclass=Nueva` | Controlar creación de clases |
| Dunder | `__metodo__` | Comportamiento especial |
| Mixins | `class Mixin:` | Reutilizar métodos |
| Comprehensions | `[x for x in lista]` | Crear colecciones |
| enumerate | `for i, v in enumerate()` | Índice y valor |
