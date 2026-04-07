wq# Métodos Pythonic - Referencia Completa

## 1. Listas (List)

### Agregación

```python
numeros = [1, 2, 3]

# append - agregar un elemento
numeros.append(4)           # [1, 2, 3, 4]

# extend - agregar varios elementos
numeros.extend([5, 6])       # [1, 2, 3, 4, 5, 6]

# insert - agregar en posición específica
numeros.insert(0, 0)         # [0, 1, 2, 3, 4, 5, 6]

# + operador
nueva = numeros + [7, 8]    # [1, 2, 3, 4, 5, 6, 7, 8]

# += con extend
numeros += [9, 10]           # [1, 2, 3, 4, 5, 6, 9, 10]

#列表推导式
cuadrados = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

#repeat
repeticiones = [1, 2] * 3    # [1, 2, 1, 2, 1, 2]
```

### Eliminación

```python
numeros = [1, 2, 3, 4, 5, 3]

# remove - elimina primera ocurrencia
numeros.remove(3)            # [1, 2, 4, 5, 3]

# pop - elimina y retorna por índice
eliminado = numeros.pop()    # elimina 3, retorna 3
eliminado = numeros.pop(0)   # elimina 1, retorna 1

# del - elimina por índice
del numeros[0]

# clear - elimina todo
numeros.clear()              # []

# filter - eliminar con condición
numeros = [1, 2, 3, 4, 5, 6]
numeros = [x for x in numeros if x % 2 != 0]  # [1, 3, 5]

# removeall - eliminar todos los duplicados
numeros = [1, 2, 2, 3, 3, 3]
numeros = list(set(numeros))  # [1, 2, 3]
```

### Búsqueda

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# index - buscar índice
idx = numeros.index(5)        # 4
#idx = numeros.index(5, 0, 3) # con rango

# count - contar ocurrencias
count = numeros.count(3)     # 1

# in - verificar existencia
existe = 5 in numeros        # True
existe = 15 in numeros       # False

# find - no existe en listas, usar index con try
try:
    idx = numeros.index(15)
except ValueError:
    idx = -1

# Buscar con enumerate
for i, valor in enumerate(numeros):
    if valor == 5:
        print(f"Encontrado en índice {i}")
        break

# Buscar primero que cumpla condición
resultado = next((x for x in numeros if x > 5), None)  # 6
```

### Ordenamiento

```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6]

# sort - ordena in-place
numeros.sort()               # [1, 1, 2, 3, 4, 5, 6, 9]
numeros.sort(reverse=True)   # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted - retorna nueva lista
ordenado = sorted(numeros)   # [1, 1, 2, 3, 4, 5, 6, 9]

# sort con key
nombres = ["ana", "Carlos", "beatriz"]
nombres.sort(key=str.lower)   # ['ana', 'beatriz', 'Carlos']

# sort con key compleja
personas = [("Ana", 25), ("Juan", 30), ("Pedro", 20)]
personas.sort(key=lambda x: x[1])  # Por edad
# [('Pedro', 20), ('Ana', 25), ('Juan', 30)]
```

### Duplicados

```python
numeros = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# set - eliminar duplicados
unicos = list(set(numeros))           # [1, 2, 3, 4]

# preservar orden con dict.fromkeys
unicos = list(dict.fromkeys(numeros))  # [1, 2, 3, 4]

# encontrar duplicados
duplicados = [x for x in set(numeros) if numeros.count(x) > 1]  # [2, 3, 4]

# Counter para duplicados
from collections import Counter
conteo = Counter(numeros)
duplicados = [k for k, v in conteo.items() if v > 1]  # [2, 3, 4]

# Eliminar duplicados con condición
datos = [1, 2, 2, 3, 4, 4, 5]
unicos = []
for x in datos:
    if x not in unicos:
        unicos.append(x)
# O usando una lista auxiliar para limpiar duplicados mientras se preserva orden
seen = set()
unicos = [x for x in datos if not (x in seen or seen.add(x))]
```

---

## 2. Diccionarios (Dict)

### Agregación

```python
datos = {}

# Asignación directa
datos["nombre"] = "Ana"
datos["edad"] = 25

# update - agregar varios
datos.update({"ciudad": "Madrid", "pais": "España"})

# setdefault - agregar solo si no existe
datos.setdefault("telefono", "000000000")

# fromkeys - crear dict con valores por defecto
keys = ["a", "b", "c"]
dict_default = dict.fromkeys(keys, 0)  # {'a': 0, 'b': 0, 'c': 0}

# Dictionary comprehension
cuadrados = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# merge con |
d1 = {"a": 1}
d2 = {"b": 2}
d3 = d1 | d2  # {'a': 1, 'b': 2}

