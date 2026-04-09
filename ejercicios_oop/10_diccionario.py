inventario = {
    "espada": {"precio": 100, "cantidad": 5},
    "escudo": {"precio": 50, "cantidad": 10},
    "pocion": {"precio": 25, "cantidad": 20}
}

def mostrar_tabla(inv):
    print(f"{'ITEM':<10} {'PRECIO':<10} {'CANTIDAD':<10}")
    print("-" * 30)
    for item, datos in inv.items():
        print(f"{item:<10} ${datos['precio']:<9} {datos['cantidad']:<10}")

mostrar_tabla(inventario)

print("\n=== Total valor inventario ===")
total = sum(d['precio'] * d['cantidad'] for d in inventario.values())
print(f"Total: ${total}")
