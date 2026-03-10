from datetime import datetime, timedelta

# 1. Obtener fecha y hora actual
ahora = datetime.now()

# Formatear la salida inicial
# %d: día, %m: mes, %Y: año, %H:%M: hora y minutos
print(f"Registro y primera cita: {ahora.strftime('%-d del %m de %Y a las %H:%M')}")
print("Siguientes citas:")

# 2. Calcular las 6 citas siguientes
fecha_cita = ahora
for i in range(1, 7):
    fecha_cita += timedelta(days=200)
    print(f"{i} - {fecha_cita.strftime('%-d del %m de %Y')}")