from datetime import datetime, date


def _es_hex(caracter):
    return caracter.isdigit() or caracter.lower() in "abcdef"


def _todas_hex(cadena):
    return all(_es_hex(c) for c in cadena)


def validar_email(email):
    if "@" not in email:
        return False
    partes = email.split("@")
    if len(partes) != 2:
        return False
    local, dominio = partes
    if not local or not dominio:
        return False
    if "." not in dominio:
        return False
    return True


def validar_telefono(telefono, longitud=10):
    solo_digitos = telefono.replace("+", "").replace(" ", "").replace("-", "")
    if not solo_digitos.isdigit():
        return False
    return len(solo_digitos) >= longitud


def validar_url(url):
    if url.startswith("http://") or url.startswith("https://"):
        resto = url.split("://", 1)[1]
        if not resto:
            return False
        if "." in resto:
            return True
    return False


def validar_rfc_mx(rfc):
    rfc = rfc.upper()
    if len(rfc) not in (12, 13):
        return False
    letras = rfc[:len(rfc)-9]
    numeros = rfc[len(rfc)-9:len(rfc)-3]
    homonimos = rfc[len(rfc)-3:]
    if not all(c.isalpha() for c in letras):
        return False
    if not numeros.isdigit() or len(numeros) != 6:
        return False
    if not all(c.isalnum() for c in homonimos):
        return False
    return True


def validar_curp_mx(curp):
    curp = curp.upper()
    if len(curp) != 18:
        return False
    letras = curp[:4]
    fecha = curp[4:10]
    sexo = curp[10]
    entidad = curp[11:13]
    consonantes = curp[13:16]
    diferencia = curp[16]
    digito = curp[17]
    if not all(c.isalpha() for c in letras):
        return False
    if not fecha.isdigit():
        return False
    if sexo not in ("H", "M"):
        return False
    if not all(c.isalpha() for c in entidad):
        return False
    if not all(c.isalpha() for c in consonantes):
        return False
    if not diferencia.isalnum():
        return False
    if not digito.isdigit():
        return False
    return True


def validar_fecha(fecha_str, formato="%Y-%m-%d"):
    try:
        datetime.strptime(fecha_str, formato)
        return True
    except ValueError:
        return False


def validar_rango_fecha(fecha_str, inicio, fin, formato="%Y-%m-%d"):
    try:
        fecha = datetime.strptime(fecha_str, formato)
        fecha_ini = datetime.strptime(inicio, formato)
        fecha_fin = datetime.strptime(fin, formato)
        return fecha_ini <= fecha <= fecha_fin
    except ValueError:
        return False


def validar_edad(fecha_nacimiento, edad_min=18, formato="%Y-%m-%d"):
    try:
        nacimiento = datetime.strptime(fecha_nacimiento, formato).date()
        hoy = date.today()
        edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
        return edad >= edad_min
    except ValueError:
        return False


def validar_hora(hora_str, formato="%H:%M"):
    try:
        datetime.strptime(hora_str, formato)
        return True
    except ValueError:
        return False


def validar_ipv4(ip):
    partes = ip.split(".")
    if len(partes) != 4:
        return False
    for p in partes:
        if not p.isdigit():
            return False
        if p != str(int(p)):
            return False
        if not (0 <= int(p) <= 255):
            return False
    return True


def validar_ipv6(ip):
    if "::" in ip:
        partes = ip.split("::")
        if len(partes) > 2:
            return False
        izquierda = partes[0].split(":") if partes[0] else []
        derecha = partes[1].split(":") if len(partes) > 1 and partes[1] else []
        total = izquierda + ["0"] * (8 - len(izquierda) - len(derecha)) + derecha
    else:
        total = ip.split(":")
        if len(total) != 8:
            return False
    for grupo in total:
        if not grupo:
            return False
        if len(grupo) > 4:
            return False
        if not _todas_hex(grupo):
            return False
    return True


