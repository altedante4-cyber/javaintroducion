from datetime import date ,time,datetime,timedelta

hoy = date.today()
print(hoy)

#Crear una fecha especifica

cumple = date(1968,10,8)
print(cumple)

#tenemos tres metodos
#date
#time
#datetime

hora = time(14,30,45)
print(hora)

#crear horas

hora_nueva = time(14)
print(hora_nueva)# si no se le especifica  los minutos ni los seundos   los pone a 0

ahora = datetime.now()
print(ahora)

citaMedico = datetime(2026,2,11,14,56)
print(citaMedico) #los compelta con 00 los segundo que no le especificamos

#el formato que nos dan es el formato anglosajon y nosotrosqueremos el formaot espanol

citaFormateada = citaMedico.strftime("%d/%m/%Y")
print(citaFormateada)

#si ademas lo quiero en hora y minutos se hace de la siguiente manera
citaFormateada = citaMedico.strftime("%d/%m/%Y a las %H:%M:%S") #tiene mas conbinaciones es decir si pones con y minuscula
print(citaFormateada)


fecha = "01/01/2022"
objetoFecha = datetime.strptime(fecha, "%d/%m/%Y") #la expecifico en el formato que viene fecha
print(objetoFecha)



hoy_nuevo = datetime.now()

if hoy_nuevo < objetoFecha:
    print(hoy_nuevo , "es anterior a " , objetoFecha)

else:
    print(objetoFecha , "es anterior a  " , hoy_nuevo)

    dentrode670dias = hoy + timedelta(days=670) #calcula que fecha sera dentro de 67 dias

    print(dentrode670dias)


    #sumarle   semanaas y hora y segundo

    dentrode670dias_nuevo = hoy + timedelta(weeks=2 , days=67, hours=4,seconds=33) #calcula que fecha sera dentro de 67 dias
    print(dentrode670dias_nuevo)


