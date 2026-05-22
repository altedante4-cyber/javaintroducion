"""Lambda, operator, functools — herramientas funcionales avanzadas"""

from functools import partial, cmp_to_key
from operator import itemgetter, attrgetter, methodcaller

# --- partial: fijar argumentos ---
def potencia(base, exp):
    return base ** exp

cuadrado = partial(potencia, exp=2)
cubo = partial(potencia, exp=3)

# --- map con múltiples iterables ---
list(map(lambda a, b: a + b, [1, 2, 3], [4, 5, 6]))

# --- sorted con cmp_to_key (raro pero útil) ---
def comparar(a, b):
    # -1: a va antes, 1: b va antes, 0: iguales
    if len(a) < len(b): return -1
    if len(a) > len(b): return 1
    if a < b: return -1
    if a > b: return 1
    return 0

sorted(["bb", "aaa", "c", "dd"], key=cmp_to_key(comparar))

# --- max/min con key y default ---
max([], default=0)  # 0
max([1, -2, 3], key=abs)  # -2

# --- filter con None (elimina falsy) ---
list(filter(None, [0, 1, "", "hola", None, []]))  # [1, "hola"]

# --- sorted con atributos de objetos ---
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __repr__(self):
        return f"{self.nombre}({self.edad})"

personas = [Persona("Ana", 25), Persona("Luis", 20)]
sorted(personas, key=attrgetter("edad"))
sorted(personas, key=attrgetter("nombre"))

# --- methodcaller: llamar método a cada elemento ---
palabras = ["hola", "mundo", "PYTHON"]
list(map(methodcaller("upper"), palabras))
list(map(methodcaller("count", "o"), palabras))

# --- zip como diccionario ---
claves = ["a", "b", "c"]
valores = [1, 2, 3]
dict(zip(claves, valores))  # {"a": 1, "b": 2, "c": 3}

# --- Counter operaciones ---
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
c1 + c2  # Counter({'a': 4, 'b': 3})
c1 - c2  # Counter({'a': 2})  (solo positivos)
c1 & c2  # intersección: Counter({'a': 1, 'b': 1})
c1 | c2  # unión: Counter({'a': 3, 'b': 2})

# --- defaultdict de listas (agrupar) ---
from collections import defaultdict
agrupado = defaultdict(list)
for k, v in [("a", 1), ("b", 2), ("a", 3)]:
    agrupado[k].append(v)
# {'a': [1, 3], 'b': [2]}

# --- defaultdict de int (contar) ---
contador = defaultdict(int)
for c in "abracadabra":
    contador[c] += 1

# --- all/any con generadores (lazy, cortocircuito) ---
all(x > 0 for x in [1, 2, 3])  # True (no recorre toda la lista si encuentra False)

# --- next con default ---
next((x for x in [1, 2, 3] if x > 5), None)  # None, no error
