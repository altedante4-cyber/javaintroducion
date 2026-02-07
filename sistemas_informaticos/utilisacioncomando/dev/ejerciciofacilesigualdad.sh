#!/bin/bash

if [ $# -ne 3 ]; then
    echo "Erro tiene que ser 3 palabras"
    echo "Uso: $0 palabra1 palabra2 palabra3"
    exit 1
fi

p1=$1
p2=$2
p3=$3

if [[ "$p1" == "$p2" && "$p2" == "$p3" ]]; then
    echo "Las tres son iguales"
elif [[ "$p1" == "$p2" ]]; then
    echo "Son iguales primera y segunda"
elif [[ "$p1" == "$p3" ]]; then
    echo "Son iguales primera y tercera"
elif [[ "$p2" == "$p3" ]]; then
    echo "Son iguales segunda y tercera"
else
    echo "Son las tres distintas"
fi
