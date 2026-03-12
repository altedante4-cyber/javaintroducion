# Herencia en Python - Nivel Medio

## 1. Herencia con `@property`

Las propiedades (`@property`) permiten acceder a atributos como si fueran variables, pero ejecutando código personalizado.

```python
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Convención: _ indica que es privado
        self._edad = edad
    
    @property
    def nombre(self):
        """Permite leer el atributo"""
        return self._nombre.upper()
    
    @nombre.setter
    def nombre(self, valor):
        """Permite modificar el atributo con validación"""
        if len(valor) > 2:
            self._nombre = valor
        else:
            print("El nombre debe tener más de 2 caracteres")
    
    @property
    def es_mayor_edad(self):
        """Propiedad calculada"""
        return self._edad >= 18

class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.matricula = matricula
    
    @property
    def estado_academico(self):
        if self.es_mayor_edad:
            return "Estudiante de universiad"
        else:
            return "Estudiante de preparatoria"

# Uso
est = Estudiante("Juan", 20, "2024001")
print(est.nombre)  # JUAN (usa @property)
est.nombre = "Carlos"  # Usa el setter
print(est.estado_academico)  # Estudiante de universidad
```

## 2. `@classmethod` y `@staticmethod`

### Métodos de clase (`@classmethod`)
Reciben la clase como primer parámetro (`cls`), no la instancia.

```python
class Producto:
    cantidad_total = 0
    
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        Producto.cantidad_total += 1
    
    @classmethod
    def crear_oferta(cls, nombre, precio_original, descuento):
        """Método de clase para crear con descuento"""
        precio_final = precio_original * (1 - descuento/100)
        return cls(nombre, precio_final)
    
    @classmethod
    def obtener_total_productos(cls):
        """Retorna el total de productos creados"""
        return cls.cantidad_total

# Uso
p1 = Producto("Laptop", 1000)
p2 = Producto.crear_oferta("Mouse", 50, 20)  # 20% descuento
print(Producto.obtener_total_productos())  # 2
```

### Métodos estáticos (`@staticmethod`)
No reciben `self` ni `cls`. Son funciones dentro de la clase.

```python
class Calculadora:
    @staticmethod
    def sumar(a, b):
        """Función estática sin acceso a instancia"""
        return a + b
    
    @staticmethod
    def validar_numero(valor):
        """Validación sin acceso a la clase"""
        return isinstance(valor, (int, float))

# Uso
resultado = Calculadora.sumar(5, 3)  # 8
print(Calculadora.validar_numero(10))  # True
print(Calculadora.validar_numero("10"))  # False
```

## 3. Trabajar con Colecciones (Listas, Tuplas, Sets, Diccionarios)

### Listas y métodos
```python
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []  # Lista de libros
    
    def agregar_libro(self, titulo, autor):
        self.libros.append({"titulo": titulo, "autor": autor})
    
    def obtener_titulos(self):
        """Retorna lista de títulos"""
        return [libro["titulo"] for libro in self.libros]
    
    def listar_libros(self):
        for i, libro in enumerate(self.libros, 1):
            print(f"{i}. {libro['titulo']} - {libro['autor']}")

# Uso
bib = Biblioteca("Central")
bib.agregar_libro("El Quijote", "Cervantes")
bib.agregar_libro("García Márquez", "Cien años...")
bib.listar_libros()
```

### Tuplas (inmutables)
```python
class Punto3D:
    def __init__(self, x, y, z):
        self.coordenadas = (x, y, z)  # Tupla inmutable
    
    def desempacar(self):
        x, y, z = self.coordenadas
        return f"X: {x}, Y: {y}, Z: {z}"

# Uso
p = Punto3D(1, 2, 3)
print(p.desempacar())  # X: 1, Y: 2, Z: 3
```

### Sets (conjuntos únicos)
```python
class Grupo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.miembros = set()  # Set para evitar duplicados
    
    def agregar_miembro(self, miembro):
        self.miembros.add(miembro)
    
    def obtener_miembros_unicos(self):
        return len(self.miembros)
    
    def combinar_con(self, otro_grupo):
        """Combina dos grupos"""
        grupo_combinado = self.miembros | otro_grupo.miembros
        return grupo_combinado

# Uso
g1 = Grupo("Programadores")
g1.agregar_miembro("Ana")
g1.agregar_miembro("Bob")
g1.agregar_miembro("Ana")  # No se duplica

g2 = Grupo("Diseñadores")
g2.agregar_miembro("Carlos")
g2.agregar_miembro("Bob")

print(f"Miembros únicos G1: {g1.obtener_miembros_unicos()}")  # 2
print(g1.combinar_con(g2))  # {'Ana', 'Bob', 'Carlos'}
```