# update con |= (Python 3.9+)
d1 |= d2  # {'a': 1, 'b': 2}
```

### Eliminación

```python
datos = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid", "pais": "España"}

# pop - eliminar y retornar
eliminado = datos.pop("pais")      # 'España', datos ya no tiene 'pais'

# pop con valor por defecto
eliminado = datos.pop("telefono", None)  # None si no existe

# popitem - eliminar último par
clave, valor = datos.popitem()

# del - eliminar
del datos["ciudad"]

# clear - limpiar todo
datos.clear()

# Eliminar con condición
datos = {"a": 1, "b": 2, "c": 3, "d": 4}
datos = {k: v for k, v in datos.items() if v > 2}  # {'c': 3, 'd': 4}

# Eliminar claves específicas
claves_eliminar = ["a", "c"]
datos = {k: v for k, v in datos.items() if k not in claves_eliminar}
```

### Búsqueda

```python
datos = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

# Acceso directo
print(datos["nombre"])  # Ana

# get - acceso seguro
print(datos.get("nombre"))          # Ana
print(datos.get("telefono"))        # None
print(datos.get("telefono", "N/A"))  # N/A

# in - verificar clave
print("nombre" in datos)    # True
print("telefono" in datos)  # False

# keys, values, items
print(datos.keys())    # dict_keys(['nombre', 'edad', 'ciudad'])
print(datos.values())  # dict_values(['Ana', 25, 'Madrid'])
print(datos.items())  # dict_items([('nombre', 'Ana'), ...])

# Buscar por valor
for clave, valor in datos.items():
    if valor == 25:
        print(f"Encontrado: {clave}")  # edad

# Buscar con next
clave_encontrada = next((k for k, v in datos.items() if v == 25), None)

# Buscar múltiples
coincidencias = [k for k, v in datos.items() if "a" in str(v)]
```

### Duplicados

```python
# Por definición, las claves son únicas
datos = {"a": 1, "a": 2}  # {'a': 2} - se sobrescribe

# Mergear diccionarios (evitar sobrescritura)
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

# Combinar sin perder datos
combinado = {**d1, **d2}  # {'a': 1, 'b': 3, 'c': 4}

# Combinar sumando valores de claves duplicadas
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
combinado = {}
for k in set(list(d1.keys()) + list(d2.keys())):
    combinado[k] = d1.get(k, 0) + d2.get(k, 0)  # {'a': 1, 'b': 5, 'c': 4}

# defaultdict para contar
from collections import defaultdict
contador = defaultdict(int)
for palabra in ["a", "b", "a", "c", "b", "a"]:
    contador[palabra] += 1
print(dict(contador))  # {'a': 3, 'b': 2, 'c': 1}
```

---

## 3. Sets

### Agregación

```python
colores = {"rojo", "verde"}

# add - agregar uno
colores.add("azul")        # {'rojo', 'verde', 'azul'}

# update - agregar varios
colores.update(["amarillo", "negro"])  # {'rojo', 'verde', 'azul', 'amarillo', 'negro'}

# | operador (unión)
a = {1, 2, 3}
b = {3, 4, 5}
c = a | b                 # {1, 2, 3, 4, 5}

# |= (update)
a |= {6, 7}

# Set comprehension
cuadrados = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}
```

### Eliminación

```python
colores = {"rojo", "verde", "azul", "amarillo"}

# remove - elimina, error si no existe
colores.remove("amarillo")  # {'rojo', 'verde', 'azul'}
# colores.remove("blanco")  # KeyError

# discard - elimina, no error si no existe
colores.discard("blanco")   # No error

# pop - elimina y retorna uno arbitrario
eliminado = colores.pop()   # Elimina un elemento aleatorio

# clear - limpiar
colores.clear()

# Eliminar con condición
colores = {"rojo", "verde", "azul", "amarillo"}
colores = {c for c in colores if c != "amarillo"}
```

### Búsqueda

```python
colores = {"rojo", "verde", "azul"}

# in - verificar existencia
print("rojo" in colores)    # True
print("blanco" in colores)  # False

# issubset - es subconjunto
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))  # True

# issuperset - es superconjunto
print(b.issuperset(a))  # True

# isdisjoint - sin elementos en común
c = {5, 6}
print(a.isdisjoint(c))  # True

# iterar
for color in colores:
    print(color)
```

### Duplicados

```python
# Por definición, no hay duplicados en sets
numeros = {1, 2, 2, 3, 3, 3}
print(numeros)  # {1, 2, 3}

# Encontrar elementos únicos en dos listas
l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]

solo_l1 = set(l1) - set(l2)      # {1, 2} - solo en l1
solo_l2 = set(l2) - set(l1)      # {5, 6} - solo en l2
comunes = set(l1) & set(l2)      # {3, 4} - en ambos
todos = set(l1) | set(l2)        # {1, 2, 3, 4, 5, 6} - todos

