import random

filas = random.randint(3, 5)
cols = random.randint(3, 5)

matriz = [[random.randint(0, 9) for _ in range(cols)] for _ in range(filas)]

print(f"Matriz {filas}x{cols} generada:")
for fila in matriz:
    print("  " + " ".join(str(n) for n in fila))

print(f"\nSuma por filas:")
for i, fila in enumerate(matriz):
    print(f"  fila {i+1}: {sum(fila)}")

print(f"\nSuma por columnas:")
for j in range(cols):
    col = [matriz[i][j] for i in range(filas)]
    print(f"  col {j+1}: {sum(col)}")

total = sum(sum(fila) for fila in matriz)
print(f"\nTotal: {total}")
print(f"Promedio: {total / (filas * cols):.2f}")
