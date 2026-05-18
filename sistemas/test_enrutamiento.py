#!/usr/bin/env python3
"""
TEST INTERACTIVO DE ENRUTAMIENTO
Ejercicios de routing con repetición hasta acertar todos
"""

def mostrar_enunciado(num, titulo, topologia, enunciado, opciones, correcta):
    print("\n" + "="*60)
    print(f"EJERCICIO {num}: {titulo}")
    print("="*60)
    print("\nTOPOLOGÍA:")
    print(topologia)
    print("\nENUNCIADO:")
    print(enunciado)
    print("\nOPCIONES:")
    letras = ['A', 'B', 'C', 'D']
    for i, op in enumerate(opciones):
        print(f"  {letras[i]}. {op}")
    return letras[correcta]

def evaluar(respuesta, correcta, num, titulo):
    if respuesta.upper() == correcta:
        print(f"\n✅ ¡CORRECTO! Ejercicio {num} ({titulo}) bien resuelto.")
        return True
    else:
        print(f"\n❌ INCORRECTO. La respuesta correcta era: {correcta}")
        return False

def main():
    print("\n" + "="*60)
    print("   TEST INTERACTIVO DE ENRUTAMIENTO")
    print("="*60)
    print("\nResponde con A, B, C o D según corresponda.")
    print("Debes acertar TODOS los ejercicios para terminar.")
    print("Los fallados se repetirán hasta que los aciertes.\n")
    
    # BASE DE DATOS DE EJERCICIOS (SOLO ENRUTAMIENTO)
    # Primero definimos todos los ejercicios en el orden original
    ejercicios_original = [
        {  # ANTIGUO 1
            "titulo": "Comunicación básica",
            "topo": """
    PC1 (192.168.1.10/24) ── SW1 ── R1 ── R2 ── SW2 ── PC2 (192.168.2.10/24)
                              192.168.1.1    192.168.2.1
            """,
            "enun": "¿Pueden PC1 y PC2 comunicarse directamente sin configurar nada adicional?",
            "opc": [
                "Sí, porque están en la misma red lógica",
                "No, porque están en redes diferentes (/24) y no hay ruta configurada",
                "Sí, porque el switch se encarga de enrutar",
                "No, porque las máscaras son diferentes"
            ],
            "corr": 1  # B
        },
        {  # ANTIGUO 2
            "titulo": "Ruta por defecto",
            "topo": """
    R1 tiene configuradas estas rutas:
    Destino:     192.168.2.0    Máscara: 255.255.255.0    Gateway: 192.168.1.2
    Destino:     0.0.0.0        Máscara: 0.0.0.0          Gateway: 192.168.1.1
    
    Llega un paquete con destino: 8.8.8.8
            """,
            "enun": "¿Por qué ruta se enviará el paquete?",
            "opc": [
                "Por la ruta a 192.168.2.0 vía 192.168.1.2",
                "Se descarta porque no hay ruta específica",
                "Por la ruta por defecto (0.0.0.0) vía 192.168.1.1",
                "El paquete se queda en el buffer esperando una nueva ruta"
            ],
            "corr": 2  # C
        },
        {  # ANTIGUO 3
            "titulo": "Operación AND y comunicación",
            "topo": """
    Host A: IP=10.1.1.10, Máscara=255.0.0.0 (Clase A)
    Host B: IP=10.1.2.10, Máscara=255.255.255.0 (/24)
            """,
            "enun": "Calcula la red de cada host con AND. ¿Pueden comunicarse directamente?",
            "opc": [
                "Sí, A está en 10.0.0.0 y B en 10.1.2.0, misma red Clase A",
                "No, A está en 10.0.0.0/8 y B en 10.1.2.0/24, redes diferentes",
                "Sí, porque ambos empiezan por 10",
                "No, porque 10.1.1.10 y 10.1.2.10 son redes diferentes"
            ],
            "corr": 1  # B
        },
        {  # ANTIGUO 4
            "titulo": "Configuración de ruta estática",
            "topo": """
    R1 (192.168.1.1) ─── 192.168.3.0/24 ─── R2 (192.168.3.2) ─── PC2 (192.168.2.10/24)
    PC1 (192.168.1.10/24)                                    PC2 gateway: 192.168.2.1
    PC1 gateway: 192.168.1.1
            """,
            "enun": "¿Qué ruta estática debes configurar en R1 para que PC1 llegue a PC2?",
            "opc": [
                "ip route 192.168.2.0 255.255.255.0 192.168.1.1",
                "ip route 192.168.2.0 255.255.255.0 192.168.3.2",
                "ip route 192.168.1.0 255.255.255.0 192.168.3.2",
                "ip route 0.0.0.0 0.0.0.0 192.168.3.2"
            ],
            "corr": 1  # B
        },
        {  # ANTIGUO 5
            "titulo": "Interpretar Traceroute",
            "topo": """
    Resultado del comando: Router# trace 172.16.33.5
    1 LONDON (172.16.12.3) 1 msec
    2 PARIS  (172.16.16.2) 8 msec
    3 ROME   (172.16.35.5) 5 msec
            """,
            "enun": "¿Cuántos 'saltos' (routers) hay entre el origen y el destino final?",
            "opc": [
                "1 salto (solo Londres)",
                "2 saltos (Londres y París)",
                "3 saltos (Londres, París y Roma)",
                "0 saltos, es conexión directa"
            ],
            "corr": 2  # C
        },
        {  # ANTIGUO 6
            "titulo": "Comunicación en mismo switch",
            "topo": """
    SwA conecta a: A1(212.1.0.2), A3(212.1.0.3), B2(212.1.0.4)
    SwB conecta a: A2(133.3.0.3), B1(133.3.0.2)
    Máscara todas: 255.255.255.0
            """,
            "enun": "¿Qué máquinas pueden comunicarse SIN configurar nada adicional?",
            "opc": [
                "Todas se comunican porque el switch conecta todo",
                "A1, A3, B2 entre sí; A2 y B1 entre sí",
                "Solo A1 con A3; el resto no puede",
                "Ninguna, necesitan router obligatoriamente"
            ],
            "corr": 1  # B
        },
        {  # ANTIGUO 7
            "titulo": "Rutas bidireccionales",
            "topo": """
    Router R1 tiene:
    - Interfaz f0/0: 192.168.1.1/24 (conecta a PC1)
    - Interfaz f0/1: 192.168.3.1/24 (enlace a R2)
    
    Router R2 tiene:
    - Interfaz f0/0: 192.168.3.2/24 (enlace a R1)
    - Interfaz f0/1: 192.168.2.1/24 (conecta a PC2)
    
    PC1: 192.168.1.10/24, gateway 192.168.1.1
    PC2: 192.168.2.10/24, gateway 192.168.2.1
            """,
            "enun": "Para que PC1 haga ping a PC2, ¿qué rutas estáticas mínimas debes configurar?",
            "opc": [
                "En R1: ip route 192.168.2.0 255.255.255.0 192.168.3.2 | En R2: ya sabe su red 192.168.2.0",
                "En R1: ip route 192.168.2.0 255.255.255.0 192.168.3.2 | En R2: ip route 192.168.1.0 255.255.255.0 192.168.3.1",
                "Solo en R1: ip route 0.0.0.0 0.0.0.0 192.168.3.2",
                "No hace falta nada, las redes están conectadas directamente a cada router"
            ],
            "corr": 1  # B
        },
        {  # NUEVO 8
            "titulo": "Verificación de ruta de ida y vuelta",
            "topo": """
    Tabla de R1:
    Destino: 192.168.2.0  Máscara: 255.255.255.0  Gateway: 192.168.1.2
    
    Tabla de R2:
    Destino: 192.168.1.0  Máscara: 255.255.255.0  Gateway: 192.168.1.1
    
    PC1 (192.168.1.10) quiere comunicarse con PC2 (192.168.2.10)
            """,
            "enun": "¿Es posible la comunicación bidireccional?",
            "opc": [
                "Sí, hay ruta de ida en R1 y de vuelta en R2",
                "No, solo hay ruta de ida pero no de vuelta",
                "No, R1 no sabe llegar a 192.168.2.0",
                "Sí, porque están en la misma red"
            ],
            "corr": 0  # A
        },
        {  # NUEVO 9
            "titulo": "Rutas más específicas (Longest Prefix Match)",
            "topo": """
    R2 tiene esta tabla de enrutamiento:
    Destino: 10.0.0.0    Máscara: 255.0.0.0 (/8)      Gateway: R3
    Destino: 10.1.0.0    Máscara: 255.255.0.0 (/16)    Gateway: R4
    Destino: 10.1.1.0    Máscara: 255.255.255.0 (/24)  Gateway: R5
    Destino: 0.0.0.0     Máscara: 0.0.0.0 (/0)         Gateway: R6
    
    Llega un paquete con destino: 10.1.1.1
            """,
            "enun": "¿Por qué ruta se enviará el paquete y por qué?",
            "opc": [
                "Por R3 (10.0.0.0/8) porque es la primera en la tabla",
                "Por R6 (0.0.0.0/0) porque es la ruta por defecto",
                "Por R5 (10.1.1.0/24) porque es la coincidencia más específica (longest prefix match)",
                "Por R4 (10.1.0.0/16) porque tiene máscara media"
            ],
            "corr": 2  # C
        },
        {  # NUEVO 10
            "titulo": "Ping y respuestas ICMP",
            "topo": """
    Router> ping 192.168.1.1
    
    Respuestas recibidas:
    !!!!! (5 signos de exclamación)
            """,
            "enun": "¿Qué significa el resultado del ping?",
            "opc": [
                "Hubo 5 timeouts, no hay conectividad",
                "Se enviaron 5 paquetes y todos recibieron respuesta exitosa",
                "Hay congestión en la red, paquetes perdidos",
                "El destino es inalcanzable"
            ],
            "corr": 1  # B
        },
        {  # NUEVO 11
            "titulo": "Análisis de red destino",
            "topo": """
    R1 recibe un paquete con IP destino: 172.30.3.5
    
    Tabla de R1:
    Destino:     172.30.1.0    Máscara: 255.255.255.0    Gateway: 172.30.10.1
    Destino:     172.30.2.0    Máscara: 255.255.255.0    Gateway: 172.30.10.2
    Destino:     172.30.3.0    Máscara: 255.255.255.0    Gateway: 172.30.10.3
    Destino:     172.30.0.0    Máscara: 255.255.0.0      Gateway: 172.30.10.4
            """,
            "enun": "¿A qué gateway enviará R1 el paquete con destino 172.30.3.5?",
            "opc": [
                "172.30.10.1 (por la primera ruta)",
                "172.30.10.2 (por la segunda ruta)",
                "172.30.10.3 (coincide exactamente con 172.30.3.0/24)",
                "172.30.10.4 (por la ruta resumida /16)"
            ],
            "corr": 2  # C
        },
        {  # NUEVO 12
            "titulo": "Configuración de gateway en hosts",
            "topo": """
    PC1 (192.168.1.10/24)
     |
    R1 (192.168.1.1) ─── R2 ─── PC2 (192.168.2.10/24)
    
    Queremos que PC1 llegue a PC2.
            """,
            "enun": "¿Cuál debe ser la configuración del gateway en PC1?",
            "opc": [
                "192.168.1.10 (su propia IP)",
                "192.168.2.10 (la IP de PC2)",
                "192.168.1.1 (la IP de R1 en su misma red)",
                "192.168.2.1 (la IP de R2 en la red destino)"
            ],
            "corr": 2  # C
        },
        {  # NUEVO 13
            "titulo": "TTL (Time To Live) en routers",
            "topo": """
    Host A ── R1 ── R2 ── R3 ── R4 ── Host B
    
    Paquete enviado desde A con TTL=3
            """,
            "enun": "¿Llegará el paquete a B? ¿Qué sucede con el TTL?",
            "opc": [
                "Sí, llega. TTL se reduce a 2, 1, 0 (llegada)",
                "No, el TTL llega a 0 en R3 y el paquete se descarta",
                "Sí, llega. El TTL no se modifica en los routers",
                "No, el TTL llega a 0 en R4 y da error de destino inalcanzable"
            ],
            "corr": 1  # B (TTL=3: R1=2, R2=1, R3=0 → descarta)
        },
        {  # NUEVO 14
            "titulo": "Rutas conectadas vs estáticas",
            "topo": """
    R1 tiene interfaces:
    - f0/0: 192.168.1.1/24
    - f0/1: 192.168.3.1/24
    
    R2 tiene interfaces:
    - f0/0: 192.168.3.2/24
    - f0/1: 192.168.2.1/24
            """,
            "enun": "¿Qué rutas tiene R1 AUTOMÁTICAMENTE sin configurar nada?",
            "opc": [
                "192.168.1.0/24 y 192.168.3.0/24 (rutas conectadas)",
                "Solo 192.168.1.0/24, la otra hay que configurarla",
                "Ninguna, todas son rutas estáticas",
                "192.168.2.0/24 porque R2 la propaga automáticamente"
            ],
            "corr": 0  # A
        },
        {  # NUEVO 15
            "titulo": "Respuesta de Traceroute",
            "topo": """
    Router# trace 212.1.1.5
    1 192.168.1.2 !H
    2 192.168.2.2 P
            """,
            "enun": "¿Qué significan las respuestas !H y P en el traceroute?",
            "opc": [
                "!H = Host alcanzado, P = Protocolo correcto",
                "!H = Router recibió pero no envió, P = Protocolo inalcanzable",
                "!H = Error de hardware, P = Puerto abierto",
                "!H = Host desconocido, P = Paquete perdido"
            ],
            "corr": 1  # B
        },
    ]
    
    # REORDENAR: NUEVOS (índices 7-14) PRIMERO, LUEGO ANTIGUOS (0-6)
    nuevos = ejercicios_original[7:]   # Nuevos ejercicios (índices 7 a 14)
    antiguos = ejercicios_original[:7]  # Antiguos ejercicios (índices 0 a 6)
    ejercicios = nuevos + antiguos
    
    # RENUMERAR EJERCICIOS SECUENCIALMENTE (1-15)
    for i, ej in enumerate(ejercicios, start=1):
        ej["num"] = i
    
    # Lista de ejercicios fallados (índices)
    fallados = list(range(len(ejercicios)))  # Empezamos con todos
    total_intentos = 0
    
    while fallados:
        print("\n" + "="*60)
        print(f"   EJERCICIOS PENDIENTES: {len(fallados)}")
        print("="*60)
        
        nuevos_fallados = []
        
        for idx in fallados:
            ej = ejercicios[idx]
            correcta = mostrar_enunciado(ej["num"], ej["titulo"], ej["topo"], ej["enun"], ej["opc"], ej["corr"])
            
            while True:
                r = input("\nTu respuesta (A/B/C/D) o 'salir': ")
                if r.lower() == 'salir':
                    print("\n👋 ¡Hasta luego! Vuelve para completar el test.")
                    return
                
                if r.upper() in ['A', 'B', 'C', 'D']:
                    break
                print("❌ Respuesta inválida. Usa A, B, C o D.")
            
            total_intentos += 1
            
            if evaluar(r, correcta, ej["num"], ej["titulo"]):
                pass  # Acertó, no se añade a fallados
            else:
                nuevos_fallados.append(idx)
                print(f"   ↻ Este ejercicio se repetirá más tarde.")
        
        fallados = nuevos_fallados
        
        if fallados:
            print("\n" + "-"*60)
            print(f"   Te quedan {len(fallados)} ejercicios por acertar.")
            print("   Vamos a repetirlos...\n")
        else:
            print("\n" + "="*60)
            print(f"   ¡FELICIDADES! Has acertado TODOS los ejercicios")
            print(f"   Total de intentos: {total_intentos}")
            print("="*60)
            print("\n🎉 ¡Dominas el enrutamiento perfectamente!\n")

if __name__ == "__main__":
    main()
