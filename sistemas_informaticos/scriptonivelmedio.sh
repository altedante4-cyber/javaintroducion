#!/bin/bash
echo -n "Ingrese el nombre del directorio"
read name

if [ -d "$name" ];then
    cd $name
    echo -n "Ingrese la palabra a buscar : " 
    read palabra 

    for archivo in *"$palabra"*;do
     if [ -f $archivo ];then
        echo "Desea eliminar el archivo $archivo"
        read opcion 

        if [ "$opcion" == "s" ];then
            rm $archivo 
            echo "eliminado correctamente el archivo"
            echo "mostrando el directorio "
            ls .
        else
            echo "el archivo no ha podido ser eliminado"         
        fi
     fi 
    done 

else
    echo "directorio no existe"
fi
