class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b
    
    @staticmethod
    def multiplicar(a, b):
        return a * b
    
    @staticmethod
    def es_par(numero):
        return numero % 2 == 0

print(f"5 + 3 = {Calculadora.sumar(5, 3)}")
print(f"4 * 7 = {Calculadora.multiplicar(4, 7)}")
print(f"10 es par: {Calculadora.es_par(10)}")
print(f"7 es par: {Calculadora.es_par(7)}")
