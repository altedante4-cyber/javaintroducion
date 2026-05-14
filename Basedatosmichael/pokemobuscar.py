
import mysql.connector
from contextlib import closing


try:
    with closing(mysql.connector.connect(user="admin",passwd="1234",host="localhost",database="pokemondb")) as conexion:
        with closing(conexion.cursor() ) as cursor :
            def insertar_elemento(numero, nombre, peso, altura, tipo1=None, tipo2=None):
                texto = "insert into pokemon values (%s,'%s',%s ,%s)"

                cursor.execute(texto, (numero, nombre, peso, altura))
                filas = cursor.rowcount
                conexion.commit()

                return filas if filas else 0


            filas_afectadas = insertar_elemento(152, 'hola', 6.4, 0.9)
            print(filas_afectadas)
except mysql.connector.Error as err:
        print(err)

