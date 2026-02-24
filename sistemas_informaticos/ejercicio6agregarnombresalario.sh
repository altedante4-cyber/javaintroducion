#!/bin/bash

echo -n "Nombre del empleado: "
read nombre
echo -n "Salario: "
read salario


echo "$nombre:$salario" >> empleados.txt
echo "Datos guardados."