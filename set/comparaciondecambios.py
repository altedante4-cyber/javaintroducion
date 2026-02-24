def sincronizar_etiquetas(viejas, nuevas):
    etiquetas_viejas = set(viejas)
    etiquetas_nuevas = set(nuevas)

    # Elementos a añadir
    añadir = etiquetas_nuevas - etiquetas_viejas

    # Elementos a borrar
    borrar = etiquetas_viejas - etiquetas_nuevas

    return añadir, borrar

# Uso: tags_add, tags_del = sincronizar_etiquetas(db_tags, input_tags)