class Inventario:
    def __init__(self):
        self.items = []
    
    def __add__(self, item):
        self.items.append(item)
        return self
    
    def __iter__(self):
        return iter(self.items)
    
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return ", ".join(str(i) for i in self.items)

inv = Inventario()
inv + "espada"
inv + "escudo"
inv + "armadura"

print(f"Items: {inv}")
print(f"Cantidad: {len(inv)}")
