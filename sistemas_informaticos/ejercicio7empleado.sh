#!/bin/bash

FICHERO="empleados.txt"
opcion=0

until [ $opcion -eq 5 ]; do
    echo -e "\n--- MENÚ EMPLEADOS ---"
    echo "1.- Mostrar sólo empleados"
    echo "2.- Alta de todos los empleados"
    echo "3.- Baja de todos los empleados"
    echo "4.- Bloquear todos los empleados"
    echo "5.- Salir"
    read -p "Elija opción: " opcion

    case $opcion in
        1)
            echo "Listado de empleados:"
            if [ -f "$FICHERO" ]; then
                cat "$FICHERO"
            else
                echo "No hay empleados registrados."
            fi
            ;;
        2)
            read -p "Nombre: " nom
            read -p "Salario: " sal
            echo "$nom:$sal" >> "$FICHERO"
            ;;
        3)
            > "$FICHERO"
            echo "Fichero vaciado correctamente."
            ;;
        4)
            if [ -s "$FICHERO" ]; then
                touch temporal.txt
                
                while read linea; do
                    echo "BLOQUEADO:$linea" >> temporal.txt
                done < "$FICHERO"
                
                mv temporal.txt "$FICHERO"
                echo "Todos los empleados han sido bloqueados."
            else
                echo "El fichero está vacío, nada que bloquear."
            fi
            ;;
        5) echo "Saliendo..." ;;
        *) echo "Opción no válida." ;;
    esac
done