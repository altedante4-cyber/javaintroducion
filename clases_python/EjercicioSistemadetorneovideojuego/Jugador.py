import random


class Jugador:
    contador = 0
    ranking = []

    def __init__(self, nombre, edad, puntuacion=1000):
        self._nombre = nombre
        self.edad = edad
        self._puntuacion = puntuacion
        Jugador.ranking.append(self)
        Jugador.contador += 1

    @property
    def puntuacion(self):
        return self._puntuacion

    @puntuacion.setter
    def puntuacion(self, valor):
        if valor >= 0 and valor <= 9999:
            self._puntuacion = valor
        else:
            print("Valor de puntuación no válido (debe estar entre 0 y 9999)")

    @property
    def nombre(self):
        return self._nombre

    def actualizar_puntuacion(self, puntos):
        nueva_puntuacion = self._puntuacion + puntos
        if 0 <= nueva_puntuacion <= 9999:
            self._puntuacion = nueva_puntuacion
        else:
            print("La puntuación resultante excede los límites")

    @staticmethod
    def generar_suerte():
        return random.randint(1, 100)

    @classmethod
    def obtener_ranking(cls):
        lista_ordenada = sorted(cls.ranking, key=lambda x: x.puntuacion, reverse=True)
        return lista_ordenada

    @classmethod
    def crear_jugador_random(cls, nombre):
        edad = random.randint(18, 40)
        puntuacion = random.randint(0, 9999)
        return cls(nombre, edad, puntuacion)

    def __str__(self):
        return f"| {self._nombre:<15} | {self.edad:>3} años | {self._puntuacion:>4} pts |"


# ============ PRUEBAS ============
print("=" * 50)
print("CREAR JUGADORES")
print("=" * 50)

j1 = Jugador("Carlos", 25, 1500)
j2 = Jugador.crear_jugador_random("María")
j3 = Jugador("Ana", 30)

print(j1)
print(j2)
print(j3)

print("\n" + "=" * 50)
print("ACTUALIZAR PUNTUACIÓN (+500)")
print("=" * 50)
j1.actualizar_puntuacion(500)
print(f"Nueva puntuación de Carlos: {j1.puntuacion}")

print("\n" + "=" * 50)
print("GENERAR SUERTE")
print("=" * 50)
print(f"Número de suerte: {Jugador.generar_suerte()}")

print("\n" + "=" * 50)
print("RANKING (ordenado por puntuación)")
print("=" * 50)
print("| NOMBRE         | EDAD | PUNTOS |")
print("|" + "-" * 17 + "+" + "-" * 5 + "+" + "-" * 7 + "|")
for jugador in Jugador.obtener_ranking():
    print(jugador)

print("\n" + "=" * 50)
print(f"Total jugadores: {Jugador.contador}")
