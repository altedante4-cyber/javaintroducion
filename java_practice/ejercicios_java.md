# Ejercicios de Programación Java - Nivel Medio-Alto

Introducción: Esta colección presenta 20 ejercicios diseñados para consolidar conocimientos de programación orientada a objetos en Java. Los ejercicios cubren estructuras de datos, patrones de diseño, herencia, polimorfismo y conceptos avanzados en contextos variados y creativos.

---

## 1. Sistema de Magia Arcana

**Contexto:** En un reino fantástico, los magos utilizan runas para lanzar hechizos. Cada runa tiene un nombre, un nivel de poder (1-100) y un elemento (FUEGO, AGUA, TIERRA, AIRE, LUZ, OSCURIDAD).

**Descripción:** Implementa un sistema donde los magos pueden crear grimorios (colecciones de runas). El sistema debe permitir:
- Añadir runas al grimorio (sin duplicados por nombre)
- Buscar runas por elemento y devolver todas las que coincidan
- Calcular el poder total de un grimorio
- Encontrar la runa más poderosa de un elemento específico

**Requisitos técnicos:** HashSet, ArrayList, sobrescritura de equals() y hashCode().

**Clases a implementar:**
- `enum Elemento` - constantes: FUEGO, AGUA, TIERRA, AIRE, LUZ, OSCURIDAD
- `class Runa` - atributos: nombre (String), poder (int 1-100), elemento (Elemento); métodos: getters, setters, equals(), hashCode()
- `class Grimorio` - atributos: nombre (String), runes (HashSet<Runa>); métodos: añadirRuna(Runa), buscarPorElemento(Elemento): ArrayList<Runa>, getPoderTotal(): int, getRunaMasPoderosa(Elemento): Runa
- `class Main` -演示 del sistema

---

## 2. Simulación de Ecosistema Marino

**Contexto:** Un biólogo necesita simular una cadena alimentaria marina con tres tipos de entidades: Pez, Tiburón y Plancton. Los tiburones come

n plancton, y todos tienen energía que disminuye con el tiempo.

**Descripción:** Implementa un sistema de simulación donde:
- Cada entidad tiene posición (x, y), energía y velocidad de movimiento
- Los tiburones se mueven hacia el pez más cercano dentro de su rango de visión
- Los peces huyen del tiburón más cercano si está dentro de su rango de detección
- Cuando una entidad come, gana energía; cuando su energía llega a 0, muere
- La simulación avanza en turnos, mostrando el estado de todas las entidades vivas

**Requisitos técnicos:** Herencia, Polimorfismo, ArrayList, Arrays bidimensionales para el mapa.

**Clases a implementar:**
- `abstract class Entidad` - atributos: x, y (double), energia (int), velocidad (double), vivo (boolean); métodos: mover(double dx, double dy), comer(int energia), estaViva(): boolean, distancia(Entidad e): double
- `class Tiburon extends Entidad` - atributos: rangoVision (int); métodos: buscarPez(ArrayList<Pez>): Pez, hunt(ArrayList<Pez>)
- `class Pez extends Entidad` - atributos: rangoDeteccion (int); métodos: buscarTiburon(ArrayList<Tiburon>): Tiburon, flee(ArrayList<Tiburon>)
- `class Plancton extends Entidad` - métodos: reproduce(): Plancton
- `class Ecosistema` - atributos: tiburones (ArrayList<Tiburon>), peces (ArrayList<Pez>), plancton (ArrayList<Plancton>), mapa[20][20]; métodos: simularTurno(), estadoActual(): String
- `class Main` - menú interactivo de simulación

---

## 3. Gestor de Inventario de Videojuego RPG

**Contexto:** Un jugador tiene un inventario con diferentes tipos de items: armas, armaduras, pociones y materiales. Cada item tiene valor, peso y rarity (común, raro, épico, legendario).

**Descripción:** Crea un sistema donde:
- El inventario tiene una capacidad máxima de peso (ej: 100 unidades)
- Los items se organizan automáticamente por rarity (usando HashMap<String, ArrayList<Item>>)
- Se puede buscar el item de mayor valor dentro de una rarity específica
- Al equipar un arma, esta se mueve de "inventario" a "equipado" (solo una arma y una armadura equippeda a la vez)
- El sistema calcula el daño total del personaje (base + daño del arma) y la defensa total

**Requisitos técnicos:** HashMap, ArrayList, Herencia (Item como clase padre), Polimorfismo.

**Clases a implementar:**
- `enum Rarity` - constantes: COMUN, RARO, EPICO, LEGENDARIO
- `enum TipoItem` - constantes: ARMA, ARMADURA, POCION, MATERIAL
- `abstract class Item` - atributos: nombre (String), valor (int), peso (int), rarity (Rarity), tipo (TipoItem); métodos abstractos: getDescripcion(): String
- `class Arma extends Item` - atributos: daño (int), equipada (boolean); métodos: getDescripcion(), equipar(), desequipar()
- `class Armadura extends Item` - atributos: defensa (int), equipada (boolean); métodos: getDescripcion(), equipar(), desequipar()
- `class Pocion extends Item` - atributos: efecto (String), cantidad (int); métodos: getDescripcion(), usar()
- `class Material extends Item` - atributos: cantidad (int); métodos: getDescripcion()
- `class Inventario` - atributos: items (HashMap<Rarity, ArrayList<Item>>), capacidadMax (int), armaEquipada (Arma), armaduraEquipada (Armadura); métodos: añadirItem(Item): boolean, eliminarItem(Item): boolean, getItemMayorValor(Rarity): Item, equiparArma(Arma), equiparArmadura(Armadura), getPesoActual(): int, getDañoTotal(int dañoBase): int, getDefensaTotal(): int
- `class Personaje` - atributos: nombre (String), nivel (int), dañoBase (int), inventario (Inventario); métodos: mostrarStats()
- `class Main` -演示 del sistema