# Diferencia simétrica
diferentes = set(l1) ^ set(l2)    # {1, 2, 5, 6} - en uno u otro, no en ambos
```

---

## 4. Tuplas

### Agregación

```python
# Las tuplas son inmutables, pero podemos crear nuevas

tupla = (1, 2, 3)

# + operador
nueva = tupla + (4, 5)       # (1, 2, 3, 4, 5)

# * operador (repetición)
repetida = tupla * 2          # (1, 2, 3, 1, 2, 3)

# tuple() - convertir de otra secuencia
desde_lista = tuple([1, 2, 3])     # (1, 2, 3)
desde_string = tuple("hola")       # ('h', 'o', 'l', 'a')
desde_range = tuple(range(5))       # (0, 1, 2, 3, 4)
```

### Eliminación

```python
# No se pueden eliminar elementos de tuplas
# Solo se puede eliminar la tupla completa

tupla = (1, 2, 3, 4, 5)

# Eliminar elementos con condición
tupla = tuple(x for x in tupla if x != 3)  # (1, 2, 4, 5)

# Slice para eliminar
tupla = tupla[:2] + tupla[3:]  # Eliminar elemento en índice 2
```

### Búsqueda

```python
tupla = (1, 2, 3, 4, 5, 3)

# index
idx = tupla.index(3)          # 2 (primera ocurrencia)
idx = tupla.index(3, 3)       # 5 (desde índice 3)

# count
count = tupla.count(3)         # 2

# in
print(3 in tupla)              # True

# Buscar con enumerate
for i, valor in enumerate(tupla):
    if valor == 3:
        print(f"Índice: {i}")
        break
```

### Duplicados

```python
tupla = (1, 2, 2, 3, 3, 3)

# Convertir a set y volver a tuple
unica = tuple(set(tupla))  # (1, 2, 3) - orden puede variar

# Preservar orden
from collections import OrderedDict
unica = tuple(OrderedDict.fromkeys(tupla))  # (1, 2, 3)

# Contar duplicados
from collections import Counter
conteo = Counter(tupla)
print(conteo)  # Counter({3: 3, 2: 2, 1: 1})
```

---

## 5. Strings

### Agregación

```python
# Concatenación
nombre = "Hola" + " " + "Mundo"    # "Hola Mundo"

# join
palabras = ["Hola", "Mundo", "Python"]
oracion = " ".join(palabras)       # "Hola Mundo Python"
oracion = "-".join(palabras)       # "Hola-Mundo-Python"

# f-strings
edad = 25
texto = f"Tengo {edad} años"      # "Tengo 25 años"

# format
texto = "Soy {} y tengo {} años".format("Ana", 25)

# * (repetición)
linea = "-" * 20                  # "--------------------"

# startswith / endswith
print("archivo.txt".endswith(".txt"))  # True
```

### Eliminación

```python
texto = "   Hola Mundo   "

# strip - eliminar espacios al inicio y final
print(texto.strip())              # "Hola Mundo"

# lstrip - solo izquierda
print(texto.lstrip())             # "Hola Mundo   "

# rstrip - solo derecha
print(texto.rstrip())             # "   Hola Mundo"

# replace
print(texto.replace("Mundo", "Python"))  # "   Hola Python   "

# replace con contador
print("aaabbbccc".replace("a", "x", 2))  # "xxabbccc"

# Eliminar caracteres específicos
import string
texto = "Hola, Mundo!"
texto = texto.translate(str.maketrans("", "", ",!"))  # "Hola Mundo"
```

### Búsqueda

```python
texto = "Hola Mundo, Python es genial"

# find - retorna índice o -1
idx = texto.find("Mundo")         # 5
idx = texto.find("Java")          # -1

# index - igual pero lanza error
idx = texto.index("Mundo")        # 5
# idx = texto.index("Java")      # ValueError

# count
print(texto.count("o"))           # 3

# in
print("Python" in texto)         # True

# startswith / endswith
print(texto.startswith("Hola"))  # True
print(texto.endswith("!"))        # False

# Buscar todos los índices
indices = [i for i in range(len(texto)) if texto.startswith("o", i)]
# o con find
indices = []
start = 0
while True:
    idx = texto.find("o", start)
    if idx == -1:
        break
    indices.append(idx)
    start = idx + 1
```

### Duplicados

```python
texto = "abbcccdddde"

# Eliminar caracteres duplicados consecutivos
from itertools import groupby
unico = "".join(k for k, _ in groupby(texto))  # "abcde"

# Eliminar todos los duplicados (preservar orden)
unico = "".join(dict.fromkeys(texto))  # "abcde"

