#escribir fichero 

# FORMA 1: open() + close() manual
# open("ruta", "modo") devuelve un objeto fichero.
#   "w" (write):  abre el fichero para escritura.
#                 SI existe, lo SOBREESCRIBE desde cero.
#                 SI no existe, lo CREA.
#   "a" (append): abre el fichero para escritura.
#                 NO borra el contenido existente.
#                 Empieza a escribir al FINAL del archivo.
#   "t" (text):   modo texto (se puede omitir, es el default).
# ------------------------------------------------------------

fichero = None
try:
    # "at" = append + text mode. Agrega contenido al final.
    fichero = open("fichero.txt", "at")
    fichero.write("Texto agregado al final\n")
except Exception as e:
    print("Error al abrir/escribir el fichero:", e)
finally:
    # finally se ejecuta SIEMPRE, haya error o no.
    # Aquí cerramos el fichero manualmente para liberar recursos.
    if fichero is not None:
        fichero.close()


# ------------------------------------------------------------
# FORMA 2 (RECOMENDADA): with open()
# ------------------------------------------------------------
# El bloque "with" se encarga AUTOMÁTICAMENTE de cerrar
# el fichero al salir del bloque, incluso si ocurre una
# excepción. No hace falta llamar a .close().
# ------------------------------------------------------------

# "w"  => write. Borra todo y escribe desde el principio.
with open("fichero.txt", "w") as f:
    f.write("Esto borra el contenido anterior\n")
    f.write("y escribe estas líneas desde cero.\n")

# "a"  => append. Agrega al final sin borrar.
with open("fichero.txt", "a") as f:
    f.write("Esto se agrega al final\n")
    f.write("sin borrar lo que ya había.\n")