---

## 4. Protocolo de Comunicación interestelar

**Contexto:** Una nave espacial recibe mensajes codificados de diferentes civilizaciones alienígenas. Cada mensaje tiene un remitente identificado por una clave única, un contenido y un nivel de prioridad (1-5).

**Descripción:** Implementa un sistema que:
- Almacena mensajes en un HashMap donde la clave es el ID del remitente
- Permite agregar nuevos mensajes (sobrescribe si el remitente ya existe)
- Recupera todos los mensajes de prioridad >= 3 ordenados por prioridad descendente
- Elimina mensajes de remitentes que no han enviado nada en los últimos "X" turnos (simulado)
- Genera un reporte con: total de mensajes, promedio de prioridad, remitente con más mensajes

**Requisitos técnicos:** HashMap, ArrayList, Comparable/Comparator, Colecciones.

**Clases a implementar:**
- `class Mensaje` - atributos: id (String), contenido (String), prioridad (int 1-5), remitente (String), turnoRecibido (int); métodos: getters, setters, compareTo(Mensaje)
- `class Comunicador` - atributos: mensajes (HashMap<String, Mensaje>), ultimoTurnoActivo (HashMap<String, int>), contadorTurnos (int); métodos: recibirMensaje(Mensaje), getMensaje(String): Mensaje, getMensajesPrioridadAlta(): ArrayList<Mensaje>, limpiarInactivos(int turnosSinActividad): int, generarReporte(): String
- `class Main` -演示 del sistema

---

## 5. Motor de Física de Partículas

**Contexto:** Un científico necesita simular partículas en un espacio 2D donde cada partícula tiene posición, velocidad, masa y carga eléctrica.

**Descripción:** Crea un simulador donde:
- Las partículas se almacenan en un ArrayList
- En cada paso de simulación, se calculan las fuerzas entre todas las parejas de partículas (atracción/repulsión según carga)
- Se aplica la segunda ley de Newton para actualizar velocidades y posiciones
- Se puede "congelar" partículas (dejan de moverse pero siguen interactuando)
- El sistema permite obtener: partícula más rápida, partícula con mayor aceleración, energía cinética total del sistema

**Requisitos técnicos:** Clases abstractas, Herencia, ArrayList, sobrecarga de métodos.

**Clases a implementar:**
- `abstract class Particula` - atributos: id (String), x, y (double), vx, vy (double), masa (double), carga (double), congelada (boolean), ax, ay (double); métodos: calcularAceleracion(double fx, double fy), mover(double dt), getVelocidad(): double, getEnergiaCinetica(): double, congelar(), descongelar(), estaCongelada(): boolean
- `class Electrón extends Particula` - constructor: carga = -1.6e-19, masa = 9.11e-31
- `class Protón extends Particula` - constructor: carga = 1.6e-19, masa = 1.67e-27
- `class Neutrón extends Particula` - constructor: carga = 0, masa = 1.67e-27
- `class Fotón extends Particula` - constructor: masa = 0, carga = 0 (siempre se mueve a velocidad c)
- `class SimuladorFísica` - atributos: partículas (ArrayList<Particula>), constantes (const G, k); métodos: añadirParticula(Particula), simularPaso(double dt), calcularFuerzas(), getParticulaMasRapida(): Particula, getParticulaMayorAceleracion(): Particula, getEnergiaTotal(): double
- `class Main` -演示 del sistema

---

## 6. Sistema de Quests para MMORPG

**Contexto:** Un juego online tiene misiones con diferentes tipos: matar monstruos, recolectar objetos, proteger NPC, alcanzar ubicación. Cada quest tiene dificultad, experiencia recomendada y recompensas.

**Descripción:** Implementa un gestor de quests donde:
- Las quests se clasifican por tipo usando HashMap<String, ArrayList<Quest>>
- El jugador tiene un nivel y experiencia actual
- Solo puede tomar quests donde nivel_recomendado <= nivel_jugador + 2
- Al completar una quest, gana experiencia y objetos de recompensa
- El sistema recomienda quests basadas en el nivel actual del jugador
- Hay quests diarias (solo se pueden hacer una vez por día real) y normales

**Requisitos técnicos:** Herencia, HashMap, Interfaces (QuestDiurna interface), ArrayList.

**Clases a implementar:**
- `enum TipoQuest` - constantes: MATAR_MONSTRUOS, RECOLECTAR_OBJETOS, PROTEGER_NPC, ALCANZAR_UBICACION
- `enum Dificultad` - constantes: FACIL, MEDIA, DIFICIL, EXTREMA
- `class Recompensa` - atributos: experiencia (int), items (ArrayList<String>), oro (int); métodos: getters
- `interface QuestDiurna` - métodos: esValidaHoy(): boolean, completar()
- `abstract class Quest` - atributos: id (String), nombre (String), descripcion (String), tipo (TipoQuest), dificultad (Dificultad), nivelRecomendado (int), recompensa (Recompensa), completada (boolean); métodos abstractos: completar(): boolean
- `class QuestMatar extends Quest` - atributos: monstruo (String), cantidad (int), matados (int)
- `class QuestRecolectar extends Quest` - atributos: objeto (String), cantidad (int), recolectados (int)
- `class QuestProteger extends Quest` - atributos: npc (String), duración (int)
- `class QuestUbicacion extends Quest` - atributos: ubicacion (String)
- `class QuestDiaria extends Quest implements QuestDiurna` - atributos: ultimaFechaCompletada (LocalDate); métodos: esValidaHoy(), puedeCompletar(): boolean
- `class GestorQuests` - atributos: quests (HashMap<TipoQuest, ArrayList<Quest>>), questDiarias (ArrayList<QuestDiaria>); métodos: añadirQuest(Quest), getQuestsDisponibles(int nivelJugador): ArrayList<Quest>, completarQuest(Quest, Jugador): boolean
- `class Jugador` - atributos: nombre (String), nivel (int), experiencia (int), experienciaParaSigNivel (int); métodos: ganarExperiencia(int), subirNivel()
- `class Main` -演示 del sistema

