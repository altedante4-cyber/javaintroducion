from datetime import time , datetime , timedelta 

# citas programadas cada 200 dias


def convertir_fecha(citar:str):

    convertir = datetime.strptime(citar , "%d-%m-%Y %H:%M")
    for i in range(6):
        proxima_cita = convertir + timedelta(days=200 * (i+1))

        print(proxima_cita)


cita = datetime.now()

#ahora formateamos el objeto para que pueda valerse entonces lo hacemos con el srtftime


formateada = cita.strftime(f"%d del %m  del %Y  a las %H:%M ") #ahora mismo esto esta en string 

convertir_fecha(cita)
 