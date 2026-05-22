"""Patrones comunes resueltos de forma pythonica"""

from itertools import zip_longest, chain, groupby, combinations, permutations
from collections import Counter, defaultdict
import random

# --- 1. CHUNK: dividir lista en bloques de n ---
def chunk(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

print(chunk([1, 2, 3, 4, 5, 6, 7], 3))  # [[1,2,3], [4,5,6], [7]]

# --- 2. WINDOW: ventana deslizante ---
def window(lst, n):
    return [lst[i:i + n] for i in range(len(lst) - n + 1)]

print(window([1, 2, 3, 4, 5], 3))  # [[1,2,3], [2,3,4], [3,4,5]]

# --- 3. FLATTEN: aplanar lista anidada ---
def flatten(lst):
    return [x for sub in lst for x in (flatten(sub) if isinstance(sub, (list, tuple)) else [sub])]

def flatten_one_level(lst):
    return [x for sub in lst for x in sub]

# --- 4. DEDUPE: eliminar duplicados preservando orden ---
def dedupe(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

print(dedupe([1, 2, 1, 3, 2, 4]))  # [1, 2, 3, 4]

# --- 5. DUPLICADOS: encontrar duplicados ---
def duplicados(lst):
    counts = Counter(lst)
    return [item for item, count in counts.items() if count > 1]

# --- 6. TRANSPOSE: transponer matriz ---
matriz = [[1, 2, 3], [4, 5, 6]]
transpuesta = list(zip(*matriz))  # [(1,4), (2,5), (3,6)]

# --- 7. GROUP BY: agrupar por clave ---
items = ["manzana", "banana", "cereza", "dátil", "arándano"]
groups = {k: list(g) for k, g in groupby(sorted(items, key=len), key=len)}
# {5: ['cereza', 'dátil'], 6: ['banana'], 8: ['manzana', 'arándano']}

# --- 8. MOST COMMON: elementos más frecuentes ---
Counter([1, 1, 2, 2, 2, 3]).most_common(2)  # [(2, 3), (1, 2)]

# --- 9. SHUFFLE: mezclar aleatoriamente ---
random.shuffle(items)  # in-place
muestra = random.sample(items, k=3)  # 3 aleatorios sin repetición

# --- 10. PARTITION: partir en dos según condición ---
def partition(lst, predicate):
    ok = []
    ko = []
    for x in lst:
        (ok if predicate(x) else ko).append(x)
    return ok, ko

pares, impares = partition([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)

# --- 11. DIFFERENCE: elementos en A pero no en B ---
a = [1, 2, 3, 4]
b = [3, 4, 5]
list(set(a) - set(b))  # [1, 2]

# --- 12. INTERSECTION / UNION (con sets) ---
list(set(a) & set(b))  # intersección [3,4]
list(set(a) | set(b))  # unión [1,2,3,4,5]

# --- 13. COMBINACIONES Y PERMUTACIONES ---
list(combinations([1, 2, 3], 2))  # [(1,2), (1,3), (2,3)]
list(permutations([1, 2, 3], 2))  # [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]

# --- 14. PADDING: rellenar a longitud fija ---
def pad(lst, length, val=None):
    return lst + [val] * (length - len(lst))

def pad_right(lst, length, val=None):
    return list(zip_longest(lst, range(length), fillvalue=val))[0]

# --- 15. TAKE WHILE / DROP WHILE ---
from itertools import takewhile, dropwhile
list(takewhile(lambda x: x < 5, [1, 3, 5, 7, 2]))  # [1, 3]
list(dropwhile(lambda x: x < 5, [1, 3, 5, 7, 2]))  # [5, 7, 2]
