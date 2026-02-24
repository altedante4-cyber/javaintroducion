def validar_permisos(solicitados):
    permisos_validos = {"leer", "escribir", "borrar", "actualizar"}

    # ¿Hay algún permiso solicitado que no sea válido?
    invalidos = solicitados - permisos_validos

    if invalidos:
        return f"Error: Los siguientes permisos no existen: {invalidos}"
    return "Todos los permisos son correctos"


# Uso
print(validar_permisos({"leer", "ejecutar"}))  # El set resultante será {"ejecutar"}