---

## 7. Analizador Léxico de Código

**Contexto:** Un compilador simplificado necesita tokenizar código fuente. Los tokens pueden ser: PALABRA_RESERVADA, IDENTIFICADOR, NÚMERO, OPERADOR, DELIMITADOR.

**Descripción:** Crea un analizador que:
- Recibe una cadena con código fuente
- Identifica cada token y lo clasifica
- Almacena los tokens en un ArrayList de objetos Token
- Usa un HashMap para contar frecuencia de cada tipo de token
- Valida que los delimitadores (paréntesis, llaves) estén balanceados
- Genera una lista de errores si encuentra tokens inválidos

**Requisitos técnicos:** Clases abstractas (Token), Herencia para tipos concretos, HashMap, ArrayList.

**Clases a implementar:**
- `enum TipoToken` - constantes: PALABRA_RESERVADA, IDENTIFICADOR, NUMERO, OPERADOR, DELIMITADOR, CADENA, COMENTARIO, DESCONOCIDO
- `abstract class Token` - atributos: tipo (TipoToken), valor (String), posicion (int); métodos abstractos: getTipo(): TipoToken
- `class TokenReservado extends Token` - palabras: if, else, while, for, return, class, public, private, void, int, String, boolean
- `class TokenIdentificador extends Token`
- `class TokenNumero extends Token` - atributos: valorNumerico (double)
- `class TokenOperador extends Token` - operadores: +, -, *, /, =, ==, !=, <, >, <=, >=, &&, ||
- `class TokenDelimitador extends Token` - delimitadores: (, ), {, }, [, ], ;, ,
- `class TokenCadena extends Token`
- `class AnalizadorLexico` - atributos: código (String), tokens (ArrayList<Token>), frecuencia (HashMap<TipoToken, Integer>), errores (ArrayList<String>); métodos: tokenizar(), validarBalanceo(): boolean, getFrecuencias(): HashMap, getErrores(): ArrayList<String>
- `class Main` -演示 del sistema

---

## 8. Simulador de Tráfico Vehicular

**Contexto:** Una ciudad tiene intersecciones conectadas por calles. Los vehículos viajan de un punto a otro siguiendo rutas, pero pueden encontrar tráfico.

**Descripción:** Implementa una simulación donde:
- Las calles tienen capacidad máxima y flujo actual (vehículos presentes)
- Los vehículos tienen origen, destino y ruta (lista de calles a seguir)
- Cuando un vehículo intenta entrar a una calle llena, debe esperar
- Cada segundo, los vehículos avanzan una "unidad" de calle
- El sistema muestra: vehículos en tránsito, vehículos que llegaron a destino, vehículos esperando

**Requisitos técnicos:** Herencia (Vehículo como padre, coche, camión, moto como hijos), HashMap (mapa de calles), ArrayList, Polimorfismo.

**Clases a implementar:**
- `class Calle` - atributos: nombre (String), capacidad (int), vehiculosActuales (ArrayList<Vehiculo>), longitud (int); métodos: añadirVehiculo(Vehiculo): boolean, removeVehiculo(Vehiculo), getOcupacion(): int, estaLlena(): boolean
- `abstract class Vehiculo` - atributos: id (String), origen (String), destino (String), ruta (ArrayList<Calle>), posicionActual (int), velocidad (int), esperando (boolean), llegada (boolean); métodos abstractos: getTipo(): String, mover(), puedeAvanzar(): boolean
- `class Coche extends Vehiculo` - velocidad: 3, capacidad: 1
- `class Camión extends Vehiculo` - velocidad: 1, capacidad: 2
- `class Moto extends Vehiculo` - velocidad: 4, capacidad: 1
- `class Ciudad` - atributos: calles (HashMap<String, Calle>), vehiculos (ArrayList<Vehiculo>), vehiculosEsperando (ArrayList<Vehiculo>), vehiculosLlegados (ArrayList<Vehiculo>); métodos: añadirCalle(Calle), añadirVehiculo(Vehiculo), simularSegundo(), getEstado(): String
- `class Main` -演示 del sistema

---

## 9. Sistema de Mensajería Cifrada

**Contexto:** Una aplicación de mensajería usa diferentes algoritmos de cifrado según el nivel de seguridad requerido. Los métodos posibles: César, Vigenère, RSA simplificado.

**Descripción:** Crea un sistema donde:
- Cada mensaje tiene contenido, destinatario, nivel de seguridad
- Se usa un HashMap para almacenar los mensajes por destinatario
- El sistema aplica el cifrado correspondiente según el nivel:
  - Nivel 1: César (desplazamiento = nivel_usuario)
  - Nivel 2: Vigenère (clave = nombre_destinatario)
  - Nivel 3: Invertir cadena + César
- Se puede descifrar un mensaje si se conoce el nivel de seguridad
- Permite buscar mensajes de un destinatario específicos

**Requisitos técnicos:** Interfaces (Cifrador interface con métodos cifrar() y descifrar()), implementaciones concretas para cada algoritmo, HashMap.

