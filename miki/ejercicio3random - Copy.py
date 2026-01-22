#tenemos 4 palos y cada palo tiene 13 cartas 9 son numerales y 4 literales

# choice elige sin repetidos y choices elegi con repetidos pero se le puede asignar la k que es cuantos valores quieres sacar
import random

# Definir todos los valores posibles
valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
palos = ['corazones', 'diamantes', 'tréboles', 'picas']

# Seleccionar aleatoriamente
valor = random.choice(valores)
palo = random.choice(palos)

print(f"{valor} de {palo}")