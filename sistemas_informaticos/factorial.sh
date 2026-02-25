#!/bin/bash

##!/bin/bash
#echo "Nombre del script: $0"
#echo "Primer parámetro: $1"
#echo "Segundo parámetro: $2"
#echo "Todos los parámetros: $@"
#echo "Número total de parámetros: $#"



# 1. Verificamos que se haya pasado exactamente UN argumento
if [ $# -eq 1 ]; then

    # 2. Verificamos si el valor de ese argumento está entre 3 y 8
    if (( $1 >= 3 && $1 <= 8 )); then
          
          for (( i = 1 ; i < $1 ; i++ )); do
            echo "$i"
          done

    else
        echo "El valor $1 NO se encuentra en el rango"
    fi 

else
    # Si hay 0 o más de 1 argumento
    echo "Error: Debes introducir exactamente un parámetro."
fi