### Diccionarios (clave-valor)
```python
class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.movimientos = {}  # Diccionario para historial
    
    def registrar_transaccion(self, fecha, tipo, monto):
        if fecha not in self.movimientos:
            self.movimientos[fecha] = []
        self.movimientos[fecha].append({"tipo": tipo, "monto": monto})
    
    def obtener_movimientos_por_fecha(self, fecha):
        return self.movimientos.get(fecha, [])
    
    def resumen_transacciones(self):
        for fecha, transacciones in self.movimientos.items():
            print(f"\n{fecha}:")
            for t in transacciones:
                print(f"  {t['tipo']}: ${t['monto']}")

# Uso
cuenta = CuentaBancaria("Juan Pérez")
cuenta.registrar_transaccion("2026-03-12", "Depósito", 500)
cuenta.registrar_transaccion("2026-03-12", "Retiro", 100)
cuenta.registrar_transaccion("2026-03-13", "Depósito", 200)
cuenta.resumen_transacciones()
```

## 4. F-Strings Avanzados

Los f-strings permiten formatear strings de forma elegante.

```python
class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento
    
    def __str__(self):
        # F-string básico
        return f"Empleado: {self.nombre}"
    
    def resumen_laboral(self):
        # F-string con expresiones
        incremento = self.salario * 0.10
        nuevo_salario = self.salario + incremento
        return f"""
        Nombre: {self.nombre.upper()}
        Salario actual: ${self.salario:,.2f}
        Con incremento 10%: ${nuevo_salario:,.2f}
        Departamento: {self.departamento}
        """
    
    def comparar_salarios(self, otro_empleado):
        diferencia = abs(self.salario - otro_empleado.salario)
        quien_gana_mas = "Yo" if self.salario > otro_empleado.salario else "Él/Ella"
        return f"{self.nombre} vs {otro_empleado.nombre}: Diferencia ${diferencia:,.2f} ({quien_gana_mas} gana más)"

# Ejemplos
emp1 = Empleado("María García", 1500, "Ventas")
emp2 = Empleado("Luis Rodríguez", 1800, "Desarrollo")

print(emp1.resumen_laboral())
print(emp1.comparar_salarios(emp2))

# F-strings con formateo
print(f"Nombre: {emp1.nombre:<20} Salario: ${emp1.salario:>10.2f}")
print(f"Valor booleano: {emp1.salario > 2000!r}")
```

### Formateo avanzado de f-strings
```python
# Formato de números
precio = 1999.5
print(f"Precio: ${precio:.2f}")  # $1999.50
print(f"Precio: ${precio:,.2f}")  # $1,999.50

# Alineación
nombre = "Juan"
print(f"{nombre:<10} izquierda")      # Juan       izquierda
print(f"{nombre:>10} derecha")        # Juan       derecha
print(f"{nombre:^10} centro")         # Juan       centro

# Expresiones dentro de f-strings
edad = 25
print(f"En 5 años tendré {edad + 5} años")
lista = [1, 2, 3]
print(f"Largo de lista: {len(lista)}")
```

---

## Ejercicios

### Ejercicio 1: Sistema de Biblioteca con Herencia

**Enunciado:**

Crea un sistema de biblioteca con las siguientes clases:

- **Clase `Recurso` (Padre):**
  - Atributos: `titulo`, `autor`, `año_publicacion`, `disponible` (booleano)
  - Método: `prestar()` y `devolver()`
  - Propiedad: `estado` (retorna "Disponible" o "Prestado")

- **Clase `Libro` (Hereda de Recurso):**
  - Atributos adicionales: `paginas`, `editorial`
  - Método estático: `validar_isbn(isbn)` (retorna True si tiene 10 o 13 dígitos)

- **Clase `Revista` (Hereda de Recurso):**
  - Atributos adicionales: `numero`, `categoria`
  - Método de clase: `contar_revistas()` (cuenta total de revistas creadas)

- **Clase `Biblioteca`:**
  - Usar un diccionario para almacenar recursos por ID
  - Usar una lista para el historial de préstamos (tuplas de (recurso, fecha, usuario))
  - Usar un set para los usuarios registrados
  - Métodos: `agregar_recurso()`, `prestar_recurso()`, `devolver_recurso()`, `listar_disponibles()`
  - Una propiedad que retorne el porcentaje de ocupación

