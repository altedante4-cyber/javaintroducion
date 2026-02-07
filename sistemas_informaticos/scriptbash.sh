#!/bin/bash

if [ $# -ne 1 ]
then 
    echo "hay que incluir el nombre de un fichero como parametro"
elif [ -f "$1" ]
then 
    echo "copia fichero -$1 -al directorio -tmp y lo borro"
        
    if [ ! -d "tmp" ]
    then 
        mkdir tmp
    fi
    
    cp "$1" tmp
    rm -f "$1"

else 
    echo "el parametro $1 no es un fichero!!"
fi
