from functools import partial

class Calculadora:
    def operaciones(self, a, b, operacion):
        if operacion == "sumar":
            return a + b
        elif operacion == "restar":
            return a - b
        elif operacion == "multiplicar":
            return a * b
        return None

calc = Calculadora()
sumar = partial(calc.operaciones, operacion="sumar")
restar = partial(calc.operaciones, operacion="restar")

print(f"5 + 3 = {sumar(5, 3)}")
print(f"10 - 7 = {restar(10, 7)}")
print(f"4 * 6 = {calc.operaciones(4, 6, 'multiplicar')}")
