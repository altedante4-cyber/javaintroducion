alumnos = [
    {"nombre": "Ana", "edad": 22, "notas": [7, 8, 9]},
    {"nombre": "Luis", "edad": 25, "notas": [6, 5, 7]},
    {"nombre": "Carlos", "edad": 20, "notas": [9, 9, 10]},
]

for a in alumnos:
    a["media"] = round(sum(a["notas"]) / len(a["notas"]), 2)

mejor = max(alumnos, key=lambda x: x["media"])

claves_lista = list(alumnos[0].keys())
valores_lista = list(alumnos[0].values())

# diccionario desde listas:
claves = ["x", "y", "z"]
valores = [10, 20, 30]
nuevo = dict(zip(claves, valores))

lista_tuplas = [("a", 1), ("b", 2), ("c", 3)]
desde_tuplas = dict(lista_tuplas)

print("Alumnos con media:", alumnos)
print("Mejor alumno:", mejor)
print("Claves:", claves_lista)
print("Valores:", valores_lista)
print("Desde listas paralelas:", nuevo)
print("Desde lista de tuplas:", desde_tuplas)
