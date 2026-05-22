empresa = {
    "ventas": {"Ana": 150, "Luis": 200},
    "it": {"Carlos": 180, "Marta": 220},
}

todos = {}
for depto, personas in empresa.items():
    for nombre, sueldo in personas.items():
        todos[nombre] = {"departamento": depto, "sueldo": sueldo}

empleados = {
    "E001": {"nombre": "Ana", "cargo": "Analista", "hijos": 2},
    "E002": {"nombre": "Luis", "cargo": "Developer", "hijos": 0},
    "E003": {"nombre": "Marta", "cargo": "Manager", "hijos": 1},
}

for cod, info in empleados.items():
    info["plus"] = info["hijos"] * 50

cargo_orden = dict(sorted(empleados.items(), key=lambda x: x[1]["cargo"]))

print("Todos combinados:", todos)
print("Empleados con plus:", empleados)
print("Orden por cargo:", cargo_orden)
