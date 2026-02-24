nombres = {"Ana", "Luis", "Pedro"}

# Verificar si un elemento está en el set (muy rápido, O(1))
print("Ana" in nombres) # True

# Verificar si es un subconjunto (¿Están todos los de A en B?)
A = {1, 2}
B = {1, 2, 3}
print(A.issubset(B)) # True (A <= B)

# Verificar si es un superconjunto
print(B.issuperset(A)) # True (B >= A)

# Verificar si no tienen ningún elemento en común
C = {8, 9}
print(A.isdisjoint(C)) # True