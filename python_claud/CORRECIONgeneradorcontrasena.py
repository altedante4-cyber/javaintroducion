import string
import random
def generar_contrasena(longitud, mayus, nums,esps):
    caracteres_pool = string.ascii_lowercase #base siempre en minusculas
    obligatorios = []
    #1.construir el pool y asegurar unminimo de cada uno

    if mayus == "si":
        caracteres_pool += string.ascii_uppercase
        obligatorios.append(random.choice(string.ascii_uppercase))

    if nums == "si":
        caracteres_pool += string.digits
        obligatorios.append(random.choice(string.digits))

    if esps == "si":
        caracteres_pool += string.punctuation
        obligatorios.append(random.choice(string.punctuation))

    #2 rellnear el reesto de la longitud
    #usamos random.choices (con 's' al final ) para elegir varios a la vez

    resto_longitud = longitud - len(obligatorios )
    if resto_longitud < 0 : return "Longitud muy corta"

    relleno = random.choices(caracteres_pool , k=resto_longitud)

    #3.Mezclar todo para que no sea predecible 

    password_list = obligatorios + relleno
    random.shuffle(password_list)

    return "".join(password_list)

def evaluar_fortaleza(password):
    n = len(password)

    #verificamos variedad usanod sets o any()

    tiene_mayus = any(c.isupper() for c in password ) #deuvelv ture si al menos uno de los elemenots del iterable ses verdadero
    tiene_nums = any(c.isdigit() for c in password )
    tiene_esps = any(c in string.punctuation for c in password )
# piensa en any() como un operador or gigantee que conecta a todos los elementos 
    #logica de puntuciono devuelve true si encnetra almenos uno 

    puntos = sum([tiene_mayus + tiene_nums + tiene_esps])
    if n >= 12 and puntos >= 2 :
        return "FUERTE"

    elif n >= 8 and puntos >= 1:
        return "MEDIA"
    else:
        return "DEBIL"
    
cant = int(input("Cuantas contase quieres generar?"))
lon = int(input("LONGITUD"))
m = input("mayusculas si o no ").lower()
n = input("nuemeros si ono ").lower()
e = input("especiales si o no  ").lower()

print("\n -- RESULTADOS -- ")
for i in range(cant):
    pwd = generar_contrasena(lon , m , n , e )
    fort = evaluar_fortaleza(pwd)
    print(f"contrasena {i + 1} : {pwd:<20} | fortaleza {fort}")

#random.choices(pool, k= n ) es mucho mas rapido que hace 