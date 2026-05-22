import random
def intentar_capturar(pokemon_salvaje, pokeball_efectividad=1.0,
salud_porcentaje=1.0):
# La probabilidad base de captura se puede ajustar
# Un Pokémon con menos salud es más fácil de capturar (salud_porcentaje
#bajo)
# Una mejor Poké Ball aumenta la efectividad (pokeball_efectividad alto)
# Ejemplo de cálculo de probabilidad: inversamente proporcional a la
#salud
# y directamente proporcional a la efectividad de la Poké Ball.
# Este es un modelo simplificado, los juegos reales usan fórmulas más
#complejas [10].
    probabilidad_base = 0.3 # Probabilidad base de captura
    probabilidad_final = probabilidad_base * pokeball_efectividad * (1 + (1 - salud_porcentaje) * 0.7) # Aumenta hasta un 70% si la salud es 0
# Aseguramos que la probabilidad no exceda 1.0
    probabilidad_final = min(probabilidad_final, 0.95)
    print(f"Intentando capturar a {pokemon_salvaje['nombre']} (Salud:
    {salud_porcentaje*100:.0f}%, Probabilidad: {probabilidad_final*100:.2f}%) ")
    if random.random() < probabilidad_final:
        print(f"¡Felicidades! ¡Has capturado a
            {pokemon_salvaje['nombre']}!")
            return True
else:
print(f"¡Oh no! {pokemon_salvaje['nombre']} escapó.")
return False
# Simulamos un intento de captura
mi_pokemon_salvaje = {"nombre": "Charmander", "nivel": 7}
intentar_capturar(mi_pokemon_salvaje, salud_porcentaje=0.5) # Charmander con
50% de salud
intentar_capturar(mi_pokemon_salvaje, pokeball_efectividad=1.5,
salud_porcentaje=0.1) # Charmander con poca salud y Super Ball
# Salida potencial:
# Intentando capturar a Charmander (Salud: 50%, Probabilidad: 40.50%)
# ¡Felicidades! ¡Has capturado a Charmander!
# Intentando capturar a Charmander (Salud: 10%, Probabilidad: 70.50%)
# ¡Felicidades! ¡Has capturado a Charmander!