**Clases a implementar:**
- `class Mensaje` - atributos: id (String), contenido (String), destinatario (String), nivelSeguridad (int), cifrado (boolean); métodos: getters, setters
- `interface Cifrador` - métodos: cifrar(String texto, String clave): String, descifrar(String texto, String clave): String
- `class CifradorCésar implements Cifrador` - atributos: desplazamiento (int); métodos: cifrar(), descifrar()
- `class CifradorVigenère implements Cifrador` - atributos: clave (String); métodos: cifrar(), descifrar()
- `class CifradorHíbrido implements Cifrador` - métodos: cifrar(), descifrar()
- `class GestorMensajes` - atributos: mensajes (HashMap<String, ArrayList<Mensaje>>), cifradores (HashMap<Integer, Cifrador>), nivelUsuario (int); métodos: enviarMensaje(Mensaje), recibirMensaje(String destinatario): ArrayList<Mensaje>, cifrarMensaje(Mensaje), descifrarMensaje(Mensaje)
- `class Main` -演示 del sistema

---

## 10. Juego de Estrategia por Turnos

**Contexto:** Dos jugadores controlan ejércitos en un tablero de dimensiones NxM. Cada unidad tiene stats: puntos de vida, daño, rango de movimiento, rango de ataque.

**Descripción:** Implementa un juego donde:
- El tablero se representa como un array bidimensional de celdas
- Cada jugador tiene un ArrayList de unidades
- En un turno, un jugador puede: mover unidades (hasta su rango), atacar (si hay enemigo en rango)
- Las unidades tienen tipos: Guerrero (alto daño, bajo HP), Arquero (rango alto), Tanque (alto HP, bajo movimiento)
- Gana el jugador que elimina todas las unidades del oponente
- El sistema registra el historial de acciones del juego

**Requisitos técnicos:** Herencia (Unidad clase padre), Polimorfismo, ArrayList, Arrays bidimensionales.

**Clases a implementar:**
- `enum TipoUnidad` - constantes: GUERRERO, ARQUERO, TANQUE
- `enum TipoCelda` - constantes: VACIA, OBSTACULO, POSICION_J1, POSICION_J2
- `class Celda` - atributos: tipo (TipoCelda), contenido (Unidad), posicionX (int), posicionY (int)
- `abstract class Unidad` - atributos: nombre (String), tipo (TipoUnidad), hp (int), hpMax (int), daño (int), rangoMovimiento (int), rangoAtaque (int), jugador (int), posicionX (int), posicionY (int), haAccionado (boolean); métodos abstractos: getStats(): String; métodos: mover(int x, int y), atacar(Unidad objetivo), recibirDaño(int daño), estaViva(): boolean
- `class Guerrero extends Unidad` - hp: 80, daño: 25, rangoMov: 3, rangoAtaque: 1
- `class Arquero extends Unidad` - hp: 60, daño: 20, rangoMov: 2, rangoAtaque: 4
- `class Tanque extends Unidad` - hp: 120, daño: 15, rangoMov: 2, rangoAtaque: 1
- `class Tablero` - atributos: celdas[][], filas, columnas; métodos: inicializar(int n, int m), colocarUnidad(Unidad, int x, int y), moverUnidad(Unidad, int x, int y), getCelda(int x, int y): Celda, hayEnemigoEnRango(Unidad): boolean
- `class Jugador` - atributos: id (int), nombre (String), unidades (ArrayList<Unidad>), historialAcciones (ArrayList<String>); métodos: tieneUnidadesVivas(): boolean, getUnidadesVivas(): ArrayList
- `class Juego` - atributos: tablero (Tablero), jugador1 (Jugador), jugador2 (Jugador), turnoActual (int), terminado (boolean); métodos: inicializar(), ejecutarMovimiento(Jugador, Unidad, int x, int y), ejecutarAtaque(Jugador, Unidad, Unidad), cambiarTurno(), verificarFin(): boolean, getGanador(): Jugador
- `class Main` -演示 del sistema

---

## 11. Gestor de Reservas de Cine

**Contexto:** Un cine tiene salas, cada sala tiene asientos organizados en filas y columnas. Las películas tienen título, duración, género y clasificación de edad.

**Descripción:** Implementa un sistema donde:
- Las salas se gestionan con HashMap (clave: numero_sala)
- Cada sala tiene una matriz de booleanos para asientos disponibles/ocupados
- Los clientes hacen reservas con: película, sala, lista de asientos deseados
- Si todos los asientos están disponibles, se confirman y marcan como ocupados
- Se puede cancelar una reserva (liberando los asientos)
- El sistema calcula: ocupación por sala, película más popular, ingresos totales

**Requisitos técnicos:** HashMap, Arrays bidimensionales, Herencia (Reserva clase padre, ReservaIndividual, ReservaGrupo), Interfaces.

**Clases a implementar:**
- `enum Género` - constantes: ACCION, COMEDIA, DRAMA, TERROR, CIENCIA_FICCION, ANIMACION
- `enum Clasificación` - constantes: AA, A, B, C, D
- `class Película` - atributos: título (String), duración (int minutos), género (Género), clasificación (Clasificación); métodos: getters
- `class Asiento` - atributos: fila (char), columna (int), disponible (boolean)
- `class Sala` - atributos: numero (int), película (Película), asientos[][], filas, columnas, precioBase (double); métodos: getAsiento(char, int): Asiento, reservar(ArrayList<Asiento>): boolean, liberar(ArrayList<Asiento>), getOcupación(): double, getAsientosDisponibles(): ArrayList<Asiento>
- `interface Reserva` - métodos: confirmar(): boolean, cancelar(): double
- `abstract class ReservaBase implements Reserva` - atributos: id (String), cliente (String), sala (Sala), asientos (ArrayList<Asiento>), precioTotal (double), confirmada (boolean)
- `class ReservaIndividual extends ReservaBase` - atributos: asientoIndividual (Asiento)
- `class ReservaGrupo extends ReservaBase` - atributos: cantidadAsientos (int)
- `class GestorCine` - atributos: salas (HashMap<Integer, Sala>), reservas (HashMap<String, Reserva>), películas (ArrayList<Película>), ingresosTotales (double); métodos: crearSala(int num, Película, int filas, int cols), hacerReserva(String cliente, int sala, Película, ArrayList<Asiento>): Reserva, cancelarReserva(String id): double, getOcupaciónSala(int num): double, getPelículaMásPopular(): Película, getIngresosTotales(): double
- `class Main` -演示 del sistema

