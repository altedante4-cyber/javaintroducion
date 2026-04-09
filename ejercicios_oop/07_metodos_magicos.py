class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Punto({self.x}, {self.y})"
    
    def __add__(self, other):
        return Punto(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        return abs(self.x) + abs(self.y)

p1 = Punto(3, 4)
p2 = Punto(1, 2)
print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"p1 + p2: {p1 + p2}")
print(f"p1 == p2: {p1 == p2}")
print(f"len(p1): {len(p1)}")
