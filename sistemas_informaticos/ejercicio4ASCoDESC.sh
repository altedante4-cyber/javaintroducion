#!/bin/bash

MODO=$1
shift 

# Verificamos si queremos orden Ascendente
if [ "$MODO" == "ASC" ]; then
    # Usamos un bucle para hacer echo de cada palabra y pasarlo a sort
    for palabra in "$@"; do
        echo "$palabra"
    done | sort

elif [ "$MODO" == "DESC" ]; then
    for palabra in "$@"; do
        echo "$palabra"
    done | sort -r

else
    echo "Error: El primer parámetro debe ser ASC o DESC"
fi