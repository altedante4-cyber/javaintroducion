#!/bin/bash
opcion=0
while (( $opcion != 5 ));do

    echo "1. Mostrar empleados"
    echo "2.Alta a todos los empleados"
    echo "3. BLoquear todos los empleados"
    echo "4. Baja de todos los empelados"
    echo "5. Salir"
    read opcion 

     case $opcion in
        1) echo "==========mostrando archivo ==========="
                while IFS=, read -r nombre apellido ; do
                     echo "nombre  $nombre   y su apellido $apellido "
                  done < Empleados
            ;;
        2) read -p "Ingrese el nombre del empleado a dar de alta " name
           read -p "Ingrese el apellido del empleado a dar de alta " ape
           echo "$name","$ape" >> Empleados
           echo "Agregado correctamente"
             ;;
        3) echo "Bloqueando a todos los usuario "
          ;;
        4) echo "Dando de baja a todos los usuario ";;
        5) echo "salido " ;;
        *) echo "Error introducido un caracter invalido " ;;
    esac
done