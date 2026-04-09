class Generador:
    def __init__(self, inicio, fin, paso):
        self.inicio = inicio
        self.fin = fin
        self.paso = paso
    
    def __iter__(self):
        self.actual = self.inicio
        return self
    
    def __next__(self):
        if self.actual >= self.fin:
            raise StopIteration
        valor = self.actual
        self.actual += self.paso
        return valor

print("=== Números pares ===")
for n in Generador(0, 10, 2):
    print(n)

print("\n=== Números impares ===")
for n in Generador(1, 10, 2):
    print(n)
