inventario = {"manzanas": 10, "peras": 5}

inventario["naranjas"] = 8
inventario.setdefault("peras", 0)
inventario.setdefault("uvas", 12)
inventario.update({"kiwis": 6, "limones": 4})

cantidad = inventario.get("sandias", 0)
eliminado = inventario.pop("kiwis", "no encontrado")
clave_eliminada = inventario.popitem()

tiene_manzanas = "manzanas" in inventario
tiene_sandias = "sandias" in inventario

claves_str = ", ".join(inventario.keys())
total_stock = sum(inventario.values())

copia = inventario.copy()
copia.clear()

print("Inventario final:", inventario)
print("Sandias (default):", cantidad)
print("Eliminado:", eliminado)
print("Clave eliminada:", clave_eliminada)
print("Tiene manzanas:", tiene_manzanas)
print("Claves:", claves_str)
print("Stock total:", total_stock)
print("Copia tras clear:", copia)
