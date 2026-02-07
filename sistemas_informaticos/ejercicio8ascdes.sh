#!/bin/bash
orden=$1 #leer el primer parametro 
shift 

declare -a palabras 
posicion=0

if [ "$orden" == "ASC" ]; then
    echo "Operacion ascendente"

    # Llenamos el arreglo
    while [ "$#" -gt 0 ]; do
         palabras[posicion]=$1
         ((posicion++)) # Incremento correcto
         shift 
    done

    for p in "${palabras[@]}";do
        echo "$p"
    done | sort

elif [ "$orden" == "DESC" ]; then
    echo "Operacion descendente"
    
    while [ "$#" -gt 0 ]; do
         palabras[posicion]=$1
         ((posicion++))
         shift 
    done

    #para ordenar descendentemende utilizamos la opcion -r de sort

    for k in "${palabras[@]}";do
        echo "$k"
    done | sort -r
fi