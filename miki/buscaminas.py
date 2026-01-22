import random

# ===== CONSTANTES =====
TAMANO = 5  # Tablero 5x5
LETRAS_FILAS = ['A', 'B', 'C', 'D', 'E']
LETRAS_ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Símbolos simples (sin emojis)
MINA = 'X'  # Representa una mina
OCULTO = '#'  # Representa celda oculta
VIDA = '❤'  # O usa '*' si no funciona


# Si ❤ no funciona, cambia a: VIDA = 'V'

# ===== FUNCIONES DEL JUEGO =====

def crear_tablero():
    """Crea un tablero 5x5 con letras aleatorias y minas"""
    tablero = []

    # PRIMERO: Crear tablero lleno de letras aleatorias
    for _ in range(TAMANO):
        fila = []
        for _ in range(TAMANO):
            letra = random.choice(LETRAS_ABC)
            fila.append(letra)
        tablero.append(fila)

    # SEGUNDO: Colocar 5 minas en posiciones aleatorias
    minas_colocadas = 0
    posiciones_minas = []  # Guardar dónde están las minas

    while minas_colocadas < 5:
        fila = random.randint(0, TAMANO - 1)
        col = random.randint(0, TAMANO - 1)

        # Si no hay mina ya, colocar una
        if tablero[fila][col] != MINA:
            tablero[fila][col] = MINA
            posiciones_minas.append((fila, col))
            minas_colocadas += 1

    return tablero, posiciones_minas


def crear_tablero_visible():
    """Crea un tablero visible para el jugador (todo oculto)"""
    return [[OCULTO for _ in range(TAMANO)] for _ in range(TAMANO)]


def mostrar_tablero(tablero_visible):
    """Muestra el tablero que ve el jugador"""
    print("\n    1   2   3   4   5")
    print("  +" + "---+" * TAMANO)

    for i in range(TAMANO):
        fila_str = f"{LETRAS_FILAS[i]} |"
        for j in range(TAMANO):
            fila_str += f" {tablero_visible[i][j]} |"
        print(fila_str)
        print("  +" + "---+" * TAMANO)


def convertir_coordenada(coord):
    """
    Convierte coordenada como 'A1' a índices (fila, columna)
    Ejemplo: 'B3' → (1, 2)
    """
    if len(coord) < 2 or len(coord) > 3:
        return None

    letra = coord[0].upper()

    # Obtener la parte numérica (podría ser 10, 11, etc. pero nosotros solo 1-5)
    try:
        numero = int(coord[1:])
    except ValueError:
        return None

    # Validar que la letra sea A-E
    if letra not in LETRAS_FILAS:
        return None

    # Validar que el número sea 1-5
    if numero < 1 or numero > TAMANO:
        return None

    fila = LETRAS_FILAS.index(letra)
    col = numero - 1

    return (fila, col)


# ===== PRÁCTICA 1: Función revelar_celda =====
def revelar_celda(tablero_real, tablero_visible, fila, col):
    """
    Revela una celda y devuelve una tupla con:
    (tipo, valor)
    tipo puede ser: 'mina', 'letra', 'ya_revelada'
    """
    # 1. Verificar si ya está revelada
    if tablero_visible[fila][col] != OCULTO:
        return ('ya_revelada', None)

    # 2. Obtener lo que hay en el tablero real
    contenido = tablero_real[fila][col]

    # 3. Revelar en el tablero visible
    tablero_visible[fila][col] = contenido

    # 4. Devolver resultado
    if contenido == MINA:
        return ('mina', MINA)
    else:
        return ('letra', contenido)


# ===== PRÁCTICA 2: Función contar_celdas_restantes =====
def contar_celdas_restantes(tablero_visible):
    """Cuenta cuántas celdas ocultas quedan"""
    contador = 0
    for fila in range(TAMANO):
        for col in range(TAMANO):
            if tablero_visible[fila][col] == OCULTO:
                contador += 1
    return contador


# ===== PRÁCTICA 3: Función contar_minas_descubiertas =====
def contar_minas_descubiertas(tablero_visible):
    """Cuenta cuántas minas ya fueron descubiertas"""
    contador = 0
    for fila in range(TAMANO):
        for col in range(TAMANO):
            if tablero_visible[fila][col] == MINA:
                contador += 1
    return contador


def mostrar_estado(vidas, puntos, celdas_restantes):
    """Muestra el estado actual del juego"""
    print(f"\n{'=' * 40}")
    print(f"VIDAS: {vidas}  |  PUNTOS: {puntos}  |  CELDAS: {celdas_restantes}")
    print(f"{'=' * 40}")