# set (no preserva orden)
unico = "".join(set(texto))  # "abcde"

# Encontrar duplicados
from collections import Counter
conteo = Counter(texto)
duplicados = [c for c, v in conteo.items() if v > 1]  # ['b', 'c', 'd']
```

---

## 6. Funciones de Orden Superior

### map, filter, reduce

```python
from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map - aplicar función a cada elemento
cuadrados = list(map(lambda x: x**2, numeros))

# filter - mantener los que cumplen condición
pares = list(filter(lambda x: x % 2 == 0, numeros))

# reduce - acumular valor
suma = reduce(lambda a, b: a + b, numeros)  # 55

# Combinados
resultado = list(map(lambda x: x**2, 
                 filter(lambda x: x > 5, numeros)))

# Equivalente con comprensión
resultado = [x**2 for x in numeros if x > 5]
```

### sorted con key avanzada

```python
personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Juan", "edad": 30},
    {"nombre": "Pedro", "edad": 20}
]

# Ordenar por edad
por_edad = sorted(personas, key=lambda x: x["edad"])

# Ordenar por nombre
por_nombre = sorted(personas, key=lambda x: x["nombre"])

# Ordenar por longitud del nombre
por_longitud = sorted(personas, key=lambda x: len(x["nombre"]))

# Múltiples criterios
por_edad_nombre = sorted(personas, key=lambda x: (x["edad"], x["nombre"]))
```

### Comprehensions anidadas

```python
# Lista de listas a lista plana
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
plana = [x for row in matriz for x in row]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Matriz transpuesta
transpuesta = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]

# Dictionary comprehension anidada
dict_anidado = {k: {k2: v2 for k2, v2 in v.items()} 
                for k, v in {"a": {"x": 1, "y": 2}, "b": {"x": 3, "y": 4}}.items()}
```

---

## 7. Generadores y Iteradores

```python
# Generator expression
gen = (x**2 for x in range(1000000))
print(next(gen))  # 0
print(next(gen))  # 1

# Generator function
def generador_pares(limite):
    n = 0
    while n < limite:
        yield n
        n += 2

for par in generador_pares(10):
    print(par)  # 0, 2, 4, 6, 8

# enumerate
for i, valor in enumerate(["a", "b", "c"]):
    print(f"{i}: {valor}")

# zip
nombres = ["Ana", "Juan", "Pedro"]
edades = [25, 30, 35]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} - {edad}")

# zip_longest (rellena con None)
from itertools import zip_longest
for a, b in zip_longest([1, 2, 3], [4, 5], fillvalue=0):
    print(a, b)  # 1,4 / 2,5 / 3,0

# chain - concatenar iterables
from itertools import chain
resultado = list(chain([1, 2], [3, 4], [5, 6]))  # [1, 2, 3, 4, 5, 6]

# islice - slicing en iteradores
from itertools import islice
numeros = range(100)
primeros_10 = list(islice(numeros, 10))
cada_otro = list(islice(numeros, 0, 20, 2))
```

---

## 8. Trucos Pythonic

```python
# Intercambiar valores
a, b = 1, 2
a, b = b, a  # a=2, b=1

# Multiple assignment
a = b = c = 0

# Inicializar múltiples variables
x, y, z = 1, 2, 3

# Desempaquetado extendido
primero, *resto, ultimo = [1, 2, 3, 4, 5]
# primero = 1, resto = [2, 3, 4], ultimo = 5

# Desempaquetado con enumerate
for i, (a, b) in enumerate([(1, 2), (3, 4), (5, 6)]):
    print(i, a, b)

# any / all en una línea
todos_positivos = all(x > 0 for x in [-1, 2, 3])  # False
alguno_positivo = any(x > 0 for x in [-1, 2, -3])  # True

# Ternario
edad = 20
categoria = "mayor" if edad >= 18 else "menor"

# Swap con diccionario
lookup = {"a": 1, "b": 2}
valor = lookup.get("c", "default")  # "default"

# Merge eficiente de listas
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [*l1, *l2]  # [1, 2, 3, 4, 5, 6]

# Verificar tipo
resultado = isinstance(123, int)  # True
resultado = type(123) is int       # True

# Range con pasos negativos
for i in range(10, 0, -1):  # 10, 9, 8, ..., 1

# Sum con condición
suma_pares = sum(x for x in range(10) if x % 2 == 0)  # 20

# defaultdict automático
from collections import defaultdict
d = defaultdict(list)
d["frutas"].append("manzana")  # No necesita inicializar

# Count con Counter
from collections import Counter
contador = Counter("abracadabra")
print(contador.most_common(3))  # [('a', 5), ('b', 2), ('r', 2)]
```
