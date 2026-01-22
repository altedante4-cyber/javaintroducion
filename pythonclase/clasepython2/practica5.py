"""
Docstring for practica5
5. Operaciones de conjuntos
Dados tres conjuntos:

python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = {5, 8, 9, 10}
Encuentra:

Elementos que están en A pero no en B ni C

Elementos que están en exactamente dos de los tres conjuntos

"""
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = {5, 8, 9, 10}


#el primero me tiene que devolver  todos los numeros que no estan en a es decir 6,7,8,9,10

elementos_no_b = []
elementos_no_c = []
for a in A :

    if a not in B :

        elementos_no_b.append(a)

    if a not in C :

        elementos_no_c.append(a)



elemento_estan_en_los_tres_conjuntos = set()

for raiz in A:

    if raiz in B  and raiz in C :

        elemento_estan_en_los_tres_conjuntos.add(raiz)


for segundo in B :

    if segundo in A and segundo in C :

        elemento_estan_en_los_tres_conjuntos.add(raiz)


for tercer in C :

    if tercer in A and tercer in B :

        elemento_estan_en_los_tres_conjuntos.add(tercer)
print(elemento_estan_en_los_tres_conjuntos)
