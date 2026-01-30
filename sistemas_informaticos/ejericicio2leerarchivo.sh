#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Uso: $0 <archivo_entrada> <archivo_salida>"
    exit 1
fi
ENTRADA=$1
SALIDA=$2
if [ ! -f "$ENTRADA" ]; then
    echo "Error: El archivo '$ENTRADA' no existe."
    exit 1
fi
grep '^[AEIOUaeiou]' "$ENTRADA" > "$SALIDA"

echo "Proceso finalizado. Las líneas filtradas se guardaron en '$SALIDA'."