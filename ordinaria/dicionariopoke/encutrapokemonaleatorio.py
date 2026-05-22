import random
# Definimos los Pokémon disponibles y sus probabilidades de aparición
pokemon_disponibles = {
"Pikachu": {"probabilidad": 0.3, "nivel_min": 5, "nivel_max": 10},
"Charmander": {"probabilidad": 0.1, "nivel_min": 5, "nivel_max": 12},
"Bulbasaur": {"probabilidad": 0.15, "nivel_min": 4, "nivel_max": 9},
"Squirtle": {"probabilidad": 0.15, "nivel_min": 4, "nivel_max": 9},
"Rattata": {"probabilidad": 0.2, "nivel_min": 2, "nivel_max": 7},
"Pidgey": {"probabilidad": 0.1, "nivel_min": 2, "nivel_max": 6}
}

#extraemos los  nombre de los pokemon y sus probablidades en al lista separadas

nombre_pokemon= list(pokemon_disponibles.keys())
probabilidades = [data["probabilidad"] for data in pokemon_disponibles.values()]

def generar_encuentro():

    #selecionamos un pokemon basado en las probablidades

    pokemon_elegido_nombre = random.choices(nombre_pokemon , weights=probabilidades , k= 1)[0]

    pokemon_data = pokemon_disponibles[pokemon_elegido_nombre]
    print(pokemon_data)

    #asignamos un nivel aleatorio dentro de su rango

    nivel = random.randint(pokemon_data["nivel_min"],pokemon_data["nivel_max"])


    print(f"un {pokemon_elegido_nombre} salvaje de nivel {nivel} aparecio ")

    return {"nombre ": pokemon_elegido_nombre , "nivel": nivel }

print("simulando 3 encuentros aleatorios ")

for _  in range(3):
    generar_encuentro()
    

