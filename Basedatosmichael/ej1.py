import mysql.connector


try:

    conexion = mysql.connector.connect(user="admin",passwd="1234",host="localhost",database="sakila")

    print("conexion ralizada correctamente")
    cursor = conexion.cursor()
    #cursor.execute("select first_name , last_name  from actor ")
    cursor.execute("select * from actor ")


    #for first_name , last_name in cursor:
     #   print(first_name,last_name )

    #for fila in cursor:
     #   print(fila[1],fila[2])

    resultado = cursor.fetchall()

    print("El select ha devuelvto", len(resultado),"lineas")
    for linea in resultado:
        print(linea[1],linea[2])

    cursor.close()
    conexion.close()

except mysql.connector.Error as err:
    print(err)
