"""
=======================================
FUNCIONES EN PYTHON — Errores comunes
y patrones para resolver ejercicios
=======================================

1.  SINTAXIS Y DEFINICIÓN
2.  PARÁMETROS Y ARGUMENTOS
3.  SCOPE (ÁMBITO)
4.  RETURN Y VALOR DE RETORNO
5.  ERRORES COMUNES
6.  PATRONES PARA RESOLVER EJERCICIOS
7.  CASOS PRÁCTICOS RESUELTOS
"""

# ============================================================
# 1. SINTAXIS Y DEFINICIÓN
# ============================================================

def nombre_funcion(param1, param2):
    """Docstring opcional."""
    resultado = param1 + param2
    return resultado

# Llamada
print(nombre_funcion(3, 5))

# - La definición termina con dos puntos (:)
# - El cuerpo va indentado (4 espacios por convención PEP 8)
# - El bloque termina cuando la indentación vuelve al nivel anterior

# ============================================================
# 2. PARÁMETROS Y ARGUMENTOS
# ============================================================

# 2a. Parámetros posicionales --- el orden importa
def sumar(a, b):
    return a + b

print(sumar(3, 5))

# 2b. Parámetros con valor por defecto
def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}!"

print(saludar("Ana"))
print(saludar("Luis", "Hey"))

# 2c. Parámetros nombrados (keyword arguments)
print(sumar(b=10, a=5))  # 15 — el orden no importa al nombrarlos

# 2d. *args (número variable de argumentos posicionales)
def sumar_varios(*numeros):
    return sum(numeros)

print(sumar_varios(1, 2, 3, 4, 5))  # 15

