#!/bin/bash
if [ $# -eq 2 ]
then
 echo "1er. número: $1."
 echo "2do. número: $2."
 if [ $1 -eq $2 ]
 then
  relacion='='
 else
  if [ $1 -lt $2 ]
  then 
   relacion='<'
  else
   relacion='>'
  fi
 fi
 echo "Relación: $1 $relacion $2"
else
 echo "Formato: $0 num1 num2 !!!"
fi  