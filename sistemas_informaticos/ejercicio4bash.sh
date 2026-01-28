if [ -d dir1 ]
then
    echo "El directorio $dir1 ya existe en el sistema"
else
    mkdir dir1
    echo "Creado el directorio dir1"
    
    cd dir1
    touch fich
    
    echo "Creado el directorio -fich"  # Nota: esto crea un archivo, no un directorio
    
    ls /dev/t*[0-9] >> fich
    cat /etc/passwd >> fich
    echo "Llenado el fichero -fich-."
    echo "Contenido del fichero -fich-:"
    more fich
fi