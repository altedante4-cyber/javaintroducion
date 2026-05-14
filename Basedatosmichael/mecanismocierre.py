import mysql.connector
from contextlib import closing


try:
    with closing(mysql.connector.connect(user="admin",passwd="1234",host="localhost",database="pokemondb")) as conexion:
        with closing(conexion.cursor() ) as cursor :
            texto = "insert into pokemon values (152,'Chikorita',6.4 ,0.9)"
            cursor.execute(texto)
            print(cursor.rowcount , "filas afectadas ")
            conexion.commit()

            print("conexion ralizada correctamente")

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
