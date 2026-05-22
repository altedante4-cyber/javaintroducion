datos = {"Ana": 85, "Luis": 92, "Carlos": 78, "Marta": 95, "Pedro": 88}

orden_asc = dict(sorted(datos.items(), key=lambda x: x[1]))
orden_desc = dict(sorted(datos.items(), key=lambda x: x[1], reverse=True))
orden_clave = dict(sorted(datos.items()))
orden_longitud = dict(sorted(datos.items(), key=lambda x: len(x[0])))

solo_claves = sorted(datos)
solo_valores = sorted(datos.values())

top3 = dict(sorted(datos.items(), key=lambda x: x[1], reverse=True)[:3])

doble_criterio = dict(sorted(datos.items(), key=lambda x: (x[1], len(x[0]))))

print("Original:", datos)
print("Ascendente por valor:", orden_asc)
print("Descendente por valor:", orden_desc)
print("Ordenado por clave:", orden_clave)
print("Por longitud de nombre:", orden_longitud)
print("Solo claves:", solo_claves)
print("Solo valores:", solo_valores)
print("Top 3:", top3)
print("Doble criterio:", doble_criterio)
