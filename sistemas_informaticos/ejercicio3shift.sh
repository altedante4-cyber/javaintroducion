#!/bin/bash

#verificar si se le paso parametros 

if [ $# -eq 0 ]; then
    echo "Error no se introdujeron parámetros."
    exit 1 #salimos 
fi

# 2. Comprobamos si el archivo de destino existe
archivo="pruebashift"

if [ ! -f "$archivo" ]; then
    echo "Creando archivo no existente..."
    touch "$archivo"
    echo "Creado correctamente."
else 
    echo "El archivo '$archivo' ya existe. Se añadirán los nuevos datos."
fi

#ahora si que si pasamos los parametros al archivo destino 
while [ $# -ne 0 ]; do
    echo "$1" >> "$archivo"
    shift 
done

echo "Parámetros agregados correctamente."

#la opcion lo que hace es guardar los resultado en el mismo archivo

sort "$archivo" -o "$archivo"

echo "Archivo ordenado alfabéticamente."