---

## 12. Simulación de Evolución Genética

**Contexto:** Una población de criaturas virtuales tiene genes que determinan sus características: velocidad, fortaleza, inteligencia. Las criaturas pueden reproducirse combinando genes de dos padres.

**Descripción:** Crea un simulador donde:
- Cada criatura tiene un HashMap de genes (clave: nombre gen, valor: valor numérico)
- La reproducción toma dos criaturas y crea una nueva con:
  - 50% genes del padre 1, 50% del padre 2 (alternados)
  - Posibilidad de mutación (10% de cambiar un gen aleatoriamente)
- Cada generación vive "X" turnos donde buscan comida
- Las criaturas con mejores stats sobreviven más y tienen más oportunidad de reproducirse
- El sistema muestra la evolución de la población a lo largo de las generaciones

**Requisitos técnicos:** HashMap, ArrayList, Clases abstractas (Criatura), Herencia, Polimorfismo.

**Clases a implementar:**
- `enum TipoGen` - constantes: VELOCIDAD, FORTALEZA, INTELIGENCIA, RESISTENCIA, AGRESIVIDAD
- `class Genética` - atributos: genes (HashMap<TipoGen, Integer>); métodos: getGen(TipoGen): Integer, setGen(TipoGen, int), mutar(double probabilidad), combinar(Genética padre2): Genética
- `abstract class Criatura` - atributos: id (String), genética (Genética), energía (int), edad (int), viva (boolean); métodos abstractos: getDescripcion(): String; métodos: buscarComida(int cantidad), reproducir(Criatura otra): Criatura, envejecer(), estaViva(): boolean, getFitness(): int
- `class Depredador extends Criatura` - atributos: tamaño (int); métodos: getDescripcion(), cazar(ArrayList<Criatura>)
- `class Presa extends Criatura` - atributos: velocidadBase (int); métodos: getDescripcion(), huir(ArrayList<Depredador>)
- `class Población` - atributos: criaturas (ArrayList<Criatura>), generación (int), turnoActual (int), maxTurnosPorGen (int); métodos: siguienteTurno(), reproducirSiguienteGeneración(), seleccionarPadres(): ArrayList<Criatura>, getEstadísticas(): String
- `class Ecosistema` - atributos: población (Población), comidaTotal (int); métodos: simular(int generaciones), mostrarEvolución()
- `class Main` -演示 del sistema

---

## 13. Procesador de Texto con Estilos

**Contexto:** Un editor de texto soporta diferentes estilos de formato: negrita, cursiva, subrayado, código. Cada segmento de texto tiene un estilo asociado.

**Descripción:** Implementa un sistema donde:
- El documento se representa como un ArrayList de Segmento
- Cada segmento tiene: texto, estilo, posición inicio, posición fin
- Se pueden aplicar estilos a rangos específicos (sobrescribiendo si ya existe)
- El sistema permite: buscar todas las ocurrencias de una palabra, contar palabras por estilo
- Serializa el documento a HTML simple (convertir estilos a etiquetas)
- Deserializa desde HTML creando la estructura de segmentos

**Requisitos técnicos:** Clases abstractas (Segmento), Herencia para tipos de estilo, ArrayList, Interfaces (Formateable).

**Clases a implementar:**
- `enum Estilo` - constantes: NORMAL, NEGRITA, CURSIVA, SUBRAYADO, CÓDIGO
- `interface Formateable` - métodos: aHTML(): String, desdeHTML(String html)
- `abstract class Segmento implements Formateable` - atributos: texto (String), estilo (Estilo), inicio (int), fin (int); métodos abstractos: getLongitud(): int
- `class SegmentoNormal extends Segmento`
- `class SegmentoNegrita extends Segmento`
- `class SegmentoCursiva extends Segmento`
- `class SegmentoSubrayado extends Segmento`
- `class SegmentoCódigo extends Segmento`
- `class Documento` - atributos: título (String), segmentos (ArrayList<Segmento>); métodos: añadirSegmento(Segmento), aplicarEstilo(Estilo, int inicio, int fin), buscarPalabra(String): ArrayList<Segmento>, contarPorEstilo(): HashMap<Estilo, Integer>, aHTML(): String, static desdeHTML(String html): Documento
- `class Main` -演示 del sistema

---

## 14. Sistema de Subastas

**Contexto:** Una casa de subastas vende items únicos. Los postores hacen ofertas y el item se vende al mayor ofertante cuando termina el tiempo.

**Descripción:** Crea un sistema donde:
- Los items en subasta se almacenan en HashMap (clave: ID_item)
- Cada item tiene: nombre, precio base, plazo (en ticks), ofertas actuales
- Las ofertas se ordenan por monto (la mayor primero)
- Cuando expira el plazo, el item se marca como "vendido" al mejor postor
- El sistema puede: crear/subastar items, hacer ofertas, consultar estado, generar reporte de subastas activas/terminadas
- Hay una comisión del 10% sobre el precio final

