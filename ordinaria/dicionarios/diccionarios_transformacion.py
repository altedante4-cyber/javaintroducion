d = {"Ana": 85, "Luis": 92, "Carlos": 78}

items = list(d.items())
claves = list(d.keys())
valores = list(d.values())

lista_nombres_notas = [(k, v) for k, v in d.items()]
lista_diccionarios = [{"nombre": k, "nota": v} for k, v in d.items()]

nombres_mayus = {k.upper(): v for k, v in d.items()}
notas_letra = {
    k: "Sobresaliente" if v >= 90 else "Notable" if v >= 80 else "Aprobado" if v >= 70 else "Suspenso"
    for k, v in d.items()
}

agrupado = {}
for i, (k, v) in enumerate(d.items()):
    agrupado[i] = {"nombre": k, "nota": v}

tuplas = [("a", 1), ("b", 2), ("c", 3)]
recuperado = {t[0]: t[1] for t in tuplas}
recuperado_v2 = dict(tuplas)

print("Items:", items)
print("Claves:", claves)
print("Valores:", valores)
print("Lista tuplas:", lista_nombres_notas)
print("Lista dicts:", lista_diccionarios)
print("Mayusculas:", nombres_mayus)
print("Notas letra:", notas_letra)
print("Agrupado:", agrupado)
print("Recuperado:", recuperado)
