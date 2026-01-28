case $# in 
   if [ -f $1 ]
   then 
        echo "Elegido un solo archivo"
        echo "Introdusca el texto que desea ingresar en el fichero"
        read linea
        echo $linea >> $1
        echo "copiado correctamente"

    else
        echo "No se copio el contenido vuelve a intentarlo"

    fi;;
    
   if [ -f $1 -a -f $2 ]
   then
        echo "Elegido dos archivos"
        echo "Copiando los dos archivos de archivo $1 a archivo $2"
        cat $1 >> $2

        echo "Copiado corretamente"
    else
        echo "NO se puedo copiar el contenido del arhcivo $1 al archivo $2"

    fi;;

*)  echo "Ningun parametro seleccionado" ;;
esac


