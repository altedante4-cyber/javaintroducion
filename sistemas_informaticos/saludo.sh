#!/bin/bash

echo -n "Ingrese el nombre: "
read Nombre
echo -n "Ingrese el apellido: "
read Apellido

echo "Hola $Nombre $Apellido "

# Nota los espacios después de '[' y antes de ']'
if [ "$Nombre" == "$Apellido" ]
then 
    echo "Las variables son iguales"
else
    echo "Las variables no son iguales"
fi