def jugar():
    """Función principal del juego"""
    print("=" * 50)
    print("          BUSCAMINAS DE LETRAS")
    print("=" * 50)
    print("\nDescubre todas las letras sin tocar las minas X")
    print("Coordenadas: A1, B3, E5, etc.")
    print("Tienes 3 vidas. ¡Buena suerte!\n")

    # Crear tableros
    tablero_real, posiciones_minas = crear_tablero()
    tablero_visible = crear_tablero_visible()

    # Estadísticas
    vidas = 3
    puntos = 0
    coordenadas_usadas = []  # Lista para guardar coordenadas ya jugadas

    # Juego principal
    while vidas > 0:
        # Mostrar estado
        mostrar_estado(vidas, puntos, contar_celdas_restantes(tablero_visible))
        mostrar_tablero(tablero_visible)

        # Pedir coordenada
        while True:
            coord = input("\nIngresa coordenada (ej: A1): ").upper().strip()

            # Convertir coordenada
            resultado = convertir_coordenada(coord)

            if resultado is None:
                print("ERROR: Coordenada inválida. Usa formato como A1, B3, E5")
                print("Letras válidas: A, B, C, D, E")
                print("Números válidos: 1, 2, 3, 4, 5")
                continue

            fila, col = resultado

            # Verificar si ya jugó esta coordenada
            if coord in coordenadas_usadas:
                print("ATENCION: Ya jugaste esta coordenada. Elige otra.")
                continue

            break

        # Revelar celda
        tipo, valor = revelar_celda(tablero_real, tablero_visible, fila, col)

        # PRÁCTICA 3: Manejar resultados
        if tipo == 'ya_revelada':
            print(f"Esta celda ya estaba revelada: {tablero_visible[fila][col]}")
        elif tipo == 'mina':
            vidas -= 1
            print(f"¡BOOM! Encontraste una mina {MINA} - Pierdes 1 vida")
            if vidas > 0:
                print(f"Te quedan {vidas} vidas")
        elif tipo == 'letra':
            puntos += 1
            print(f"¡BIEN! Letra '{valor}' encontrada - +1 punto (Total: {puntos})")

        # Agregar a coordenadas usadas
        coordenadas_usadas.append(coord)

        # Verificar si ganó (todas las letras descubiertas)
        # Total celdas = 25, minas = 5, letras = 20
        celdas_descubiertas = puntos + contar_minas_descubiertas(tablero_visible)
        if celdas_descubiertas == 25:  # Todas las celdas descubiertas
            print("\n" + "=" * 50)
            print("¡¡¡FELICIDADES!!! ¡HAS GANADO EL JUEGO!")
            print("=" * 50)
            print(f"Puntuación final: {puntos} puntos")
            print(f"Vidas restantes: {vidas}")

            # Mostrar tablero completo
            print("\nTablero completo (solución):")
            for i in range(TAMANO):
                fila_str = "  "
                for j in range(TAMANO):
                    fila_str += f"{tablero_real[i][j]} "
                print(fila_str)

            # Mostrar estadísticas
            print(f"\nEstadísticas:")
            print(f"- Letras encontradas: {puntos}/20")
            print(f"- Minas encontradas: {contar_minas_descubiertas(tablero_visible)}/5")
            print(f"- Intentos totales: {len(coordenadas_usadas)}")

            return

    # Si llega aquí, perdió (vidas = 0)
    print("\n" + "=" * 50)
    print("¡GAME OVER! Te has quedado sin vidas")
    print("=" * 50)
    print(f"Puntuación final: {puntos} puntos")

    # Mostrar tablero completo
    print("\nTablero completo (solución):")
    for i in range(TAMANO):
        fila_str = "  "
        for j in range(TAMANO):
            fila_str += f"{tablero_real[i][j]} "
        print(fila_str)

    # Mostrar dónde estaban las minas
    print(f"\nLas minas estaban en:")
    for fila, col in posiciones_minas:
        letra = LETRAS_FILAS[fila]
        numero = col + 1
        print(f"- {letra}{numero}")


# ===== MENÚ PRINCIPAL =====
def main():
    """Menú principal del juego"""
    while True:
        print("\n" + "=" * 50)
        print("            MENÚ PRINCIPAL")
        print("=" * 50)
        print("1. Jugar Buscaminas de Letras")
        print("2. Ver instrucciones")
        print("3. Salir")

        opcion = input("\nSelecciona una opción (1-3): ").strip()

        if opcion == "1":
            jugar()
        elif opcion == "2":
            print("\n" + "=" * 50)
            print("          INSTRUCCIONES DEL JUEGO")
            print("=" * 50)
            print("OBJETIVO:")
            print("- Descubrir todas las letras sin tocar las minas (X)")
            print("\nTABLERO:")
            print("- 5x5 celdas (de A1 a E5)")
            print("- 20 letras (A-Z) y 5 minas (X)")
            print("\nCÓMO JUGAR:")
            print("1. Ingresa coordenadas como 'A1', 'B3', 'E5'")
            print("2. Si es letra: ganas 1 punto")
            print("3. Si es mina X: pierdes 1 vida")
            print("4. Tienes 3 vidas iniciales")
            print("\nSÍMBOLOS:")
            print("# = Celda oculta")
            print("X = Mina")
            print("A-Z = Letra descubierta")
            print("=" * 50)
            input("\nPresiona Enter para continuar...")
        elif opcion == "3":
            print("\n¡Gracias por jugar! ¡Hasta la próxima! 👋")
            break
        else:
            print("ERROR: Opción inválida. Elige 1, 2 o 3.")


# ===== EJECUCIÓN =====
if __name__ == "__main__":
    # Prueba inicial
    print("Iniciando Buscaminas de Letras...")
    main()