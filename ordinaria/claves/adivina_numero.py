import random

secreto = random.randint(1, 100)
intentos = 0

print("Adivina el numero entre 1 y 100")

while True:
    try:
        entrada = input("> ")
        if not entrada:
            break
        n = int(entrada)
    except ValueError:
        print("solo numeros")
        continue
    except EOFError:
        break
    intentos += 1
    if n < secreto:
        print("muy bajo")
    elif n > secreto:
        print("muy alto")
    else:
        print(f"correcto en {intentos} intentos")
        break
