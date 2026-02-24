print("Inicio del programa")
entrada = input("Escribe un numero")
try:
    print("Antes del posible error")
    numero = int(entrada)
    division = 50/numero
    print("Despues del posible error")

except ValueError:
    print("No puedo convertir eso en un numero ")
except ZeroDivisionError:
    print("No puedo diviri entre cero ")
except:
    print("Ha ocurrido un error pero no se cual es ")

#para saber la excepsion tnemos que mirar  las lineas de abajo python te lo dice

#se ejecuta sin no hay excepsiones
else:
    print("No ha  habido errores ") # pasa aqui si no havido ninguna excepsion   si habido no assa por aqui
finally:
    print("Eso se ejecuta siempre ")

print("Fin del programa")