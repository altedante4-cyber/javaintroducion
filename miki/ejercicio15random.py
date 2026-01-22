import random

figuras = random.choices(["corazon","diamante","herraura","campana","limo"],k=3)


almacenar = len(set(figuras))

mostrar = ",".join(figuras)
print(mostrar)
if almacenar == 3:
    print("Lo siento, ha perdido")
elif almacenar == 2:
    print("Bien, ha recuperado su moneda ")
else:
    print("Enhorabuena, ha ganado 10 monedas")



