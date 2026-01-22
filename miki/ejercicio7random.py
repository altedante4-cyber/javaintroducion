import random

for partido in range(15):  # 14 partidos + pleno al 15

    for pert in range(partido):
        apuesta1 = random.choice(['1', 'X', '2'])
        apuesta2 = random.choice(['1', 'X', '2'])
        apuesta3 = random.choice(['1', 'X', '2'])
        print(f"{apuesta1}  {apuesta2}  {apuesta3}" , end = " ")
    print()

