colores = {"rojo", "azul"}

# Añadir un solo elemento
colores.add("verde")

# Añadir múltiples elementos (desde otra lista o set)
colores.update(["amarillo", "blanco", "rojo"]) # El rojo no se repetirá

# Eliminar un elemento (da error si no existe)
colores.remove("azul")

# Eliminar un elemento (NO da error si no existe)
colores.discard("rosa")

# Sacar un elemento aleatorio (y devolverlo)
elemento = colores.pop()

# Vaciar el set por completo
colores.clear()