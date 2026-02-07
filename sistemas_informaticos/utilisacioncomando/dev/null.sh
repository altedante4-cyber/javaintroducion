#!/bin/bash

# En Git Bash, las rutas de Windows se escriben así:
dir="/c/Users/aguil/javaintroducion/sistemas_informaticos/utilisacioncomando/dev"

# Nota los espacios después de [ y antes de ]
if [ -d "$dir" ]; then
    for i in "$palabra"* ;do 
    rm "$i" > /dev/null ;
    done 
else
    echo "no es un directorio"
fi