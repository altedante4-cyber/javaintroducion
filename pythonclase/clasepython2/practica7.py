"""
Docstring for practica7


7. Sistema de votación único
Crea un sistema donde:

Los votantes (conjunto) solo pueden votar una vez

Los votos se almacenan en una tupla (inmutable una vez emitido)

Cada voto es una tupla: (id_votante, candidato, timestamp)

Implementa función para detectar votos duplicados

"""

# ====== SISTEMA INTERACTIVO SIN FUNCIONES ======

# Estructuras iniciales

votantes_registrados = set()
votos_totales = ()
candidatos_disponibles = ["Candidato A ","Candidato B " , "Candidato C " ]

print("=== SISTEMA DE VOTACIÓN INTERACTIVO ===")
print("Instrucciones:")
print("- Ingresa tu ID y candidato")
print("- Escribe 'FIN' en el ID para terminar")
print("- Solo puedes votar una vez\n")

votando = True 
numero_voto = 1

while votando:
    print(f"\n--- Voto #{numero_voto} ---")
    
    # Pedir ID del votante
    id_input = input("ID del votante: ")
    
   #verificar si quiere terminar

    if id_input.upper() == "FIN":
        print("Terminando...............")
        continue 

    #verificar que ya voto

    if id_input in votantes_registrados:

        print("el votante {id_input} ya voto , voto rechazado")
        continue

    # mostramos los candidatos disponibles 

    for i , cad in enumerate(candidatos_disponibles):
        
        print(f"los candidatos son {cad} ")


    
    # Pedir candidato
    try:
        opcion = int(input("Ingrese el candidato(1,2,3)"))

        if opcion < 1 or opcion > 3 :
            print("opcion invalidacion")
            continue
    except:
        print("debe ser un numero ")
        continue

    
    # obtenemos el candidato seleccionado 

    candidato_seleccionado = candidatos_disponibles[opcion - 1]
    
    # Crear el voto
    import datetime
    hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
    nuevo_voto = (id_input, candidato_seleccionado, hora_actual)
    
    # Registrar el voto
    
    votantes_registrados.add(id_input)
    votos_totales += nuevo_voto
    
    
    print(f"✅ Voto registrado: {id_input} → {candidato_seleccionado}")
    numero_voto += 1

# ====== MOSTRAR RESULTADOS ======
print("\n" + "="*50)
print("RESULTADOS FINALES DE LA VOTACIÓN")
print("="*50)

if len(votos_totales) == 0:
    print("No se registraron votos.")
else:
    # Inicializar conteo
    resultados = {"Candidato A": 0, "Candidato B": 0, "Candidato C": 0}
    
    # Contar votos
    for voto_individual in votos_totales:
        candidato = voto_individual[1]
        resultados[candidato] += 1
    
    # Mostrar resultados
    print("\n📊 RESULTADOS POR CANDIDATO:")
    for candidato, cantidad in resultados.items():
        print(f"   {candidato}: {cantidad} voto(s)")
    
    # Encontrar ganador
    max_votos = max(resultados.values())
    ganadores = [c for c, v in resultados.items() if v == max_votos]
    
    print(f"\n🏆 GANADOR(ES): {', '.join(ganadores)} con {max_votos} voto(s)")
    print(f"👥 TOTAL DE VOTANTES: {len(votos_totales)}")
    
    # Mostrar detalle de votos
    print("\n📝 DETALLE DE VOTOS:")
    print("-" * 40)
    for idx, voto in enumerate(votos_totales, 1):
        print(f"{idx}. ID: {voto[0]:10} | Candidato: {voto[1]:12} | Hora: {voto[2]}")

