# MALA PRÁCTICA (Lento)
def buscar_lento(lista_grande, lista_busqueda):
    return [x for x in lista_grande if x in lista_busqueda] # O(n * m)

# BUENA PRÁCTICA (Rápido)
def buscar_rapido(lista_grande, lista_busqueda):
    set_busqueda = set(lista_busqueda) # O(m)
    return [x for x in lista_grande if x in set_busqueda] # O(n)
