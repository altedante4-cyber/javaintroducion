def concatenar_nombres(*nombres):
    # 'nombres' es una tupla
    return " - ".join(nombres)

print(concatenar_nombres("Ana", "Luis", "Pedro"))