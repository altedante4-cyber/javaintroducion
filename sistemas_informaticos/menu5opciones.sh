#!/bin/bash

opcion=0

until [ $opcion -eq 5 ]; do 
    echo -e "\n--- MENU DE GESTIÓN ---"
    echo "1.- Crear directorio" 
    echo "2.- Borrar directorio" 
    echo "3.- Crear fichero" 
    echo "4.- Borrar fichero" 
    echo "5.- Salir" 

    echo -n "Ingrese la opción: " 
    read opcion   

    case $opcion in
        1) read -p "Nombre carpeta: " d; mkdir "$d" ;;
        2) read -p "Nombre carpeta: " d; rmdir "$d" ;;
        3) read -p "Nombre fichero: " f; touch "$f" ;;
        4) read -p "Nombre fichero: " f; rm "$f" ;;
        5) echo "Saliendo..." ;;
        *) echo "Opción no válida" ;;
    esac
done

