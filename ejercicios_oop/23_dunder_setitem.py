class Cofre:
    def __init__(self):
        self.items = {}
    
    def __setitem__(self, clave, valor):
        self.items[clave] = valor
    
    def __getitem__(self, clave):
        return self.items.get(clave, "No existe")
    
    def __len__(self):
        return len(self.items)
    
    def __contains__(self, clave):
        return clave in self.items

cofre = Cofre()
cofre["espada"] = "Excalibur"
cofre["pocion"] = "Salud"
cofre["llave"] = "Castillo"

print(f"Espada: {cofre['espada']}")
print(f"Oro: {cofre['oro']}")
print(f"¿Tiene llave?: {'llave' in cofre}")
print(f"Total items: {len(cofre)}")