**Requisitos:**
- Usa `@property`, `@classmethod`, `@staticmethod`
- Usa f-strings para mostrar reportes
- Imprime un resumen completo con diccionarios, listas, tuplas y sets

---

### Ejercicio 2: Sistema de Gestión de Videojuego con Jugadores

**Enunciado:**

Crea un sistema de videojuego con las siguientes clases:

- **Clase `Personaje` (Padre):**
  - Atributos: `nombre`, `nivel`, `experiencia`, `inventario` (diccionario con items)
  - Método: `ganar_experiencia(cantidad)` (calcula nuevo nivel)
  - Propiedad: `proximo_nivel` (experiencia para el siguiente nivel)

- **Clase `Guerrero` (Hereda de Personaje):**
  - Atributo: `fuerza` (0-100)
  - Método: `atacar(enemigo)` (retorna daño basado en fuerza)
  - Método estático: `calcular_daño(fuerza, defensa)`

- **Clase `Mago` (Hereda de Personaje):**
  - Atributo: `mana` (0-100)
  - Método: `lanzar_hechizo(hechizo)` (gasta mana)
  - Método de clase: `hechizos_disponibles()` (retorna lista de hechizos)

- **Clase `Partida`:**
  - Usar un diccionario para almacenar jugadores
  - Usar una lista para el historial de eventos (tuplas)
  - Usar un set para los jugadores activos
  - Método: `crear_reportes_json()` con f-strings

**Requisitos:**
- Implementa herencia multinivel si es necesario
- Usa f-strings con formateo de números (oro, daño, etc.)
- Muestra reportes con diccionarios, listas, tuplas y sets
- Uso obligatorio de `@property`, `@classmethod`, `@staticmethod`

---

## Sección de Práctica con F-Strings

Crea un archivo `practica_fstrings.py` y completa los siguientes ejercicios:

```python
# 1. Formatea estos datos con f-strings
nombre = "Carlos"
edad = 28
salario = 2500.75
ciudad = "Madrid"

# Imprime: "Carlos (28 años) de Madrid gana $2,500.75"
resultado_1 = f""  # COMPLETA AQUÍ

# 2. Tabla alineada con f-strings
productos = [
    {"nombre": "Laptop", "precio": 1200},
    {"nombre": "Mouse", "precio": 25.50},
    {"nombre": "Teclado", "precio": 75}
]

# Imprime una tabla con:
# - Nombre: 20 caracteres, izquierda
# - Precio: 10 caracteres, derecha, 2 decimales

# 3. Calcula datos con f-strings
numeros = [10, 20, 30, 40]
promedio = sum(numeros) / len(numeros)

# Imprime: f"Promedio de [10, 20, 30, 40] es 25.00"
# Usando f-string que calcule el promedio dentro

# 4. Formato de porcentaje y booleanos
aprobados = 45
total = 50
porcentaje = (aprobados / total) * 100

# Imprime con f-string: "45 de 50 estudiantes aprobaron (90.00%)"
resultado_4 = f""  # COMPLETA AQUÍ

# 5. F-string condicional
intento = 3
max_intentos = 5

# Imprime: "Intento 3 de 5. Tienes 2 intentos restantes. SIGUE"
# Si intento < max_intentos
# Si no: "NO TE QUEDAN INTENTOS"
resultado_5 = f""  # COMPLETA AQUÍ
```

---

## Cheat Sheet: Resumen Rápido

| Concepto | Uso |
|----------|-----|
| `@property` | Acceder a método como atributo |
| `@nombre.setter` | Modificar propiedad con validación |
| `@classmethod` | Método que recibe la clase (cls) |
| `@staticmethod` | Función dentro de clase, sin cls/self |
| `super()` | Acceder a método de la clase padre |
| Lista | `[1, 2, 3]` - Mutable, ordenada |
| Tupla | `(1, 2, 3)` - Inmutable, ordenada |
| Set | `{1, 2, 3}` - Único, sin orden |
| Dict | `{"key": "value"}` - Clave-valor |
| f-string | `f"{var:.2f}"` - Formateo elegante |

---

## Recursos adicionales

- Documentación oficial: [Python Docs](https://docs.python.org/3/)
- Real Python Herencia: https://realpython.com/inheritance-composition-python/
- F-strings: https://docs.python.org/3/tutorial/inputoutput.html#tut-fformatting
