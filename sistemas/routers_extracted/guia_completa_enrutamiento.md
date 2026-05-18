# GUÍA COMPLETA: ENRUTAMIENTO (ROUTING) - DOMINA CUALQUIER EJERCICIO

## ÍNDICE
1. [Conceptos Fundamentales](#1-conceptos-fundamentales)
2. [El Router y la Capa de Red](#2-el-router-y-la-capa-de-red)
3. [Direccionamiento IP y Máscaras de Subred](#3-direccionamiento-ip-y-máscaras-de-subred)
4. [Tablas de Enrutamiento](#4-tablas-de-enrutamiento)
5. [Tipos de Enrutamiento](#5-tipos-de-enrutamiento)
6. [Cómo Determinar si Dos Equipos se Pueden Comunicar](#6-cómo-determinar-si-dos-equipos-se-pueden-comunicar)
7. [Ejercicios Resueltos del PDF](#7-ejercicios-resueltos-del-pdf)
8. [Ejercicios Prácticos Adicionales](#8-ejercicios-prácticos-adicionales)
9. [Comandos de Diagnóstico](#9-comandos-de-diagnóstico)

---

## 1. CONCEPTOS FUNDAMENTALES

### ¿Qué es un Router?
Un **router** (enrutador, encaminador o ruteador) es un dispositivo de hardware que opera en la **Capa 3 (Capa de Red)** del modelo OSI. Su función principal es **interconectar redes** y **seleccionar la mejor ruta** para que los paquetes de datos lleguen de origen a destino.

**Componentes de un router:**
- CPU, memoria RAM, bus de sistema, interfaces de entrada/salida
- Almacena la **tabla de enrutamiento** en RAM

### ¿Qué es el Enrutamiento?
El enrutamiento es el proceso de **seleccionar el camino** que debe tomar un paquete IP para llegar desde el equipo origen hasta el equipo destino.

**Analogía:**
- **Ruta conectada**: Caminar a casa del vecino (está en tu misma calle/red)
- **Ruta estática**: Un tren que siempre usa las mismas vías (ruta fija)
- **Ruta dinámica**: Conducir un coche eligiendo ruta según tráfico/clima (se adapta)

---

## 2. EL ROUTER Y LA CAPA DE RED

### Modelo OSI - Capa de Red (Capa 3)
```
Host Origen          Router          Host Destino
Aplicación          Aplicación
Presentación        Presentación
Transporte          Transporte
Red ──────────▶    Red ──────────▶    Red
Enlace Datos        Enlace Datos      Enlace Datos
Física              Física            Física
```

**Funciones de la Capa de Red:**
1. Direccionamiento lógico (IP)
2. Determinación de la ruta
3. Reenvío de paquetes

**Funciones del Router al recibir un paquete:**
1. **Aceptar** paquetes por las líneas de entrada
2. **Lookup**: Buscar dirección destino en tabla de reenvío → identificar puerto salida
3. **Header Processing**: Manipular cabecera IP (decrementar TTL, recalcular checksum)
4. **Switching**: Enviar paquete al puerto de destino
5. **Buffering**: Almacenar en cola si necesario
6. **Transmitir** por línea de salida

---

## 3. DIRECCIONAMIENTO IP Y MÁSCARAS DE SUBRED

### Dirección IP
Una IP tiene 32 bits, escrita como 4 octetos (ej: 192.168.1.1)

### Máscara de Subred
Define qué parte de la IP es la **red** y qué parte es el **host**.

| Máscara | CIDR | Bits Red | Bits Host | Hosts por subred |
|---------|------|----------|-----------|------------------|
| 255.0.0.0 | /8 | 8 | 24 | 16,777,214 |
| 255.255.0.0 | /16 | 16 | 16 | 65,534 |
| 255.255.255.0 | /24 | 24 | 8 | 254 |
| 255.255.255.128 | /25 | 25 | 7 | 126 |
| 255.255.255.192 | /26 | 26 | 6 | 62 |
| 255.255.255.224 | /27 | 27 | 5 | 30 |

### Operación AND (Cómo saber a qué red pertenece una IP)
```
IP:       192.168.1.100  → 11000000.10101000.00000001.01100100
Máscara:  255.255.255.0  → 11111111.11111111.11111111.00000000
                     AND → 11000000.10101000.00000001.00000000 = 192.168.1.0
```

**La red es 192.168.1.0/24**

### Ejemplos de cálculo de red:
```
Ejemplo 1: 172.30.3.5 con máscara 255.255.255.0
IP:      172.30.3.5
Máscara: 255.255.255.0
Red:     172.30.3.0/24

Ejemplo 2: 10.1.1.1 con máscara 255.0.0.0
IP:      10.1.1.1
Máscara: 255.0.0.0
Red:     10.0.0.0/8

Ejemplo 3: 212.1.0.2 con máscara 255.255.255.0
IP:      212.1.0.2
Máscara: 255.255.255.0
Red:     212.1.0.0/24
```

---

## 4. TABLAS DE ENRUTAMIENTO

### Estructura de una Tabla de Enrutamiento
Una tabla de enrutamiento contiene:

| Destino | Máscara | Siguiente Nodo (Gateway) | Interfaz |
|---------|---------|--------------------------|----------|

**Ejemplo real del PDF:**
```
Destino:     212.1.1.0
Máscara:     255.255.255.128
Gateway:     0.0.0.0 (conectada directamente)
Interfaz:    If0
```

### Ruta por Defecto
Se usa cuando no hay una ruta específica. Destino y máscara son `0.0.0.0`.

```
Destino:  0.0.0.0
Máscara:  0.0.0.0
Gateway:  212.1.2.129
```

---

## 5. TIPOS DE ENRUTAMIENTO

### 5.1 Rutas Conectadas Directamente
Las redes que están **físicamente conectadas** al router. No requieren configuración manual.

### 5.2 Enrutamiento Estático
Rutas creadas **manualmente** por el administrador.

**Ventajas:** Seguro, predecible, poco uso de CPU
**Desventajas:** No se adapta a cambios, requiere mantenimiento manual

**Configuración en Cisco (ejemplo del PDF):**
```
Router> enable
Router# configure terminal
Router(config)# ip route 192.168.2.0 255.255.255.0 192.168.1.1
```

### 5.3 Enrutamiento Dinámico
Los routers intercambian información automáticamente usando **protocolos de enrutamiento**.

**Protocolos comunes:**
- **RIP**: Para redes pequeñas
- **OSPF**: Para redes empresariales
- **BGP**: Para Internet

### 5.4 Ruta Estática por Defecto
```
ip route 0.0.0.0 0.0.0.0 [gateway]
```
Útil para conexiones a Internet.

---

## 6. CÓMO DETERMINAR SI DOS EQUIPOS SE PUEDEN COMUNICAR

### Paso 1: Verificar si están en la misma subred
Aplicar AND entre IP y máscara de ambos equipos.

```
Equipo A: 192.168.1.10/24
Equipo B: 192.168.1.20/24

A: 192.168.1.10 AND 255.255.255.0 = 192.168.1.0
B: 192.168.1.20 AND 255.255.255.0 = 192.168.1.0

¡MISMA RED! → Se comunican directamente (vía switch)
```

### Paso 2: Si están en redes diferentes, verificar rutas
Debe existir una ruta **en ambos sentidos**:
- A → B (ruta de ida)
- B → A (ruta de vuelta)

### Paso 3: Verificar tablas de enrutamiento
El router debe tener una entrada para la red destino.

---

## 7. EJERCICIOS RESUELTOS DEL PDF

### EJERCICIO 1: ¿Cuántas redes hay aquí?
```
192.168.1.0/24    (LAN 1)
192.168.2.0/24    (LAN 2)
192.168.3.0/24    (LAN 3)
```
**Respuesta:** 3 redes diferentes, conectadas por el router R1.

### EJERCICIO 2: Máquinas que pueden comunicarse (Switches y Router)
**Topología:**
```
A1 (212.1.0.2) ─┐
A3 (212.1.0.3) ─┼── Switch A ── Router R ── Switch B ──┬── B1 (133.3.0.2)
B2 (212.1.0.4) ─┘                                        └── A2 (133.3.0.3)
```

**Pregunta a):** ¿Qué máquinas pueden intercambiar tráfico sin modificar nada?

**Solución:**
1. Calcular redes:
   - A1: 212.1.0.2 AND 255.255.255.0 = **212.1.0.0/24**
   - A3: 212.1.0.3 AND 255.255.255.0 = **212.1.0.0/24** ✓ Misma red
   - B2: 212.1.0.4 AND 255.255.255.0 = **212.1.0.0/24** ✓ Misma red
   - A2: 133.3.0.3 AND 255.255.255.0 = **133.3.0.0/24**
   - B1: 133.3.0.2 AND 255.255.255.0 = **133.3.0.0/24** ✓ Misma red

**Respuesta a):** 
- A1, A3 y B2 pueden comunicarse (red 212.1.0.0/24)
- A2 y B1 pueden comunicarse (red 133.3.0.0/24)

**Pregunta b):** ¿Qué cambios para que TODAS se comuniquen?

**Solución b):**
1. Configurar interfaces del router R:
   - If0: 212.1.0.1 (conectado a Switch A)
   - If1: 133.3.0.1 (conectado a Switch B)

2. Rutas en R:
```
Destino:     212.1.0.0
Máscara:     255.255.255.0
Interfaz:    If0

Destino:     133.3.0.0
Máscara:     255.255.255.0
Interfaz:    If1
```

3. Gateway por defecto en cada máquina:
   - A1, A3, B2: gateway = 212.1.0.1
   - A2, B1: gateway = 133.3.0.1

### EJERCICIO 3: Verificar comunicación A1 ↔ A2 (Red con 6 routers)
**Topología del PDF:**
- R1 conecta a A1 (red 212.1.1.0/25)
- R2, R3, R4, R5, R6 interconectados
- A2 está en red 212.1.3.0/24

**Verificación A1 → A2:**
```
A1 → R1 → R2 → ??? (R2 no tiene ruta a 212.1.3.0)
```
**Solución:** Añadir en R2:
```
Destino: 212.1.3.0
Máscara: 255.255.255.0
Gateway: 212.1.2.67 (hacia R5)
```

**Verificación A2 → A1:**
```
A2 → R5 → R2 → R1 → A1 ✓ (ya hay ruta)
```

---

## 8. EJERCICIOS PRÁCTICOS ADICIONALES

### EJERCICIO 1: Subnetting Básico
**Enunciado:** Tienes la red 192.168.1.0/24 y necesitas crear 4 subredes.
¿Cuál es la nueva máscara y los rangos?

**Solución:**
1. Necesitas 4 subredes → 2² = 4 → tomar 2 bits de host
2. Nueva máscara: /26 (255.255.255.192)

**Subredes:**
| Subred | Rango | Broadcast |
|--------|-------|-----------|
| 192.168.1.0/26 | .1 - .62 | .63 |
| 192.168.1.64/26 | .65 - .126 | .127 |
| 192.168.1.128/26 | .129 - .190 | .191 |
| 192.168.1.192/26 | .193 - .254 | .255 |

### EJERCICIO 2: Configuración de Rutas Estáticas
**Topología:**
```
PC1 (192.168.1.10/24) ── R1 ── R2 ── PC2 (192.168.2.10/24)
     192.168.1.1           192.168.3.1/24
                            192.168.3.2/24      192.168.2.1
```

**Configurar rutas estáticas:**

En R1:
```
ip route 192.168.2.0 255.255.255.0 192.168.3.2
```

En R2:
```
ip route 192.168.1.0 255.255.255.0 192.168.3.1
```

En PC1 (gateway):
```
gateway: 192.168.1.1
```

En PC2 (gateway):
```
gateway: 192.168.2.1
```

### EJERCICIO 3: ¿Pueden comunicarse?
**Datos:**
- Host A: 10.1.1.10/24
- Host B: 10.1.2.10/24

**Solución:**
```
A: 10.1.1.10 AND 255.255.255.0 = 10.1.1.0/24
B: 10.1.2.10 AND 255.255.255.0 = 10.1.2.0/24
```
**Diferentes redes** → Necesitan router con rutas en ambos sentidos.

### EJERCICIO 4: Ruta por Defecto
**Escenario:** Una empresa conecta a Internet.
- Red interna: 172.16.0.0/16
- Router interno: 172.16.1.1
- Router ISP (salida): 200.1.1.1

**Configuración en router interno:**
```
ip route 0.0.0.0 0.0.0.0 200.1.1.1
```

### EJERCICIO 5: Análisis de Tabla de Enrutamiento
**Tabla dada:**
```
Destino:     192.168.1.0    Máscara: 255.255.255.0    Gateway: 0.0.0.0
Destino:     192.168.2.0    Máscara: 255.255.255.0    Gateway: 192.168.1.2
Destino:     0.0.0.0        Máscara: 0.0.0.0          Gateway: 192.168.2.1
```

**Pregunta:** ¿Qué pasa con un paquete a 8.8.8.8?

**Solución:**
1. Buscar coincidencia exacta: no hay 8.8.8.0/24
2. Buscar ruta por defecto: **SÍ**, 0.0.0.0/0
3. El paquete va a gateway 192.168.2.1

---

## 9. COMANDOS DE DIAGNÓSTICO

### PING
Envía paquetes ICMP para probar conectividad.

**Respuestas:**
- `!` → Respuesta exitosa
- `.` → Esperando respuesta
- `U` → Destino inalcanzable
- `C` → Congestión
- `&` → TTL excedido

**Uso:**
```
Router> ping 192.168.1.1
```

### TRACE (Traceroute)
Muestra **cada salto** en el camino al destino.

**Respuestas:**
- `!H` → Host recibió pero no envió
- `P` → Protocolo inalcanzable
- `N` → Red inalcanzable
- `U` → Puerto inalcanzable

**Uso:**
```
Router# trace 172.16.33.5
```

### Interpretación de un Trace:
```
1 LONDON (172.16.12.3) 1 msec
2 PARIS  (172.16.16.2) 8 msec
3 ROME   (172.16.35.5) 5 msec
```
Significa: Origen → Londres → París → Roma

---

## RESUMEN: PASOS PARA RESOLVER CUALQUIER EJERCICIO DE ENRUTAMIENTO

1. **Identificar todas las IPs y máscaras** de la topología
2. **Calcular las redes** (operación AND) para cada equipo
3. **Dibujar la topología** si no está dibujada
4. **Verificar comunicación directa**: ¿Misma red? → Switch/Hub
5. **Si redes diferentes**: Verificar que hay router entre ellas
6. **Revisar tablas de enrutamiento**: ¿Hay ruta al destino?
7. **Verificar bidireccionalidad**: ¿Hay ruta de ida Y vuelta?
8. **Si falta ruta**: Añadir ruta estática o configurar protocolo dinámico
9. **Verificar gateways**: Las máquinas deben apuntar al router correcto
10. **Probar con ping/trace** para validar

---

## FÓRMULAS RÁPIDAS

**Número de hosts por subred:** 2^(32-máscara_CIDR) - 2
- /24: 2^8 - 2 = 254 hosts
- /26: 2^6 - 2 = 62 hosts

**Número de subredes:** 2^(bits_tomados_de_host)
- /24 a /26: 2^2 = 4 subredes

**Cálculo de salto (incremento):**
- /26: salto de 64 (256 - 192 = 64)
- /25: salto de 128
- /27: salto de 32
