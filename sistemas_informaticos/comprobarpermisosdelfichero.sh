
if [ $# -eq 1 ]
then
    if [ -f "$1" ]
    then
        if [ -r "$1" ]
        then
            echo "Es un fichero de solo lectura"
        elif [ -w "$1" ]
        then
            echo "Es un fichero de escritura"
        else
            echo "Es un fichero de ejecucion"
        fi
    else
        echo "Es un directorio el parametro introducido"
    fi
else
    echo "Me tienes que pasar solo un parametro"
fi