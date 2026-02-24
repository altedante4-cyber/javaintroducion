from datetime import date ,time,datetime,timedelta

#dentrode670dias = hoy + timedelta(days=670) #calcula que fecha sera dentro de 67 dias


#class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)¶

def sacar_dia(fecha:str):

    dia = ""

    for i in range(len(fecha)-1):

        for j in range(i+1,len(fecha)-1):


hoy = date.today()

now = datetime.now()

#Datetime
print("El día actual es {}".format(now.day))
print("El mes actual es {}".format(now.month))
print("El año actual es {}".format(now.year))
print("La hora actual es {}".format(now.hour))
print("El minuto actual es {}".format(now.minute))
print("El segundo actual es {}".format(now.second))
#emtod para formaaterr y separar los dias - mes - annos



pedir_cita = input("Registro y primera cita: " )

#necesitamos seis citas y que el rango entre esas citas seas de 200




