import random

dias = 30
temp_min = [random.randint(5, 15) for _ in range(dias)]
temp_max = [random.randint(20, 35) for _ in range(dias)]
temp_media = [(temp_min[i] + temp_max[i]) / 2 for i in range(dias)]

print(f"Reporte de temperaturas ({dias} dias):\n")

for i in range(dias):
    barra_min = "#" * temp_min[i]
    barra_max = "#" * temp_max[i]
    print(f"  dia {i+1:2d}: min {temp_min[i]:2d} {barra_min}")
    print(f"          max {temp_max[i]:2d} {barra_max}")

promedio_min = sum(temp_min) / dias
promedio_max = sum(temp_max) / dias
promedio_media = sum(temp_media) / dias
print(f"\nPromedio minimo: {promedio_min:.1f}")
print(f"Promedio maximo: {promedio_max:.1f}")
print(f"Promedio general: {promedio_media:.1f}")

max_registrada = max(temp_max)
min_registrada = min(temp_min)
print(f"\nMaxima absoluta: {max_registrada}")
print(f"Minima absoluta: {min_registrada}")