**Requisitos técnicos:** HashMap, ArrayList, Comparable (para ordenar ofertas), Herencia (ItemSubasta, ItemArte, ItemAntiguo).

**Clases a implementar:**
- `enum EstadoSubasta` - activa, TERMINADA, CANCELADA
- `enum TipoItem` - constantes: ARTE, ANTIGUO, JOYERIA, ELECTRONICA
- `class Oferta implements Comparable<Oferta>` - atributos: postor (String), monto (double), tiempo (int); métodos: compareTo(Oferta)
- `abstract class ItemSubasta` - atributos: id (String), nombre (String), descripcion (String), tipo (TipoItem), precioBase (double), plazo (int), tiempoActual (int), ofertas (ArrayList<Oferta>), estado (EstadoSubasta), vendidoA (String), precioVenta (double); métodos abstractos: getValorEstimado(): double
- `class ItemArte extends ItemSubasta` - atributos: artista (String), año (int), técnica (String)
- `class ItemAntiguo extends ItemSubasta` - atributos: época (String), estadoConservación (String), autenticado (boolean)
- `class ItemJoyería extends ItemSubasta` - atributos: material (String), quilates (int), gema (String)
- `class Subasta` - atributos: items (HashMap<String, ItemSubasta>), postores (HashMap<String, String>), comisión (double 0.10); métodos: crearItem(ItemSubasta), hacerOferta(String idItem, String postor, double monto), avanzarTiempo(), getItem(String): ItemSubasta, getActivas(): ArrayList<ItemSubasta>, getTerminadas(): ArrayList<ItemSubasta>, generarReporte(): String
- `class Main` -演示 del sistema

---

## 15. Grafo de Conexiones de Redes Sociales

**Contexto:** Una red social representa las conexiones entre usuarios como un grafo no dirigido. Cada usuario puede seguir a otros y ser seguido.

**Descripción:** Implementa un sistema donde:
- Los usuarios se almacenan en HashMap (clave: username)
- Las conexiones se manejan con HashMap<Usuario, ArrayList<Usuario>> (seguidores y seguidos)
- Se puede calcular: número de seguidores de un usuario, usuario más popular, sugerir usuarios que podría conocer (amigos de amigos)
- Detectar ciclos en las conexiones (si A sigue a B, B sigue a C, C sigue a A)
- Calcular la "distancia" entre dos usuarios (mínimo de saltos entre ellos)

**Requisitos técnicos:** HashMap, ArrayList, Clases abstractas (Usuario), Herencia, Interfaces.

**Clases a implementar:**
- `interface SocialGraph` - métodos: seguir(Usuario, Usuario), dejarSeguir(Usuario, Usuario), getSeguidores(Usuario): ArrayList, getSeguidos(Usuario): ArrayList, tieneCiclo(): boolean, sugerirAmigos(Usuario): ArrayList, distancia(Usuario, Usuario): int
- `enum TipoUsuario` - constantes: NORMAL, INFLUENCER, VERIFICADO, BOTS
- `abstract class Usuario` - atributos: username (String), nombre (String), bio (String), tipo (TipoUsuario), seguidores (ArrayList<Usuario>), seguidos (ArrayList<Usuario>); métodos abstractos: getTipo(): String; métodos: seguir(Usuario), dejarSeguir(Usuario), getNumSeguidores(): int, getNumSeguidos(): int
- `class UsuarioNormal extends Usuario`
- `class UsuarioInfluencer extends Usuario` - atributos: seguidoresCount (int), verificación (boolean)
- `class RedSocial implements SocialGraph` - atributos: usuarios (HashMap<String, Usuario>); métodos: registrarUsuario(Usuario), buscarUsuario(String): Usuario, sugerirAmigos(Usuario): ArrayList<Usuario>, detectarCiclos(): boolean, distancia(Usuario, Usuario): int, getUsuarioMasPopular(): Usuario
- `class Main` -演示 del sistema

---

## 16. Juego de Mazmorras Procedurales

**Contexto:** Un roguelike genera dungeons con habitaciones conectadas. Cada habitación puede contener: enemigo, tesoro, trampa, NPC, o estar vacía.

**Descripción:** Crea un generador donde:
- El dungeon es un grafo de habitaciones (HashMap de conexiones)
- Cada habitación tiene: tipo, items contenidos, enemigos, estado (visitada/no visitada)
- El jugador explora habitación por habitación
- Al entrar a una habitación con enemigo, ocurre un combate automático
- Los tesoros dan puntos o items útiles para el combate
- El juego termina cuando el jugador muere o encuentra la salida
- Generación procedural: cada juego es diferente

**Requisitos técnicos:** Herencia (Habitacion como padre, Tesoro, Enemigo, Trampa como hijos), HashMap (conexiones), ArrayList, Polimorfismo.

