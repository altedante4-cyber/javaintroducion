#!/bin/bash

#validacion de parametros
if [ $# -lt 5 ] || [ $# -gt 8 ]; then
    echo "Error: Debes introducir entre 5 y 8 nombres."
    echo "Uso: $0 nombre1 nombre2 ... nombreN"
    exit 1
fi

FICHERO="nombres.txt"

> "$FICHERO" #limpiar fichero si existia
for nombre in "$@"; do
    echo "$nombre" >> "$FICHERO"
done

echo "--- Contenido del fichero ($FICHERO) ---"
cat "$FICHERO"

echo -e "\n--- Nombres en orden inverso ---"
sort -r "$FICHERO"