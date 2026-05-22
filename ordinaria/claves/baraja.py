import random

palos = ["Picas", "Corazones", "Diamantes", "Treboles"]
nombres = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "As"]
valores = {n: i for i, n in enumerate(nombres)}

baraja = [(n, p) for n in nombres for p in palos]

mano = []
for _ in range(5):
    idx = random.randint(0, len(baraja) - 1)
    mano.append(baraja.pop(idx))

print("Mano de 5 cartas:")
for carta in mano:
    print(f"  {carta[0]} de {carta[1]}")

mano_ordenada = sorted(mano, key=lambda c: valores[c[0]])
print("\nMano ordenada por valor:")
for carta in mano_ordenada:
    print(f"  {carta[0]} de {carta[1]}")

def es_color(mano):
    palo = mano[0][1]
    return all(c[1] == palo for c in mano)

print(f"\nEs color: {'SI' if es_color(mano) else 'NO'}")

valores_mano = [valores[c[0]] for c in mano]
print(f"Valores: {sorted(valores_mano)}")
print(f"Suma de valores: {sum(valores_mano)}")