**Clases a implementar:**
- `enum TipoHabitacion` - VACIA, COMBATE, TESORO, TRAMPA, NPC, SALIDA, JEFE
- `enum TipoEnemigo` - ESQUELETO, ORCO, GOBLIN, DRAGON, JEFE_FINAL
- `enum TipoItem` - POCION, ARMA, ARMADURA, LLAVE, TESORO
- `class Posición` - atributos: x (int), y (int)
- `abstract class Contenido` - métodos abstractos: getDescripcion(): String
- `class Enemigo extends Contenido` - atributos: nombre (String), tipo (TipoEnemigo), hp (int), daño (int), drop (TipoItem)
- `class Tesoro extends Contenido` - atributos: tipo (TipoItem), valor (int)
- `class Trampa extends Contenido` - atributos: daño (int), activada (boolean)
- `class NPC extends Contenido` - atributos: nombre (String), diálogo (String), misión (boolean)
- `class Habitación` - atributos: id (int), tipo (TipoHabitacion), contenido (ArrayList<Contenido>), conexiones (ArrayList<Habitación>), visitada (boolean), posición (Posición); métodos: añadirConexión(Habitación), entrar(): String
- `class Jugador` - atributos: nombre (String), hp (int), hpMax (int), daño (int), defensa (int), inventario (ArrayList<TipoItem>), posición (Posición), experiencia (int), nivel (int); métodos: atacar(Enemigo), recibirDaño(int), usarPocion(), estaVivo(): boolean
- `class Mazmorra` - atributos: habitaciones (HashMap<Integer, Habitación>,), habitaciónInicial (Habitación), habitaciónSalida (Habitación), generar(): void
- `class Juego` - atributos: jugador (Jugador), mazmorra (Mazmorra), enCurso (boolean); métodos: explorar(int idHabitacion), combate(Enemigo), buscarSalida(): boolean
- `class Main` -演示 del sistema

---

## 17. Simulador de Bolsa de Valores

**Contexto:** Un mercado de valores tiene acciones de diferentes empresas. Los precios varían según oferta/demanda y noticias del mercado.

**Descripción:** Implementa un simulador donde:
- Las empresas tienen: símbolo, nombre, precio actual, volatilidad
- Los inversores tienen: nombre, dinero, portfolio de acciones poseídas
- En cada "tick": los precios fluctúan según volatilidad + factor aleatorio
- Los inversores pueden: comprar (si tienen dinero), vender (si tienen acciones)
- Hay eventos aleatorios que afectan sectores específicos (sube/baja)
- El sistema muestra: valor del portfolio de cada inversor, acción con mayor ganancia/pérdida

**Requisitos técnicos:** HashMap (portfolios), ArrayList, Herencia (Inversor como padre, Conservador, Agresivo como hijos), Interfaces (Operable).

**Clases a implementar:**
- `enum Sector` - constantes: TECNOLOGÍA, SALUD, ENERGÍA, FINANZAS, CONSUMO, INDUSTRIA
- `class Acción` - atributos: símbolo (String), nombre (String), sector (Sector), precioActual (double), precioAnterior (double), volatilidad (double); métodos: actualizarPrecio(), getVariaciónPorcentual(): double
- `class Portafolio` - atributos: acciones (HashMap<Acción, Integer>), valorTotal (double); métodos: añadirAcción(Acción, int), venderAcción(Acción, int), getValor(): double, getDetalle(): String
- `interface Operable` - métodos: comprar(Acción, int, double), vender(Acción, int), puedeComprar(double monto): boolean
- `abstract class Inversor implements Operable` - atributos: nombre (String), dinero (double), portafolio (Portafolio); métodos abstractos: getTipo(): String; métodos: comprar(Acción, int, double), vender(Acción, int), getPatrimonioTotal(): double
- `class InversorConservador extends Inversor` - atributos: riesgoMax (double 0.05); métodos: getTipo(), tomarDecisión(Acción): boolean
- `class InversorAgresivo extends Inversor` - atributos: toleranciaRiesgo (double 0.30); métodos: getTipo(), tomarDecisión(Acción): boolean
- `class Mercado` - atributos: acciones (HashMap<String, Acción>), inversores (ArrayList<Inversor>), eventos (ArrayList<String>); métodos: siguienteTick(), aplicarEvento(Sector, double cambio), getAcciónMayorGanancia(): Acción, getAcciónMayorPérdida(): Acción
- `class Main` -演示 del sistema

---

## 18. Gestor de Biblioteca de Videojuegos

**Contexto:** Un coleccionista tiene una biblioteca de juegos con información: título, género, plataforma, horas jugadas, estado (sin jugar, en progreso, completado).

**Descripción:** Crea un sistema donde:
- Los juegos se organizan por plataforma usando HashMap<String, ArrayList<Videojuego>>
- Se puede filtrar por: género, estado, plataforma
- Calcular: total de horas jugadas, juego más completado, juegos sin jugar por plataforma
- Marcar progreso en un juego (sumar horas jugadas)
- Recomendaciones: juegos similares al último jugado (mismo género, no jugados)
- Estadísticas: distribución por género, distribución por estado

**Requisitos técnicos:** HashMap, ArrayList, Clases abstractas (Videojuego), Herencia, Interfaces.

**Clases a implementar:**
- `enum Género` - constantes: ACCION, AVENTURA, RPG, ESTRATEGIA, SIMULACIÓN, DEPORTES, CARRERAS, PUZZLE, HORROR
- `enum Plataforma` - constantes: PC, PLAYSTATION, XBOX, NINTENDO_SWITCH, MÓVIL
- `enum Estado` - constantes: SIN_JUGAR, EN_PROGRESO, COMPLETADO, ABANDONADO
- `interface Recomendable` - métodos: esSimilar(Videojuego): boolean, getPuntuaciónSimilaridad(Videojuego): double
- `abstract class Videojuego implements Recomendable` - atributos: título (String), género (Género), plataforma (Plataforma), horasJugadas (double), estado (Estado), fechaAdquisición (LocalDate); métodos abstractos: getDescripcion(): String; métodos: añadirHoras(double), marcarEstado(Estado), esSimilar(Videojuego)
- `class VideojuegoFísico extends Videojuego` - atributos: disco (boolean), estadoFísico (String)
- `class VideojuegoDigital extends Videojuego` - atributos: tamañoGB (double), plataformaDigital (String)
- `class Biblioteca` - atributos: juegos (HashMap<Plataforma, ArrayList<Videojuego>>), últimoJugado (Videojuego); métodos: añadirJuego(Videojuego), eliminarJuego(Videojuego), filtrarPorGénero(Género): ArrayList<Videojuego>, filtrarPorEstado(Estado): ArrayList<Videojuego>, filtrarPorPlataforma(Plataforma): ArrayList<Videojuego>, getTotalHoras(): double, getJuegoMasCompletado(): Videojuego, getSinJugarPorPlataforma(Plataforma): ArrayList<Videojuego>, getRecomendaciones(): ArrayList<Videojuego>, getEstadísticas(): String
- `class Main` -演示 del sistema

