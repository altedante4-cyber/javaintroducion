#!/bin/bash

echo "======================= CALCULADORA ====================================="
echo "Ingrese la operacion que desea realizar: + (suma), - (resta), * (multiplicacion), / (division)"
read opcion 

# --- SUMA ---
if [[ "$opcion" == "+" ]]; then
    echo -n "Seleccione el primer operando: "
    read num1 
    echo -n "Seleccione el segundo operando: "
    read num2 
    resultado=$((num1 + num2))
    echo "El resultado de la suma es: $resultado"

# --- RESTA ---
elif [[ "$opcion" == "-" ]]; then
    echo -n "Seleccione el primer operando: "
    read num1
    echo -n "Seleccione el segundo operando: "
    read num2
    resultado=$((num1 - num2))
    echo "El resultado de la resta es: $resultado"

# --- MULTIPLICACION ---
elif [[ "$opcion" == "*" ]]; then
    echo -n "Seleccione el primer operando: "
    read num1
    echo -n "Seleccione el segundo operando: "
    read num2 
    resultado=$((num1 * num2))
    echo "El resultado de la multiplicacion es: $resultado"

# --- DIVISION ---
elif [[ "$opcion" == "/" ]]; then
    echo -n "Seleccione el primer operando: "
    read num1
    echo -n "Seleccione el segundo operando: "
    read num2

    if (( num2 != 0 )); then 
        resultado=$((num1 / num2))
        echo "El resultado de la division es: $resultado"
    else
        echo "Error: No se puede dividir por cero." 
    fi
else
    echo "Operación no válida."
fi