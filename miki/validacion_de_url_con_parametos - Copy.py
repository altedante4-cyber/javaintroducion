def validar_url(url:str):

    #veerifvcar que empiese con http://

    primer_parte_https = url.startswith("https://")
    segunda_parte_http = url.startswith("http://")

    #extraer el dominio si lo hay

    separar = url.split("/")

    dominio = separar[2]
    separar_parametros = url.split("&")









print(validar_url("https://ejemplo.com/search?q=python&page=2"))