def validar_nombre_usuario(usuario, min_len=3, max_len=30):
    if not (min_len <= len(usuario) <= max_len):
        return False
    for c in usuario:
        if not c.isalnum() and c != "_":
            return False
    return True


def validar_contrasena(contrasena, min_len=8):
    errores = []
    if len(contrasena) < min_len:
        errores.append(f"Debe tener al menos {min_len} caracteres")
    tiene_mayus = False
    tiene_minus = False
    tiene_num = False
    tiene_especial = False
    especiales = "!@#$%^&*(),.?\":{}|<>_-"
    for c in contrasena:
        if c.isupper():
            tiene_mayus = True
        elif c.islower():
            tiene_minus = True
        elif c.isdigit():
            tiene_num = True
        elif c in especiales:
            tiene_especial = True
    if not tiene_mayus:
        errores.append("Debe contener al menos una mayuscula")
    if not tiene_minus:
        errores.append("Debe contener al menos una minuscula")
    if not tiene_num:
        errores.append("Debe contener al menos un numero")
    if not tiene_especial:
        errores.append("Debe contener al menos un caracter especial")
    return errores


def validar_tarjeta_credito(numero):
    numero = numero.replace(" ", "").replace("-", "")
    if not numero.isdigit():
        return False
    if not (13 <= len(numero) <= 19):
        return False
    suma = 0
    alternar = False
    for digito in reversed(numero):
        d = int(digito)
        if alternar:
            d *= 2
            if d > 9:
                d -= 9
        suma += d
        alternar = not alternar
    return suma % 10 == 0


def validar_codigo_postal(cp, pais="MX"):
    cp = cp.strip()
    p = pais.upper()
    if p == "MX" or p == "ES":
        return len(cp) == 5 and cp.isdigit()
    elif p == "US":
        if len(cp) == 5 and cp.isdigit():
            return True
        if len(cp) == 10 and cp[5] == "-" and cp[:5].isdigit() and cp[6:].isdigit():
            return True
        return False
    elif p == "AR":
        return len(cp) == 4 and cp.isdigit()
    elif p == "CL":
        return len(cp) == 7 and cp.isdigit()
    elif p == "CO":
        return len(cp) == 6 and cp.isdigit()
    return False


def validar_numero_entero(valor, minimo=None, maximo=None):
    try:
        n = int(valor)
        if minimo is not None and n < minimo:
            return False
        if maximo is not None and n > maximo:
            return False
        return True
    except (ValueError, TypeError):
        return False


def validar_numero_decimal(valor, minimo=None, maximo=None):
    try:
        n = float(valor)
        if minimo is not None and n < minimo:
            return False
        if maximo is not None and n > maximo:
            return False
        return True
    except (ValueError, TypeError):
        return False


def validar_longitud_cadena(valor, min_len=0, max_len=None):
    if len(valor) < min_len:
        return False
    if max_len is not None and len(valor) > max_len:
        return False
    return True


def validar_solo_letras(valor, permitir_espacios=False):
    for c in valor:
        if not c.isalpha() and c not in "áéíóúüñÁÉÍÓÚÜÑ":
            if permitir_espacios and c == " ":
                continue
            return False
    return True


def validar_solo_numeros(valor):
    return valor.isdigit()


def validar_hex_color(color):
    if not color.startswith("#"):
        return False
    resto = color[1:]
    if len(resto) not in (3, 6):
        return False
    return _todas_hex(resto)


def validar_uuid(uuid_str):
    uuid_str = uuid_str.lower()
    partes = uuid_str.split("-")
    longitudes = [8, 4, 4, 4, 12]
    if len(partes) != 5:
        return False
    for parte, long in zip(partes, longitudes):
        if len(parte) != long:
            return False
        if not _todas_hex(parte):
            return False
    return True


def validar_slug(slug):
    if not slug:
        return False
    if slug.startswith("-") or slug.endswith("-"):
        return False
    partes = slug.split("-")
    for parte in partes:
        if not parte:
            return False
        for c in parte:
            if not c.isalnum():
                return False
    return True


