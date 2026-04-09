class Arma:
    def __init__(self, nombre, dano):
        self.nombre = nombre
        self.dano = dano
    
    @property
    def dano_total(self):
        return self.dano

class Espada(Arma):
    @property
    def dano_total(self):
        return self.dano + 10

class Arco(Arma):
    @property
    def dano_total(self):
        return self.dano + 5

class Baculo(Arma):
    @property
    def dano_total(self):
        return self.dano + 20

armas = [Espada("Espada", 30), Arco("Arco", 25), Baculo("Varita", 15)]
for a in armas:
    print(f"{a.nombre}: Daño {a.dano_total}")