---

## 19. Sistema de Control de Drones

**Contexto:** Una flota de drones de reparto tiene diferentes modelos con características distintas: velocidad máxima, capacidad de carga, autonomía de batería.

**Descripción:** Implementa un sistema donde:
- Los drones se gestionan con HashMap (clave: ID_dron)
- Cada dron tiene: posición actual (x, y), carga actual, batería restante, estado (disponible, en misión, cargando, mantenimiento)
- Las misiones tienen: origen, destino, peso del paquete, prioridad
- El sistema asigna el mejor dron disponible (menor tiempo estimado de llegada)
- Los drones se mueven hacia el destino en cada tick
- Al llegar, vuelven a base (posición 0,0)
- Reporte: drones en misión, promedio de tiempo de entrega, eficiencia de la flota

**Requisitos técnicos:** Herencia (Dron como padre, DronLite, DronStandard, DronHeavy), HashMap, ArrayList, Polimorfismo, Interfaces.

**Clases a implementar:**
- `enum EstadoDron` - constantes: DISPONIBLE, EN_MISIÓN, CARGANDO, MANTENIMIENTO
- `enum Prioridad` - constantes: BAJA, MEDIA, ALTA, URGENTE
- `class Posición` - atributos: x (double), y (double); métodos: distancia(Posición otra): double
- `abstract class Dron` - atributos: id (String), modelo (String), posición (Posición), velocidadMax (double), capacidadCarga (double), batería (int 0-100), cargaActual (double), estado (EstadoDron); métodos abstractos: getTipo(): String; métodos: mover(Posición destino), asignarMisión(Misión), completarMisión(), recargar(), necesitaMantenimiento(): boolean
- `class DronLite extends Dron` - capacidadCarga: 2kg, velocidadMax: 30, batería: 60min
- `class DronStandard extends Dron` - capacidadCarga: 5kg, velocidadMax: 25, batería: 90min
- `class DronHeavy extends Dron` - capacidadCarga: 15kg, velocidadMax: 20, batería: 120min
- `class Misión` - atributos: id (String), origen (Posición), destino (Posición), peso (double), prioridad (Prioridad), dronAsignado (Dron), tiempoEstimado (int), completada (boolean); métodos: getTiempoEstimado(): int
- `class Flota` - atributos: drones (HashMap<String, Dron>), misiones (ArrayList<Misión>), base (Posición); métodos: añadirDron(Dron), crearMisión(Misión), asignarDron(Misión): Dron, siguienteTick(), getDronesEnMisión(): ArrayList<Dron>, getPromedioTiempoEntrega(): double, getEficienciaFlota(): double, generarReporte(): String
- `class Main` -演示 del sistema

---

## 20. Puzzle: Sudoku Solver con Validaciones

**Contexto:** Un resolvedor de Sudoku debe validar y resolver tableros 9x9 aplicando reglas del juego y técnicas de backtracking.

**Descripción:** Crea un sistema donde:
- El tablero se representa como int[9][9] (0 = vacío)
- Validaciones: verificar fila, columna, subcuadrante 3x3
- El solver usa backtracking para encontrar solución
- Permite verificar si un número puede ir en una posición (no repeat en fila/col/region)
- Permite cargar tableros predefinidos
- El sistema detecta tableros inválidos (sin solución posible)
- Muestra el proceso de resolución paso a paso (opcional)

**Requisitos técnicos:** Arrays bidimensionales, Recursión, Clases (Tablero, Solucionador), ArrayList para historial de cambios, Interfaces (Validador).

**Clases a implementar:**
- `interface Validador` - métodos: esVálido(Tablero): boolean, puedeColocar(int num, int fila, int col, Tablero): boolean
- `class Tablero` - atributos: grid[9][9], historial (ArrayList<Movimiento>); métodos: getValor(int fila, int col): int, setValor(int fila, int col, int num), esVacio(int fila, int col): boolean, estáResuelto(): boolean, cargar(int[][] datos), clonar(): Tablero, toString(): String
- `class Movimiento` - atributos: fila (int), col (int), valorAnterior (int), valorNuevo (int), turno (int)
- `class ValidadorSudoku implements Validador` - métodos: esVálido(Tablero), puedeColocar(int num, int fila, int col, Tablero), validarFila(int fila, Tablero): boolean, validarColumna(int col, Tablero): boolean, validarRegión(int fila, int col, Tablero): boolean
- `class Solucionador` - atributos: validador (ValidadorSudoku), intentos (int), resuelto (boolean), mostrarProceso (boolean); métodos: resolver(Tablero, boolean mostrarProceso): boolean, resolverRecursivo(Tablero): boolean, encontrarSiguienteVacío(Tablero): int[], getIntentos(): int
- `class Generador` - atributos: solucionador (Solucionador); métodos: generar(int[][] vacíos): int[][], generarAleatorio(): int[][]
- `class Main` -演示 del sistema con menú interactivo

---

## Soluciones

Las soluciones a estos ejercicios se encuentran en el directorio `src/`. Cada ejercicio tiene su propio paquete con las clases implementadas según las especificacionesabove.
