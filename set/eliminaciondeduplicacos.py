def procesar_usuarios_unicos(lista_usuarios):
    # Convertir a set elimina duplicados al instante
    usuarios_unicos = set(lista_usuarios)
    for usuario in usuarios_unicos:
        print(f"Enviando correo a: {usuario}")

# Uso
procesar_usuarios_unicos(["ana", "pedro", "ana", "luis", "pedro"])

