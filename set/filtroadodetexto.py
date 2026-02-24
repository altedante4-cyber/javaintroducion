def intereses_comunes(usuario1, usuario2):
    # Intersección: lo que está en ambos sets
    comunes = set(usuario1) & set(usuario2)
    return list(comunes)

user_a = ["cine", "música", "deporte"]
user_b = ["cocina", "cine", "música"]
print(intereses_comunes(user_a, user_b)) # ['cine', 'música']