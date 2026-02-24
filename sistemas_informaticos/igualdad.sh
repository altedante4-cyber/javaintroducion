#!/bin/bash

#Realice un shell-script que admita tres palabras como argumentos y quemuestre un mensaje informando de las relaciones 
#de igualdad y desigualdad entre esas palabras."Las tres son iguales""
#Son iguales primera y segunda""Son iguales primera y tercera""Son iguales segunda y tercera""Son las tres distintas"


declare -a array 

if (( $#  <= 3 ));then

    if [[ $1 == $2  && $1 == 3 ]];then
    
         echo "son iguales las tres"
    elif [[ $2 == $1 && $2 != 3 ]];then
        echo "son iguales las dos primeras"
    
    elif [[ $1 == $3 && $1 != $2  ]];then

        echo "son iguales el primero y el tercero"
     elif [[ $2 == $3 && $2 != $1  ]];then

        echo "son iguales el primero y el tercero"
    else
        echo "los tres son distintos"

    fi

else 
    echo "has introducido demasiados parametros"

fi 