# 2e. **kwargs (número variable de argumentos nombrados)
def mostrar_datos(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_datos(nombre="Ana", edad=25, ciudad="Madrid")

# ORDEN CORRECTO EN LA DEFINICIÓN:
# def func(posicionales, *args, default=valor, **kwargs):

# ============================================================
# 3. SCOPE (ÁMBITO) — REGLA LEGB
# ============================================================

# Local -> Enclosing (funciones anidadas) -> Global -> Built-in

x = "global"

def exterior():
    x = "enclosing"

    def interior():
        x = "local"
        print(f"Dentro: {x}")

    interior()
    print(f"Exterior: {x}")

exterior()
print(f"Fuera: {x}")

# Para modificar una variable global dentro de una función:
contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
print(contador)  # 1

# Para modificar una variable de enclosing (función externa):
def crear_contador():
    cuenta = 0

    def incrementar():
        nonlocal cuenta
        cuenta += 1
        return cuenta

    return incrementar

mi_contador = crear_contador()
print(mi_contador())  # 1
print(mi_contador())  # 2

# ============================================================
# 4. RETURN Y VALOR DE RETORNO
# ============================================================

# - Si no hay return explícito -> la función devuelve None
# - Puede devolver cualquier tipo (int, str, list, tuple, dict, ...)
# - Múltiples valores se devuelven como tupla

def dividir(a, b):
    cociente = a // b
    resto = a % b
    return cociente, resto  # devuelve una tupla

c, r = dividir(10, 3)
print(f"Cociente: {c}, Resto: {r}")

# Early return para salir rápido en casos especiales
def es_par(numero):
    if numero % 2 == 0:
        return True
    return False

# ============================================================
# 5. ERRORES COMUNES
# ============================================================

# -----------------------------------------------------------
# Error 1: Olvidar los dos puntos al definir la función
# -----------------------------------------------------------
# def mi_funcion()  # SyntaxError: invalid syntax

# Solución: Siempre terminar con : después de los paréntesis

# -----------------------------------------------------------
# Error 2: Indentación incorrecta
# -----------------------------------------------------------
# def funcion():
# print("Hola")  # IndentationError

# Solución: PEP 8 — 4 espacios para cada nivel de indentación.
# Configurar el editor para que convierta tabs a espacios.

# -----------------------------------------------------------
# Error 3: Olvidar el return o devolver None sin querer
# -----------------------------------------------------------
def suma_sin_return(a, b):
    resultado = a + b
    # falta return

print(suma_sin_return(3, 5))  # None

# Solución: Asegurarse de que toda ruta de ejecución tenga return
# si la función debe devolver un valor.

# -----------------------------------------------------------
# Error 4: Confundir parámetros posicionales y nombrados
# -----------------------------------------------------------
def restar(a, b):
    return a - b

# restar(b=5)  # TypeError: missing 1 required positional argument: 'a'
# restar(5, a=3)  # TypeError: got multiple values for argument 'a'

# Solución: No mezclar posicionales después de nombrados, y
# proporcionar todos los argumentos requeridos.

# -----------------------------------------------------------
# Error 5: Mutar argumentos mutables por defecto
# -----------------------------------------------------------
def agregar_elemento(elemento, lista=[]):
    lista.append(elemento)
    return lista

print(agregar_elemento(1))  # [1]
print(agregar_elemento(2))  # [1, 2]  <- ¡Sorpresa!

# Solución: Usar None como default y crear la lista dentro
def agregar_elemento_correcto(elemento, lista=None):
    if lista is None:
        lista = []
    lista.append(elemento)
    return lista

print(agregar_elemento_correcto(1))  # [1]
print(agregar_elemento_correcto(2))  # [2]

# -----------------------------------------------------------
# Error 6: Modificar una variable global sin declararla
# -----------------------------------------------------------
# contador = 0
#
# def incrementar():
#     contador += 1  # UnboundLocalError

# Solución: Usar `global` o pasar el valor como parámetro y
# devolverlo.

# -----------------------------------------------------------
# Error 7: No respetar el orden de *args y **kwargs
# -----------------------------------------------------------
# def func(**kwargs, *args):  # SyntaxError

# Solución: Orden correcto -> posicionales, *args, default, **kwargs

# -----------------------------------------------------------
# Error 8: Llamar a una función antes de definirla
# -----------------------------------------------------------
# saludar_antes()  # NameError: name 'saludar_antes' is not defined
#
# def saludar_antes():
#     print("Hola")

# Solución: Definir las funciones al inicio del archivo o al
# menos antes de usarlas. Mejor aún: poner el código ejecutable
# dentro de if __name__ == "__main__":

# def main():
#     saludar_antes()
#
# if __name__ == "__main__":
#     main()

# -----------------------------------------------------------
# Error 9: Sombrear (shadowing) nombres de built-ins
# -----------------------------------------------------------
# list = [1, 2, 3]  # ahora list ya no es la función built-in
# print(list(range(5)))  # TypeError: 'list' object is not callable

# Solución: No usar nombres de built-ins como variables:
# list, dict, str, int, input, print, len, type, etc.

# -----------------------------------------------------------
# Error 10: Olvidar los paréntesis al llamar a la función
# -----------------------------------------------------------
def saludar():
    return "Hola"

print(saludar)    # <function saludar at 0x...> — no la ejecuta
print(saludar())  # Hola — correcto

# Solución: Si quieres el resultado, usa paréntesis.

# ============================================================
# 6. PATRONES PARA RESOLVER EJERCICIOS
# ============================================================

"""
PATRÓN GENERAL (PASOS):

  1. LEER Y ENTENDER el enunciado
     - ¿Qué recibe la función? (parámetros, tipos)
     - ¿Qué debe devolver? (tipo, formato)
     - ¿Casos borde? (vacíos, negativos, nulos, duplicados)

  2. DEFINIR LA FIRMA de la función primero
     def mi_funcion(param1: tipo, param2: tipo) -> tipo:
     Esto aclara qué entra y qué sale.

  3. IDENTIFICAR EL PATRÓN DEL PROBLEMA (ver abajo)

  4. IMPLEMENTAR con claridad, no con atajos al principio

  5. PROBAR con:
     - Caso típico (ejemplo del enunciado)
     - Caso borde (vacío, único, extremo)
     - Caso inválido (si aplica)

  6. SIMPLIFICAR / REFACTORIZAR si es necesario
"""

# -----------------------------------------------------------
# Patrón A: Acumulador (sumar, contar, concatenar)
# -----------------------------------------------------------
def contar_pares(numeros):
    """Cuenta cuántos números pares hay en una lista."""
    contador = 0
    for num in numeros:
        if num % 2 == 0:
            contador += 1
    return contador

print(contar_pares([1, 2, 3, 4, 5, 6]))  # 3

# -----------------------------------------------------------
# Patrón B: Búsqueda / Filtrado
# -----------------------------------------------------------
def mayores_que(limite, numeros):
    """Devuelve lista con números mayores que 'limite'."""
    resultado = []
    for num in numeros:
        if num > limite:
            resultado.append(num)
    return resultado

print(mayores_que(3, [1, 5, 2, 8, 3]))  # [5, 8]

# Versión concisa con list comprehension:
def mayores_que_v2(limite, numeros):
    return [num for num in numeros if num > limite]

# -----------------------------------------------------------
# Patrón C: Mapeo (transformar cada elemento)
# -----------------------------------------------------------
def cuadrados(numeros):
    """Devuelve una lista con el cuadrado de cada número."""
    resultado = []
    for num in numeros:
        resultado.append(num ** 2)
    return resultado

print(cuadrados([1, 2, 3, 4]))  # [1, 4, 9, 16]

# -----------------------------------------------------------
# Patrón D: Flag / Centinela (encontrar si existe)
# -----------------------------------------------------------
def contiene_negativo(numeros):
    """Verifica si hay al menos un número negativo."""
    for num in numeros:
        if num < 0:
            return True  # early return — encontramos uno
    return False  # ninguno era negativo

print(contiene_negativo([1, -2, 3]))  # True
print(contiene_negativo([1, 2, 3]))   # False

# -----------------------------------------------------------
# Patrón E: Índice simultáneo (enumerate)
# -----------------------------------------------------------
def encontrar_valor(lista, objetivo):
    """Devuelve el índice de la primera aparición o -1."""
    for i, valor in enumerate(lista):
        if valor == objetivo:
            return i
    return -1

print(encontrar_valor([3, 7, 1, 9], 7))  # 1
print(encontrar_valor([3, 7, 1, 9], 5))  # -1

# -----------------------------------------------------------
# Patrón F: Dos punteros / Comparar pares
# -----------------------------------------------------------
def tiene_duplicados_adyacentes(lista):
    """Verifica si hay dos elementos iguales seguidos."""
    for i in range(len(lista) - 1):
        if lista[i] == lista[i + 1]:
            return True
    return False

print(tiene_duplicados_adyacentes([1, 2, 2, 3]))  # True
print(tiene_duplicados_adyacentes([1, 2, 3, 4]))   # False

# -----------------------------------------------------------
# Patrón G: Acumulador con condición múltiple
# -----------------------------------------------------------
def contar_palabras_por_longitud(texto, longitud_minima):
    """Cuenta palabras que tienen al menos N caracteres."""
    palabras = texto.split()
    contador = 0
    for palabra in palabras:
        if len(palabra) >= longitud_minima:
            contador += 1
    return contador

print(contar_palabras_por_longitud("Hola mundo cruel y maravilloso", 5))  # 2

# -----------------------------------------------------------
# Patrón H: Diccionario como contador / frecuencia
# -----------------------------------------------------------
def frecuencia_caracteres(texto):
    """Cuenta cuántas veces aparece cada carácter."""
    frec = {}
    for c in texto:
        frec[c] = frec.get(c, 0) + 1
    return frec

print(frecuencia_caracteres("abbccc"))
# {'a': 1, 'b': 2, 'c': 3}

# Variante con collections.Counter:
# from collections import Counter
# Counter("abbccc")

# -----------------------------------------------------------
# Patrón I: Guard clause (validar al inicio)
# -----------------------------------------------------------
def dividir_seguro(a, b):
    """Divide a entre b. Valida que b no sea 0."""
    if b == 0:
        return "Error: división por cero"
    return a / b

# -----------------------------------------------------------
# Patrón J: Conversión entre tipos de datos
# -----------------------------------------------------------
def aplanar_lista(lista_de_listas):
    """Convierte [[1,2],[3,4]] en [1,2,3,4]."""
    resultado = []
    for sublista in lista_de_listas:
        resultado.extend(sublista)
    return resultado

print(aplanar_lista([[1, 2], [3, 4], [5]]))  # [1, 2, 3, 4, 5]

# -----------------------------------------------------------
# Patrón K: Múltiples returns condicionales
# -----------------------------------------------------------
def clasificar_nota(puntaje):
    """Clasifica un puntaje en letras (A, B, C, D, F)."""
    if puntaje >= 90:
        return "A"
    if puntaje >= 80:
        return "B"
    if puntaje >= 70:
        return "C"
    if puntaje >= 60:
        return "D"
    return "F"

print(clasificar_nota(85))  # B

# -----------------------------------------------------------
# Patrón L: Acumulador con índice (range + len)
# -----------------------------------------------------------
def sumar_listas(lista1, lista2):
    """Suma elemento a elemento de dos listas del mismo tamaño."""
    if len(lista1) != len(lista2):
        return None
    resultado = []
    for i in range(len(lista1)):
        resultado.append(lista1[i] + lista2[i])
    return resultado

print(sumar_listas([1, 2, 3], [4, 5, 6]))  # [5, 7, 9]

# Versión concisa:
# [a + b for a, b in zip(lista1, lista2)]

# ============================================================
# 7. CASOS PRÁCTICOS RESUELTOS
# ============================================================

# -----------------------------------------------------------
# Ejercicio 1: ¿Es palíndromo?
# -----------------------------------------------------------
# Enunciado: Escribir una función que determine si una palabra
# es palíndromo (se lee igual al derecho y al revés).
# Ignorar mayúsculas, espacios y tildes.

def es_palindromo(texto):
    # 1. Normalizar: minúsculas, sin espacios
    texto = texto.lower().replace(" ", "")

    # 2. Comparar con su reverso
    return texto == texto[::-1]

print(es_palindromo("Anita lava la tina"))   # True
print(es_palindromo("Python"))               # False
print(es_palindromo("Reconocer"))            # True

# -----------------------------------------------------------
# Ejercicio 2: Factorial (iterativo y recursivo)
# -----------------------------------------------------------
# Enunciado: Calcular el factorial de un número entero no
# negativo.

def factorial_iterativo(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def factorial_recursivo(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * factorial_recursivo(n - 1)

print(factorial_iterativo(5))  # 120
print(factorial_recursivo(5))  # 120

# -----------------------------------------------------------
# Ejercicio 3: Número primo
# -----------------------------------------------------------
# Enunciado: Determinar si un número es primo.

def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Solo revisamos impares hasta la raíz cuadrada
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

print(es_primo(7))    # True
print(es_primo(10))   # False
print(es_primo(2))    # True

# -----------------------------------------------------------
# Ejercicio 4: Fibonacci
# -----------------------------------------------------------
# Enunciado: Devolver el n-ésimo término de la sucesión de
# Fibonacci (0, 1, 1, 2, 3, 5, 8, ...).

def fibonacci(n):
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

for i in range(10):
    print(f"fib({i}) = {fibonacci(i)}")

# -----------------------------------------------------------
# Ejercicio 5: Anagramas
# -----------------------------------------------------------
# Enunciado: Determinar si dos palabras son anagramas (tienen
# las mismas letras en diferente orden).

def son_anagramas(palabra1, palabra2):
    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")

    if len(palabra1) != len(palabra2):
        return False

    # Opción 1: ordenar y comparar
    return sorted(palabra1) == sorted(palabra2)

    # Opción 2: contar frecuencias
    # from collections import Counter
    # return Counter(palabra1) == Counter(palabra2)

print(son_anagramas("amor", "roma"))    # True
print(son_anagramas("python", "java"))  # False
print(son_anagramas("Listen", "Silent"))  # True

# -----------------------------------------------------------
# Ejercicio 6: Eliminar duplicados (preservando orden)
# -----------------------------------------------------------
# Enunciado: Recibir una lista y devolver una nueva lista sin
# elementos duplicados, manteniendo el orden original.

def eliminar_duplicados(lista):
    vistos = set()
    resultado = []
    for elemento in lista:
        if elemento not in vistos:
            vistos.add(elemento)
            resultado.append(elemento)
    return resultado

print(eliminar_duplicados([3, 1, 2, 1, 3, 4, 2]))
# [3, 1, 2, 4]

# -----------------------------------------------------------
# Ejercicio 7: Juntar dos listas en un diccionario
# -----------------------------------------------------------
# Enunciado: Recibir dos listas (claves y valores) y devolver
# un diccionario.

def lista_a_diccionario(claves, valores):
    if len(claves) != len(valores):
        return None
    return {claves[i]: valores[i] for i in range(len(claves))}

print(lista_a_diccionario(["a", "b", "c"], [1, 2, 3]))
# {'a': 1, 'b': 2, 'c': 3}

# -----------------------------------------------------------
# Ejercicio 8: Rotar lista
# -----------------------------------------------------------
# Enunciado: Rotar una lista k posiciones a la derecha.

def rotar_derecha(lista, k):
    if not lista:
        return []
    k = k % len(lista)
    return lista[-k:] + lista[:-k]

print(rotar_derecha([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]

# -----------------------------------------------------------
# Ejercicio 9: Contar palabras en un texto
# -----------------------------------------------------------
# Enunciado: Recibir un texto y devolver un diccionario con la
# frecuencia de cada palabra.

def contar_palabras(texto):
    palabras = texto.lower().split()
    frecuencias = {}
    for palabra in palabras:
        palabra = palabra.strip(".,!?\"':;()[]")
        if palabra:
            frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

texto = "Hola mundo. Hola Python! ¿Cómo estás mundo?"
print(contar_palabras(texto))
# {'hola': 2, 'mundo': 2, 'python': 1, 'cómo': 1, 'estás': 1}

# -----------------------------------------------------------
# Ejercicio 10: Matriz transpuesta
# -----------------------------------------------------------
# Enunciado: Devolver la transpuesta de una matriz (lista de
# listas, mismo tamaño de filas).

def transponer(matriz):
    if not matriz:
        return []
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta = []
    for j in range(columnas):
        nueva_fila = []
        for i in range(filas):
            nueva_fila.append(matriz[i][j])
        transpuesta.append(nueva_fila)
    return transpuesta

    # Versión concisa:
    # return [list(fila) for fila in zip(*matriz)]

matriz = [[1, 2, 3],
          [4, 5, 6]]
print(transponer(matriz))
# [[1, 4], [2, 5], [3, 6]]

# ============================================================
# BONUS: Decorador para medir tiempo de ejecución
# ============================================================

import time

def medir_tiempo(func):
    def envoltura(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fin = time.perf_counter()
        print(f"{func.__name__} tardó {fin - inicio:.6f} segundos")
        return resultado
    return envoltura

@medir_tiempo
def ejemplo_lento():
    total = sum(range(1000000))
    return total

print(ejemplo_lento())

# ============================================================
# BONUS: Type hints (anotaciones de tipo)
# ============================================================

def procesar_datos(nombre: str, edad: int, pesos: list[float]) -> dict[str, float]:
    datos = {
        "nombre": nombre,
        "edad": edad,
        "peso_promedio": sum(pesos) / len(pesos) if pesos else 0.0,
    }
    return datos

print(procesar_datos("Ana", 30, [55.5, 56.0, 57.2]))
