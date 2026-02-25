#!/bin/bash

if [ $# -ne 3 ]; then
    echo "Necesito exactamente 3 palabras."
    exit 1
fi

P1=$1
P2=$2
P3=$3

if [ "$P1" == "$P2" ] && [ "$P2" == "$P3" ]; then
    echo "Las tres son iguales"
elif [ "$P1" == "$P2" ]; then
    echo "Son iguales primera y segunda"
elif [ "$P1" == "$P3" ]; then
    echo "Son iguales primera y tercera"
elif [ "$P2" == "$P3" ]; then
    echo "Son iguales segunda y tercera"
else
    echo "Son las tres distintas"
fi