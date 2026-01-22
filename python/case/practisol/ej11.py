#9. Simulación de Clima ☀️🌧️
#Erea una lista de posibles estados del clima (["Soleado", "Nublado", "Lluvia", "Nieve"]). Simula el clima para los próximos 7 días. Usa un bucle for y random.choice() para seleccionar un clima para cada día. Si el clima es "Lluvia" o "Nieve", imprime "¡Recuerda tu paraguas!".

import random

clima = ["soleado","nublado","lluvia","Nieve"]


for i in range(1,8):

    dia = random.choice(clima)
    
    #iimprime el pronostico del dia

    print(f"Dia {i} : {dia}")



    #2.usa condicionales para dar una advertencia

    if dia =='lluvia' or dia =='Nieve':
        print("          recuerda tu paraguas")


print("----Fin de la Simulacion")


#dia1 =>sol
#dia2 => Lluvia => "recuerda tu paraguas"
#dia3 => nieve