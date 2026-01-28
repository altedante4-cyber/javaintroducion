
echo "Has subido $# archivos."

archivo="nombres.txt"

# Verificamos si el archivo de destino existe
if [ ! -f "$archivo" ]; then
    touch "$archivo"
    echo "Archivo $archivo creado correctamente."
fi 

# Bucle para procesar argumentos
while (( $# > 0 )); do
    echo "$1" >> "$archivo"
    
    echo "Escrito con éxito: $1"
    
    # Movemos la fila de parámetros
    shift
done
 
echo "Proceso finalizado. Revisa $archivo"
