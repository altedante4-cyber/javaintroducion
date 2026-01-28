#!/bin/bash

opc=0 

# El bucle debe continuar mientras no sea 4 (Salir)
while [ $opc -ne 5 ]
do 
  # clear # Comentado para que puedas ver los mensajes de éxito antes de limpiar

  echo "--- MENU ---"
  echo "1. Crear un directorio"
  echo "2. Borrar un directorio"
  echo "3. Crear un fichero"
  echo "4. Borrar archivo "
  echo "6.Salir"

  echo 

  echo -n "Elige una opcion: "
  read opc 

  case $opc in 
    1) 
        echo -n "Introduce el nombre del directorio: "
        read nombre
        mkdir "$nombre"
        echo "Directorio '$nombre' creado correctamente."
        ;;
    2)
        echo -n "Nombre del directorio a borrar: "
        read nombre
        if [ -d "$nombre" ]; then
            rm -rf "$nombre"
            echo "Directorio '$nombre' borrado correctamente."
        else
            echo "Error: El directorio no existe."
        fi
        ;;
    3) 
        echo -n "Introduce el nombre del fichero: "
        read fichero
        touch "$fichero"
        echo "Fichero '$fichero' creado."
        ;;
    4) 
        echo "Ingrese el nombre del archivo a eliminar "
        read ficheroname
        if [ -f "$ficheroname" ];then

            
            rm  "$ficheroname"
            echo "Fichero '$ficheroname' borrado correctamente"
        else
            echo "Error : fichero no existe"
        fi
        ;; 
    6) 
        echo "Saliendo del programa"
        ;;
  
    *) 
        echo "Opcion invalida, vuelva a sintentarlo."
        ;;
  esac
  
  echo "Presiona Enter para continuar..."
  read
  clear
done
