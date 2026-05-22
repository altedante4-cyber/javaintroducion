import random

hexdigitos = "0123456789ABCDEF"

monedas = ["BTC", "ETH", "SOL", "ADA", "DOT", "AVAX", "LINK", "MATIC"]
colores = ["rojo", "verde", "azul", "naranja", "morado"]
adjetivos = ["rapido", "seguro", "frio", "audaz", "sabio", "lento", "fuerte"]

def generar_id_transaccion():
    return "0x" + "".join(random.choices(hexdigitos, k=16))

def generar_usuario():
    nombre = random.choice(adjetivos).capitalize() + random.choice(colores).capitalize()
    return {"nombre": nombre, "monedas_favoritas": set(random.sample(monedas, random.randint(2, 4)))}

def generar_cartera(monedas_disponibles):
    cantidad = min(random.randint(3, 6), len(monedas_disponibles))
    return {m: round(random.uniform(0, 10), 4) for m in random.sample(monedas_disponibles, cantidad)}

def generar_transaccion(usuarios, carteras):
    emisor = random.choice(usuarios)
    receptor = random.choice([u for u in usuarios if u != emisor])
    moneda = random.choice(list(carteras[emisor["nombre"]].keys()))
    cantidad = round(random.uniform(0.1, carteras[emisor["nombre"]][moneda] * 0.5), 4)
    return {
        "id": generar_id_transaccion(),
        "emisor": emisor["nombre"],
        "receptor": receptor["nombre"],
        "moneda": moneda,
        "cantidad": cantidad,
        "exitosa": cantidad > 0,
    }

if __name__ == "__main__":
    print("=== CARTERA CRIPTO ALEATORIA ===")
    usuarios = [generar_usuario() for _ in range(4)]
    carteras = {u["nombre"]: generar_cartera(list(u["monedas_favoritas"])) for u in usuarios}
    print("\n--- USUARIOS Y CARTERAS ---")
    for u in usuarios:
        print(f"  {u['nombre']}: {carteras[u['nombre']]}")
    print("\n--- TRANSACCIONES ---")
    for _ in range(5):
        tx = generar_transaccion(usuarios, carteras)
        estado = "OK" if tx["exitosa"] else "FALLIDA"
        print(f"  [{estado}] {tx['emisor']} -> {tx['receptor']} | {tx['cantidad']} {tx['moneda']} | {tx['id']}")