def validar_booleano(valor):
    if isinstance(valor, bool):
        return True
    if isinstance(valor, str):
        return valor.lower() in ("true", "false", "1", "0", "yes", "no", "si", "no")
    return False


def validar_lista_vacia(lista):
    return len(lista) == 0


def validar_elementos_unicos(lista):
    return len(lista) == len(set(lista))


def validar_extension_archivo(nombre, extensiones_permitidas):
    for ext in extensiones_permitidas:
        if nombre.lower().endswith(ext.lower()):
            return True
    return False


def validar_sin_etiquetas_html(texto):
    i = 0
    while i < len(texto):
        if texto[i] == "<":
            j = texto.find(">", i)
            if j == -1:
                return True
            i = j + 1
        else:
            i += 1
    return "<" not in texto


def validar_sin_espacios_extremos(texto):
    return texto == texto.strip()


def validar_no_nulo_o_vacio(valor):
    if valor is None:
        return False
    if isinstance(valor, str) and valor.strip() == "":
        return False
    if isinstance(valor, (list, dict, tuple, set)) and len(valor) == 0:
        return False
    return True


def validar_tipo_dato(valor, tipo_esperado):
    return isinstance(valor, tipo_esperado)


def validar_coordenadas(latitud, longitud):
    return -90 <= latitud <= 90 and -180 <= longitud <= 180


def validar_sha256(hash_str):
    hash_str = hash_str.lower()
    if len(hash_str) != 64:
        return False
    return _todas_hex(hash_str)


def validar_md5(hash_str):
    hash_str = hash_str.lower()
    if len(hash_str) != 32:
        return False
    return _todas_hex(hash_str)


def validar_base64(cadena):
    caracteres_validos = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=")
    for c in cadena:
        if c not in caracteres_validos:
            return False
    if len(cadena) % 4 != 0:
        return False
    return True


def validar_dominio(dominio):
    if not dominio:
        return False
    partes = dominio.split(".")
    if len(partes) < 2:
        return False
    for parte in partes:
        if not parte:
            return False
        if parte.startswith("-") or parte.endswith("-"):
            return False
        for c in parte:
            if not c.isalnum() and c != "-":
                return False
    return len(partes[-1]) >= 2


def validar_puerto(puerto):
    return isinstance(puerto, int) and 0 <= puerto <= 65535


def validar_iban(iban):
    iban = iban.replace(" ", "").upper()
    if len(iban) < 4 or len(iban) > 34:
        return False
    for c in iban[:2]:
        if not c.isalpha():
            return False
    for c in iban[2:]:
        if not c.isalnum():
            return False
    iban_reordenado = iban[4:] + iban[:4]
    caracteres = ""
    for c in iban_reordenado:
        if c.isalpha():
            caracteres += str(ord(c) - 55)
        else:
            caracteres += c
    try:
        return int(caracteres) % 97 == 1
    except ValueError:
        return False


def validar_nss_mx(nss):
    return len(nss) == 11 and nss.isdigit()


def validar_version_semantica(version):
    partes = version.split(".")
    if len(partes) < 3:
        return False
    for i in range(3):
        if not partes[i].isdigit():
            return False
    return True


def validar_ascii(texto):
    for c in texto:
        if ord(c) >= 128:
            return False
    return True


def validar_json(cadena):
    if not cadena:
        return False
    cadena = cadena.strip()
    if cadena.startswith("{") and cadena.endswith("}"):
        return True
    if cadena.startswith("[") and cadena.endswith("]"):
        return True
    return False


def validar_solo_mayusculas(valor):
    return valor == valor.upper() and any(c.isalpha() for c in valor)


def validar_solo_minusculas(valor):
    return valor == valor.lower() and any(c.isalpha() for c in valor)


def validar_rango_tamano(valor, min_val, max_val):
    return min_val <= len(valor) <= max_val
