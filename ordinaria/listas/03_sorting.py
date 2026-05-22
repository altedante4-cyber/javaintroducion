"""Ordenación pythonica con sorted(), sort() y key=lambda"""

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# sorted() — devuelve nueva lista ordenada (no muta)
ordenado = sorted(nums)
reverso = sorted(nums, reverse=True)

# .sort() — ordena in-place (muta la lista, más eficiente)
nums.sort()
nums.sort(reverse=True)

# --- key=lambda: el alma del orden pythonico ---
palabras = ["manzana", "kiwi", "cereza", "dátil", "banana"]

# Por longitud
sorted(palabras, key=len)
# Por última letra
sorted(palabras, key=lambda s: s[-1])
# Por múltiples criterios: tupla de keys
sorted(palabras, key=lambda s: (len(s), s))

# --- Ordenar lista de tuplas/diccionarios ---
personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Eva", "edad": 22},
]
sorted(personas, key=lambda p: p["edad"])
sorted(personas, key=lambda p: (-p["edad"], p["nombre"]))

datos = [("Ana", 25), ("Luis", 30), ("Eva", 22)]
sorted(datos, key=lambda t: t[1])  # por edad
sorted(datos, key=lambda t: (t[1], t[0]))  # por edad, luego nombre

# --- sorted con str.lower (case-insensitive) ---
sorted(["Ana", "luis", "eva"], key=str.lower)

# --- itemgetter y attrgetter (más rápido para muchos datos) ---
from operator import itemgetter, attrgetter
sorted(datos, key=itemgetter(1))
sorted(datos, key=itemgetter(1, 0))

# --- sorted estable: mantiene orden relativo ---
# Equivalente a ORDER BY col1, col2 en SQL
sorted(sorted(datos, key=itemgetter(0)), key=itemgetter(1))

# --- n-largest / n-smallest sin ordenar todo ---
import heapq
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
heapq.nlargest(3, nums)   # [9, 6, 5]
heapq.nsmallest(3, nums)  # [1, 1, 2]
heapq.nlargest(2, personas, key=lambda p: p["edad"])
