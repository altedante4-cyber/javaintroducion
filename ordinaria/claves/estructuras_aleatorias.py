import random

nombres = ["Ana", "Luis", "Eva", "Juan", "Sofía", "Carlos", "Mía", "Pedro"]
ciudades = {"Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao"}
edades = (18, 25, 30, 35, 40, 45, 50)
puntajes_por_nombre = {"Ana": 85, "Luis": 92, "Eva": 78, "Juan": 88}

def ejemplo_listas():
    print("--- LISTAS ---")
    muestra = random.sample(nombres, 3)
    print(f"  Muestra aleatoria (3): {muestra}")
    elegido = random.choice(nombres)
    print(f"  Eleccion al azar: {elegido}")
    copia = nombres[:]
    random.shuffle(copia)
    print(f"  Lista original: {nombres}")
    print(f"  Lista mezclada: {copia}")
    pesos = [random.randint(1, 10) for _ in range(len(nombres))]
    print(f"  Pesos aleatorios: {pesos}")
    ponderado = random.choices(nombres, weights=pesos, k=3)
    print(f"  Eleccion ponderada: {ponderado}")

def ejemplo_tuplas():
    print("\n--- TUPLAS ---")
    t = random.choice(edades)
    print(f"  Edad aleatoria de la tupla: {t}")
    t_aleatoria = tuple(random.randint(1, 100) for _ in range(5))
    print(f"  Tupla generada aleatoriamente: {t_aleatoria}")
    t_mezclada = random.sample(edades, len(edades))
    print(f"  Edades reordenadas: {tuple(t_mezclada)}")

def ejemplo_conjuntos():
    print("\n--- CONJUNTOS (SET) ---")
    elegidas = set(random.sample(list(ciudades), 2))
    print(f"  Ciudades elegidas: {elegidas}")
    nums = {random.randint(1, 20) for _ in range(10)}
    print(f"  Numeros aleatorios unicos: {sorted(nums)}")

def ejemplo_diccionarios():
    print("\n--- DICCIONARIOS ---")
    datos = {nombre: random.randint(60, 100) for nombre in random.sample(nombres, 4)}
    print(f"  Diccionario generado: {datos}")
    for nombre, puntaje in datos.items():
        estado = "aprobado" if puntaje >= 70 else "reprobado"
        print(f"    {nombre}: {puntaje} -> {estado}")

def ejemplo_mixto():
    print("\n--- ESTRUCTURA MIXTA ---")
    participantes = [
        {"nombre": n, "edad": random.choice(edades), "ciudad": random.choice(list(ciudades))}
        for n in random.sample(nombres, 3)
    ]
    for p in participantes:
        print(f"  {p['nombre']} | {p['edad']} anios | {p['ciudad']}")

if __name__ == "__main__":
    ejemplo_listas()
    ejemplo_tuplas()
    ejemplo_conjuntos()
    ejemplo_diccionarios()
    ejemplo_mixto()
