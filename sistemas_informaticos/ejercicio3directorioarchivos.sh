#!/bin/bash

dir_count=0
file_count=0

for param in "$@"; do
    if [ -d "$param" ]; then
        ((dir_count++))
    elif [ -f "$param" ]; then
        ((file_count++))
    fi
done

echo "Se han pasado $# parámetros."
echo "Directorios: $dir_count"
echo "Archivos: $file_count"