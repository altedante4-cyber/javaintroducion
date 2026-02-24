def elementos_en_todos(*listas):
    if not listas:
        return set()

    # Empezamos con el primer set y buscamos la intersección con los demás
    resultado = set(listas[0])
    for s in listas[1:]:
        resultado &= set(s)
    return resultado


# Uso
print(elementos_en_todos([1, 2, 3], [2, 3, 4], [3, 4, 5]))  # {3}