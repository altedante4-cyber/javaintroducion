#!/bin/bash

contador_directorio=0
contador_archivos=0
contador_otros=0
while [ $# -gt 0 ]; do
    if [ -d "$1" ]; then
        ((contador_directorio++))
    elif [ -f "$1" ]; then
        ((contador_archivos++))
    else
        ((contador_otros++))
    fi
    shift
done

echo "------------------------------------------"
echo "Análisis de parámetros finalizado:"
echo "Directorios: $contador_directorio"
echo "Archivos:    $contador_archivos"

if [ $contador_otros -gt 0 ]; then
    echo "Otros (no existen o especiales): $contador_otros"
fi
echo "------------------------------------------"