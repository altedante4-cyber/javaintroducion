# TEMA 4: Optimización y Documentación

## 1. Refactorización

### 1.1 Concepto

- Disciplina técnica que consiste en realizar pequeñas transformaciones en el código para mejorar la estructura sin cambiar su comportamiento ni funcionalidad.
- Objetivo: limpiar el código, minimizando la posibilidad de introducir errores.
- Mejora el diseño, hace el software más fácil de entender y mantener, ayuda a encontrar errores.
- Se diferencia de la optimización porque la optimización busca mejorar el rendimiento (velocidad), mientras que la refactorización busca mejorar la estructura interna. La optimización puede hacer el código más difícil de entender.
- La refactorización no cambia el comportamiento observable del software.

### 1.2 Limitaciones

- **Bases de datos**: muy difíciles de modificar por las interdependencias. La refactorización de una aplicación asociada a una BD siempre será limitada.
- **Cambio de interfaces públicas**: si renombramos un método público, hay que cambiar todas las referencias. Solución: mantener ambas interfaces (nueva y vieja).
- **Errores de diseño**: es muy difícil refactorizar cuando hay un error de diseño estructural importante.
- **Código que no funciona**: no se refactoriza, se reescribe desde el principio.
- La refactorización se usa como técnica complementaria de realización de pruebas.

### 1.3 Patrones de refactorización más habituales

1. **Renombrado (rename)**: cambiar nombre de paquete, clase, método o campo por uno más significativo.
2. **Sustituir bloques de código por un método**: convertir un bloque en un método invocable.
3. **Campos encapsulados**: crear métodos getter y setter para cada campo.
4. **Mover la clase**: mover una clase de un paquete/proyecto a otro para no duplicar código.
5. **Borrado seguro**: comprobar que al borrar un elemento, se borran todas sus referencias.
6. **Cambiar parámetros del proyecto**: añadir/eliminar parámetros, cambiar modificadores de acceso.
7. **Extraer la interfaz**: crear una nueva interfaz a partir de métodos seleccionados.
8. **Mover del interior a otro nivel**: mover una clase interna a un nivel superior.

### 1.4 Analizadores de código (Análisis estático)

- **Análisis estático**: evalúa el software sin ejecutarlo, directamente sobre el código fuente.
- **Funciones**: encontrar código que reduzca rendimiento, provoque errores, tenga excesiva complejidad, problemas de seguridad.
- **PMD**: analizador estático para Java. Detecta patrones de posibles errores, código inalcanzable, código optimizable, expresiones simplificables, malos usos del lenguaje.
- **CPD** (parte de PMD): encuentra código duplicado.
- El análisis puede ser automático (programa como FindBugs en NetBeans) o manual (persona).

#### Uso de PMD en NetBeans

1. Instalar el plugin PMD (descargar de sourceforge, descomprimir y añadir a complementos).
2. Pulsar botón derecho sobre el directorio → Herramientas → Ejecutar PMD.
3. El informe contiene: localización, nombre de la regla incumplida y recomendación.

#### Configuración de PMD

- **Enable Scan**: activa escaneado automático a intervalos regulares.
- **Manage Rules**: activar/desactivar reglas específicas.
- **Manage Rulesets**: importar ficheros XML o JAR con reglas personalizadas.

### 1.5 Refactorización y pruebas (TDD)

- **TDD (Test Driven Development)**: el programador escribe las pruebas antes que el código.
    1. Pensar qué pruebas debe pasar la unidad.
    2. Programar las pruebas.
    3. Implementar la unidad para que pase las pruebas.
    4. Refactorizar el código tan pronto como pasa las pruebas (eliminar redundancia, hacerlo más claro).
- Se van creando pequeñas versiones compilables que pasen alguna prueba.
- El riesgo: cometer errores en la refactorización que hagan que la unidad deje de pasar las pruebas.

### 1.6 Herramientas de ayuda a la refactorización (NetBeans)

- **Renombrar**: actualiza automáticamente todas las referencias en el proyecto.
- **Introducir método**: seleccionar código y reemplazarlo por un método.
- **Encapsular campos**: genera getter/setter automáticamente y actualiza referencias.

---

## 2. Documentación

### Importancia

- Explica el funcionamiento del código punto por punto.
- Fundamental para la detección de errores y el mantenimiento posterior.
- No debe repetir lo que hace el código, sino explicar **por qué** se hace.
- Debe documentar: finalidad de una clase/paquete, qué hace un método, para qué sirve una variable, qué algoritmo se usa, por qué se implementó de una manera, qué se podría mejorar.

### 2.1 Uso de comentarios

- **Dos propósitos**:
    1. Explicar el objetivo de las sentencias.
    2. Explicar qué realiza un método/clase (no cómo lo realiza).
- En Java/C#/C:
    - `// comentario` o `/* comentario */` para explicar sentencias.
    - `/** comentario */` (JavaDoc) para explicar qué hace el código. Pueden ocupar varias líneas.
- Los comentarios JavaDoc deben seguir una estructura prefijada.

### 2.2 Alternativas para documentar

- Comentarios en el código.
- Herramientas automatizadas:
    - **JavaDoc**: genera páginas HTML a partir de comentarios en el código fuente.
    - **SchemaSpy**: genera documentación con modelos de BD gráficos y diagramas.
    - **Doxygen**: similar, genera documentación con diagramas.

### 2.3 Documentación de clases (JavaDoc)

- Los comentarios de clase deben comenzar con `/**` y terminar con `*/`.
- Etiquetas obligatorias:
    - `@author`: nombre del autor.
    - `@version`: versión y fecha.
- Etiqueta opcional: `@see` - referencia a otras clases/métodos.
- Etiquetas para constructores y métodos:
    - `@param` - nombre y descripción de cada parámetro.
    - `@return` - descripción del valor devuelto (si no es void).
    - `@exception` - excepciones que puede lanzar.
    - `@throws` - excepciones que puede lanzar.
- Campos: pueden incluir comentarios, pero no hay etiquetas obligatorias.

### 2.4 Herramientas de documentación

- **JavaDoc** (incluida en Eclipse y NetBeans): genera páginas HTML de documentación.
- **Normas para JavaDoc**:
    1. Comentarios deben empezar por `/**` y terminar por `*/`.
    2. Pueden ser a nivel de clase, variable o método.
    3. La documentación se genera para métodos `public` y `protected`.
    4. Se pueden usar tags para aspectos determinados.

| Tag           | Ámbito    | Descripción                             |
|---------------|-----------|-----------------------------------------|
| `@see`        | Todos     | Referencia a otra clase o método        |
| `@version`    | Clases    | Número de versión                       |
| `@author`     | Clases    | Nombre del autor                        |
| `@since`      | Clases    | Fecha desde la que está presente        |
| `@param`      | Métodos   | Parámetros que recibe el método         |
| `@return`     | Métodos   | Significado del valor devuelto          |
| `@throws`     | Métodos   | Excepciones que lanza                   |
| `@deprecated` | Métodos   | Indicación de método obsoleto           |
