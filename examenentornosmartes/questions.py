questions = [
    {
        "question": "¿Cuál es la definición principal de refactorización en la Ingeniería del Software?",
        "options": [
            "Modificar el código para añadir nuevas funcionalidades.",
            "Corregir errores en el código sin cambiar su estructura.",
            "Modificar la estructura interna del código sin alterar su comportamiento externo.",
            "Reescribir el código desde cero para mejorar el rendimiento."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Cuál de los siguientes NO es un propósito de la refactorización?",
        "options": [
            "Limpieza del código.",
            "Añadir nuevas funcionalidades.",
            "Mantenimiento del código.",
            "Eliminación de código 'muerto'."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué ocurre si después de refactorizar el funcionamiento del código se ve alterado?",
        "options": [
            "Significa que la refactorización fue exitosa.",
            "Indica que se han introducido nuevas funcionalidades.",
            "Se considera que se han cometido errores en el proceso de refactorización.",
            "Es un efecto secundario normal y esperado de la refactorización."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Por qué las convenciones de código son fundamentales en el desarrollo de software?",
        "options": [
            "Porque reducen el tiempo de ejecución del programa.",
            "Porque la mayoría del coste del código se usa en su mantenimiento y mejoran la lectura.",
            "Porque garantizan que el código no tendrá errores.",
            "Porque son obligatorias por ley en la mayoría de los países."
        ],
        "correct_answer": 1
    },
    {
        "question": "Según las convenciones de Java, ¿cuál es el orden correcto de los elementos dentro de un fichero .java?",
        "options": [
            "Sentencia package, comentarios, sentencias import, definición de clase.",
            "Definición de clase, sentencias import, sentencia package, comentarios.",
            "Comentarios, sentencia package, sentencias import, definición de clase.",
            "Sentencias import, comentarios, sentencia package, definición de clase."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Cómo deben declararse las sentencias `import` en un fichero Java?",
        "options": [
            "Todas en una sola línea separadas por comas.",
            "Usando un comodín (`*`) para importar todas las clases de un paquete.",
            "Cada clase importada en una línea separada.",
            "No es necesario declararlas si las clases están en el mismo paquete."
        ],
        "correct_answer": 2
    },
    {
        "question": "Dentro de la definición de una clase Java, ¿cuál es el orden recomendado para los constructores y métodos?",
        "options": [
            "Métodos, luego constructores.",
            "Constructores, luego métodos (agrupados si hay sobrecarga).",
            "No hay un orden específico, pueden ir mezclados.",
            "Variables de instancia, luego constructores, luego métodos."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Cómo deben declararse las variables locales según las buenas prácticas?",
        "options": [
            "Al inicio de la clase, junto con las variables de instancia.",
            "Sin inicializar hasta que sean estrictamente necesarias.",
            "En el momento de declararlas o justo después, y lo más cerca posible de su uso.",
            "Una por línea, pero sin inicializar para ahorrar memoria."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Cuál es la forma correcta de declarar un array en Java según las convenciones?",
        "options": [
            "`String nombres[];`",
            "`String[] nombres;`",
            "`Array<String> nombres;`",
            "`List<String> nombres;`"
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué tipo de caracteres se deben evitar en los nombres de identificadores en Java?",
        "options": [
            "Letras anglosajonas y números ASCII.",
            "Caracteres con tilde, la 'ñ', barras bajas o guiones (excepto en constantes).",
            "Solo números.",
            "Solo letras mayúsculas."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Cómo deben nombrarse las clases o interfaces en Java?",
        "options": [
            "`lowerCamelCase`",
            "`CONSTANT_CASE`",
            "`UpperCamelCase`",
            "Todo en minúsculas."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Cuál es la convención de nombres para las constantes en Java?",
        "options": [
            "`lowerCamelCase`",
            "`UpperCamelCase`",
            "`CONSTANT_CASE` (todo en mayúsculas, separando con barra baja).",
            "`camelCase` con la primera letra en mayúscula."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Qué son los 'Magic Numbers'?",
        "options": [
            "Números aleatorios generados por el sistema.",
            "Valores literales sin explicación utilizados directamente en el código.",
            "Constantes predefinidas en la API de Java.",
            "Números que se usan solo una vez en el código."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Cuál es la solución recomendada para los 'Magic Numbers'?",
        "options": [
            "Dejarlos como están si el código funciona.",
            "Comentarlos extensamente en cada aparición.",
            "Reemplazarlos por constantes con nombres descriptivos.",
            "Usar variables locales en su lugar."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Qué codificación se recomienda usar para la estructura del código?",
        "options": [
            "ASCII.",
            "ISO-8859-1.",
            "UTF-8.",
            "UTF-16."
        ],
        "correct_answer": 2
    },
    {
        "question": "Según las buenas prácticas, ¿cómo deben usarse las llaves `{}` en sentencias de control de flujo?",
        "options": [
            "Solo si contienen más de una instrucción.",
            "Nunca, si la instrucción es simple.",
            "Siempre, incluso si no contienen código o es una sola instrucción, alineadas al inicio de línea.",
            "Solo en bucles `for` y `while`."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Cuál es la longitud máxima recomendada para las líneas de código?",
        "options": [
            "80 caracteres.",
            "100 caracteres.",
            "120 caracteres.",
            "No hay límite, siempre que sea legible."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué son los 'Bad Smells' o 'Code Smells'?",
        "options": [
            "Errores de sintaxis que impiden la compilación del programa.",
            "Bugs que causan un comportamiento incorrecto del programa.",
            "Indicadores o síntomas en el código que sugieren un problema de diseño subyacente.",
            "Comentarios mal escritos en el código."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Qué Bad Smell se refiere a bloques de código idénticos o muy similares en distintas partes del programa?",
        "options": [
            "Long Method.",
            "Large Class.",
            "Duplicated Code.",
            "Feature Envy."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Cuál es la solución recomendada para un 'Long Method'?",
        "options": [
            "Aumentar el número de comentarios en el método.",
            "Dividir el método en métodos más pequeños, cada uno con una única responsabilidad.",
            "Ignorarlo si el método funciona correctamente.",
            "Cambiar el nombre del método para que sea más descriptivo."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué Bad Smell describe una clase con demasiados métodos, atributos o instancias, indicando múltiples responsabilidades?",
        "options": [
            "Long Parameter List.",
            "Large Class.",
            "Divergent Change.",
            "Shotgun Surgery."
        ],
        "correct_answer": 1
    },
    {
        "question": "Si un método requiere muchos parámetros, ¿qué solución se sugiere para evitar el 'Long Parameter List'?",
        "options": [
            "Pasar los parámetros como un array de objetos.",
            "Crear una clase para agrupar los datos y pasar un objeto de esa clase como parámetro.",
            "Reducir el número de funcionalidades del método.",
            "Usar variables globales en lugar de parámetros."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué Bad Smell ocurre cuando una clase necesita ser modificada frecuentemente por razones muy distintas?",
        "options": [
            "Feature Envy.",
            "Refused Bequest.",
            "Divergent Change.",
            "Shotgun Surgery."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Qué significa 'Feature Envy' como Bad Smell?",
        "options": [
            "Una clase que tiene demasiados atributos.",
            "Un método de una clase utiliza más funcionalidades de otra clase que de la propia.",
            "Una clase que no utiliza todas las funcionalidades que hereda.",
            "Un método que es demasiado largo."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Cuál es la forma más eficiente de instanciar un `String` en Java?",
        "options": [
            "`String s = new String(\"texto\");`",
            "`String s = \"texto\";`",
            "`StringBuilder sb = new StringBuilder(\"texto\");`",
            "`char[] c = {'t', 'e', 'x', 't', 'o'}; String s = new String(c);`"
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Por qué se debe evitar la concatenación de `String` con `+` dentro de bucles?",
        "options": [
            "Porque el operador `+` no funciona con `String` en bucles.",
            "Porque crea nuevos objetos `String` en memoria, lo que es ineficiente.",
            "Porque puede causar errores de compilación.",
            "Porque `String` son mutables y esto puede llevar a resultados inesperados."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué es más rápido en Java, los tipos primitivos o las clases `Wrapper`?",
        "options": [
            "Las clases `Wrapper` son siempre más rápidas.",
            "Los tipos primitivos son más rápidos porque las clases `Wrapper` son objetos.",
            "Ambos tienen el mismo rendimiento.",
            "Depende del compilador de Java."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Cómo se deben comparar objetos (incluidos `String` y `Wrapper`) en Java para verificar su contenido?",
        "options": [
            "Con el operador `==`.",
            "Con el método `equals()`.",
            "Con el operador `!=`.",
            "Con el método `compareTo()`."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Cuál es la visibilidad recomendada para los atributos de una clase 'estándar'?",
        "options": [
            "`public`.",
            "`protected`.",
            "`private`, accediendo a ellos mediante `setters` y `getters`.",
            "Sin modificador de visibilidad."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Dónde se recomienda declarar e inicializar una variable local?",
        "options": [
            "Al inicio de la función, independientemente de cuándo se use.",
            "Lo más cerca posible de su uso para limitar su ámbito.",
            "Como variable global para facilitar el acceso.",
            "Solo cuando sea estrictamente necesario, sin inicializarla de inmediato."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Por qué se prefiere el bucle `for` sobre `while` o `do-while` cuando es posible?",
        "options": [
            "Porque es el único bucle que permite iterar sobre colecciones.",
            "Porque concentra el control del bucle en una sola línea y la variable de control no es accesible fuera de él.",
            "Porque es más rápido en todos los escenarios.",
            "Porque `while` y `do-while` están obsoletos."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué valores literales NO necesitan ser definidos como constantes?",
        "options": [
            "Cualquier número entero.",
            "Cualquier cadena de texto.",
            "0, 1, -1 o 2 en contextos de bucles.",
            "Números decimales."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Qué debe incluir siempre una sentencia `switch` según las buenas prácticas?",
        "options": [
            "Al menos un caso vacío.",
            "Un `break` después de cada caso y un caso `default`.",
            "Solo el caso `default`.",
            "No es necesario incluir `break` si solo hay un caso."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué es el 'copiado defensivo' en el contexto de un constructor que recibe un objeto del mismo tipo de la clase?",
        "options": [
            "Crear una copia exacta del objeto recibido para evitar referencias compartidas.",
            "Asegurarse de que el objeto recibido sea `null`.",
            "Modificar el objeto recibido directamente.",
            "No hacer nada, ya que Java maneja esto automáticamente."
        ],
        "correct_answer": 0
    },
    {
        "question": "¿Qué herramienta de refactorización en Eclipse permite cambiar el nombre de cualquier identificador y actualizar todas sus referencias?",
        "options": [
            "`Move`.",
            "`Extract Method`.",
            "`Rename`.",
            "`Inline`."
        ],
        "correct_answer": 2
    },
    {
        "question": "Si necesitas mover una clase Java de un paquete a otro, ¿qué opción de refactorización en Eclipse usarías?",
        "options": [
            "`Rename`.",
            "`Move`.",
            "`Extract Constant`.",
            "`Change Method Signature`."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué hace la refactorización `Extract Constant` en Eclipse?",
        "options": [
            "Convierte una variable local en una constante de clase.",
            "Convierte un valor literal (número o cadena) en una constante, reemplazando sus apariciones.",
            "Extrae una constante de una interfaz.",
            "Crea una nueva clase con solo constantes."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Cuál es la diferencia principal entre `Extract Constant` y `Extract Local Variable` en Eclipse?",
        "options": [
            "`Extract Constant` es para números y `Extract Local Variable` es para cadenas.",
            "`Extract Constant` crea una constante de clase, mientras que `Extract Local Variable` crea una variable de ámbito local.",
            "No hay diferencia, son lo mismo.",
            "`Extract Constant` solo funciona en métodos estáticos."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué refactorización de Eclipse convierte un bloque de código seleccionado en un nuevo método?",
        "options": [
            "`Inline`.",
            "`Change Method Signature`.",
            "`Extract Method`.",
            "`Extract Interface`."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Qué permite la refactorización `Change Method Signature` en Eclipse?",
        "options": [
            "Cambiar solo el nombre del método.",
            "Cambiar solo los parámetros del método.",
            "Cambiar el nombre del método y sus parámetros, actualizando todas las llamadas.",
            "Convertir un método en una constante."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Cuándo es útil la refactorización `Extract Superclass` en Eclipse?",
        "options": [
            "Cuando se quiere eliminar una clase.",
            "Cuando se identifican características comunes que pueden ser compartidas entre varias clases.",
            "Cuando una clase es demasiado pequeña.",
            "Cuando se necesita cambiar el nombre de una clase."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué Bad Smell se soluciona extrayendo bloques de código idénticos o muy similares en un método unificado?",
        "options": [
            "Long Method.",
            "Large Class.",
            "Duplicated Code.",
            "Long Parameter List."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Qué Bad Smell se caracteriza por una clase que utiliza más funcionalidades de otra clase que de la propia?",
        "options": [
            "Shotgun Surgery.",
            "Refused Bequest.",
            "Feature Envy.",
            "Divergent Change."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Qué indica el Bad Smell 'Refused Bequest'?",
        "options": [
            "Una clase que no hereda de ninguna otra.",
            "Una subclase que utiliza muy pocas características de su superclase.",
            "Una clase que hereda de demasiadas superclases.",
            "Una superclase que no tiene subclases."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Cuál es la principal ventaja de usar `StringBuilder` para concatenar cadenas en bucles?",
        "options": [
            "Es más fácil de escribir.",
            "Es más eficiente porque no crea nuevos objetos `String` en cada concatenación.",
            "Permite usar el operador `+` de forma segura.",
            "Solo funciona con tipos primitivos."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué significa que los objetos `String` son inmutables en Java?",
        "options": [
            "Que no se pueden comparar.",
            "Que su valor no puede ser cambiado una vez creados.",
            "Que solo se pueden crear una vez.",
            "Que no se pueden concatenar."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Cuál es la consecuencia de no limitar el alcance de una variable local?",
        "options": [
            "Mejora el rendimiento del programa.",
            "Aumenta la legibilidad del código.",
            "Puede llevar a errores y dificultar el mantenimiento.",
            "No tiene ningún efecto."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Qué Bad Smell se produce cuando un cambio en una clase requiere modificaciones en muchas otras clases?",
        "options": [
            "Divergent Change.",
            "Shotgun Surgery.",
            "Feature Envy.",
            "Large Class."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué refactorización de Eclipse permite crear una interfaz a partir de los métodos seleccionados de una clase?",
        "options": [
            "`Extract Method`.",
            "`Extract Superclass`.",
            "`Extract Interface`.",
            "`Change Method Signature`."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Qué tipo de nombres se usan para los métodos en Java según las convenciones?",
        "options": [
            "`UpperCamelCase`.",
            "`CONSTANT_CASE`.",
            "`lowerCamelCase` (suelen ser verbos o frases).",
            "Todo en minúsculas."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Qué Bad Smell se refiere a métodos con muchas líneas que dificultan su comprensión?",
        "options": [
            "Duplicated Code.",
            "Long Method.",
            "Large Class.",
            "Long Parameter List."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué se recomienda para facilitar la legibilidad en operaciones aritméticas o lógicas con distinta jerarquía?",
        "options": [
            "No usar paréntesis.",
            "Usar paréntesis para agrupar las operaciones.",
            "Depender del orden de precedencia de los operadores.",
            "Escribir cada operación en una línea separada."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Cuál es la importancia de los espacios en blanco en la estructura del código?",
        "options": [
            "No tienen ninguna importancia.",
            "Mejoran la legibilidad del código.",
            "Aumentan el tamaño del archivo.",
            "Solo se usan para alinear el código."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué es un `package` en Java y por qué es importante?",
        "options": [
            "Es un tipo de variable para agrupar datos.",
            "Es una forma de organizar clases y evitar conflictos de nombres.",
            "Es un comentario especial en el código.",
            "Es una palabra clave para definir constantes."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué significa que una clase debe tener una única finalidad bien delimitada?",
        "options": [
            "Que solo puede tener un método.",
            "Que debe ser lo más pequeña posible.",
            "Que debe ser responsable de una sola tarea o concepto.",
            "Que no puede heredar de otras clases."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Qué tipo de identificadores se usan para los contadores de bucles `for`?",
        "options": [
            "Nombres descriptivos completos.",
            "Identificadores de un solo carácter, comenzando con `i`.",
            "`CONSTANT_CASE`.",
            "`UpperCamelCase`."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué es el historial de refactorización en Eclipse?",
        "options": [
            "Un registro de todos los errores de compilación.",
            "Un registro de los cambios de código realizados manualmente.",
            "Un registro de las refactorizaciones aplicadas en un proyecto.",
            "Una herramienta para deshacer todos los cambios en el código."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Cuál es el propósito de `Inline` en Eclipse?",
        "options": [
            "Crear una nueva clase.",
            "Reemplazar una referencia a una variable o método por su valor o implementación directa.",
            "Extraer un bloque de código a un nuevo método.",
            "Cambiar la firma de un método."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué tipo de variables se declaran al comienzo de la definición de la clase?",
        "options": [
            "Variables locales.",
            "Variables de instancia o de clase.",
            "Variables de bucle.",
            "Variables temporales."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué se recomienda para la visibilidad de los atributos de una clase?",
        "options": [
            "Declararlos siempre como `public`.",
            "Declararlos como `private` y usar `setters` y `getters`.",
            "No especificar ningún modificador de visibilidad.",
            "Declararlos como `protected` para facilitar la herencia."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué significa que una variable debe tener un único propósito?",
        "options": [
            "Que solo puede ser usada una vez.",
            "Que no se puede reutilizar para diferentes tareas.",
            "Que debe ser declarada como constante.",
            "Que su nombre debe ser corto."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué es la modularización en el contexto de la refactorización?",
        "options": [
            "Dividir el código en componentes más pequeños y manejables.",
            "Unificar bloques de código duplicados.",
            "Eliminar código 'muerto'.",
            "Cambiar el nombre de las variables."
        ],
        "correct_answer": 0
    },
    {
        "question": "¿Cuál es la principal razón para refactorizar el código?",
        "options": [
            "Añadir nuevas funcionalidades.",
            "Corregir errores.",
            "Mejorar la claridad y simplicidad del código.",
            "Cambiar el lenguaje de programación."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Qué tipo de nombres se usan para los paquetes en Java?",
        "options": [
            "`UpperCamelCase`.",
            "`lowerCamelCase`.",
            "Todo en minúsculas.",
            "`CONSTANT_CASE`."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Qué Bad Smell se refiere a una subclase que hereda pero utiliza pocas características de su superclase?",
        "options": [
            "Feature Envy.",
            "Refused Bequest.",
            "Divergent Change.",
            "Shotgun Surgery."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué se debe hacer si una línea de código supera los 100 caracteres?",
        "options": [
            "Ignorarlo, no afecta la funcionalidad.",
            "Romperla antes de algún operador para mejorar la legibilidad.",
            "Aumentar el tamaño de la fuente en el IDE.",
            "Usar un comentario para indicar que es una línea larga."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué es la 'limpieza del código' en el contexto de la refactorización?",
        "options": [
            "Eliminar todos los comentarios.",
            "Mejorar la consistencia y la claridad del código.",
            "Reducir el número de líneas de código.",
            "Hacer que el código sea más difícil de entender para otros."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Cuál es el propósito de `Extract Local Variable` en Eclipse?",
        "options": [
            "Convertir una variable local en un atributo de clase.",
            "Convertir un valor literal en una variable de ámbito local.",
            "Extraer una variable de un método a una clase.",
            "Cambiar el nombre de una variable local."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué Bad Smell se asocia con métodos que idealmente deberían tener 3 líneas y no más de 15?",
        "options": [
            "Large Class.",
            "Duplicated Code.",
            "Long Method.",
            "Long Parameter List."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Qué se debe hacer con los espacios en blanco en el código?",
        "options": [
            "Eliminarlos para reducir el tamaño del archivo.",
            "Usarlos para mejorar la legibilidad, por ejemplo, entre operadores.",
            "Solo usarlos al inicio de las líneas.",
            "No usarlos en absoluto."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué significa que la refactorización debe ser un paso aislado?",
        "options": [
            "Que debe hacerse al final del proyecto.",
            "Que debe hacerse sin introducir errores de código ni cambiar el funcionamiento.",
            "Que solo una persona debe refactorizar.",
            "Que no debe combinarse con la adición de nuevas funcionalidades."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué tipo de nombres se usan para las variables locales, atributos de la clase y nombres de parámetros?",
        "options": [
            "`UpperCamelCase`.",
            "`CONSTANT_CASE`.",
            "`lowerCamelCase`.",
            "Todo en minúsculas."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Qué ocurre si se usa `==` para comparar dos objetos `String` con el mismo contenido pero instanciados con `new String()`?",
        "options": [
            "Devuelve `true`.",
            "Devuelve `false` porque compara referencias.",
            "Causa un error de compilación.",
            "Depende de la versión de Java."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Cuál es una de las ventajas del bucle `for` sobre `while` o `do-while`?",
        "options": [
            "Permite modificar su variable de control fácilmente.",
            "La variable de control es accesible desde fuera de él.",
            "Reúne todo el control del bucle en la misma línea (inicio, fin, incremento).",
            "Es el único bucle que permite un número fijo de iteraciones."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Qué se recomienda hacer con los valores literales que no son 0, 1, -1 o 2 en contextos de bucles?",
        "options": [
            "Usarlos directamente en el código.",
            "Definirlos como constantes.",
            "Comentarlos.",
            "Convertirlos a variables locales."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué Bad Smell se soluciona creando una clase para agrupar los datos y pasar un objeto de esa clase como parámetro?",
        "options": [
            "Long Method.",
            "Large Class.",
            "Duplicated Code.",
            "Long Parameter List."
        ],
        "correct_answer": 3
    },
    {
        "question": "¿Qué refactorización de Eclipse permite transformar una variable local en un atributo privado de la clase?",
        "options": [
            "`Extract Local Variable`.",
            "`Convert Local Variable to Field`.",
            "`Rename`.",
            "`Inline`."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Cuál es el objetivo principal de las convenciones de código?",
        "options": [
            "Reducir el tamaño del código.",
            "Acelerar la ejecución del programa.",
            "Mejorar la legibilidad y facilitar el mantenimiento.",
            "Evitar el uso de comentarios."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Qué tipo de ficheros son los ficheros fuente de Java?",
        "options": [
            "Binarios.",
            "De texto plano con extensión `.java`.",
            "XML.",
            "HTML."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué se debe hacer si una operación aritmética o lógica se compone de distintos tipos de operaciones con distinta jerarquía?",
        "options": [
            "Dejar que el compilador maneje la precedencia.",
            "Usar paréntesis para facilitar su legibilidad.",
            "Escribir cada operación en una línea separada.",
            "Convertirla en un método separado."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué Bad Smell se asocia con una clase que tiene demasiadas responsabilidades y podría ser dividida?",
        "options": [
            "Long Method.",
            "Large Class.",
            "Divergent Change.",
            "Shotgun Surgery."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Qué es la 'limpieza del código' en el contexto de la refactorización?",
        "options": [
            "Eliminar todos los comentarios.",
            "Mejorar la consistencia y la claridad del código.",
            "Reducir el número de líneas de código.",
            "Hacer que el código sea más difícil de entender para otros."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Cuál es el propósito de `Extract Local Variable` en Eclipse?",
        "options": [
            "Convertir una variable local en un atributo de clase.",
            "Convertir un valor literal en una variable de ámbito local.",
            "Extraer una variable de un método a una clase.",
            "Cambiar el nombre de una variable local."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué Bad Smell se asocia con métodos que idealmente deberían tener 3 líneas y no más de 15?",
        "options": [
            "Large Class.",
            "Duplicated Code.",
            "Long Method.",
            "Long Parameter List."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Qué se debe hacer con los espacios en blanco en el código?",
        "options": [
            "Eliminarlos para reducir el tamaño del archivo.",
            "Usarlos para mejorar la legibilidad, por ejemplo, entre operadores.",
            "Solo usarlos al inicio de las líneas.",
            "No usarlos en absoluto."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué significa que la refactorización debe ser un paso aislado?",
        "options": [
            "Que debe hacerse al final del proyecto.",
            "Que debe hacerse sin introducir errores de código ni cambiar el funcionamiento.",
            "Que solo una persona debe refactorizar.",
            "Que no debe combinarse con la adición de nuevas funcionalidades."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué tipo de nombres se usan para las variables locales, atributos de la clase y nombres de parámetros?",
        "options": [
            "`UpperCamelCase`.",
            "`CONSTANT_CASE`.",
            "`lowerCamelCase`.",
            "Todo en minúsculas."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Qué ocurre si se usa `==` para comparar dos objetos `String` con el mismo contenido pero instanciados con `new String()`?",
        "options": [
            "Devuelve `true`.",
            "Devuelve `false` porque compara referencias.",
            "Causa un error de compilación.",
            "Depende de la versión de Java."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Cuál es una de las ventajas del bucle `for` sobre `while` o `do-while`?",
        "options": [
            "Permite modificar su variable de control fácilmente.",
            "La variable de control es accesible desde fuera de él.",
            "Reúne todo el control del bucle en la misma línea (inicio, fin, incremento).",
            "Es el único bucle que permite un número fijo de iteraciones."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Qué se recomienda hacer con los valores literales que no son 0, 1, -1 o 2 en contextos de bucles?",
        "options": [
            "Usarlos directamente en el código.",
            "Definirlos como constantes.",
            "Comentarlos.",
            "Convertirlos a variables locales."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué Bad Smell se soluciona creando una clase para agrupar los datos y pasar un objeto de esa clase como parámetro?",
        "options": [
            "Long Method.",
            "Large Class.",
            "Duplicated Code.",
            "Long Parameter List."
        ],
        "correct_answer": 3
    },
    {
        "question": "¿Qué refactorización de Eclipse permite transformar una variable local en un atributo privado de la clase?",
        "options": [
            "`Extract Local Variable`.",
            "`Convert Local Variable to Field`.",
            "`Rename`.",
            "`Inline`."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Cuál es el objetivo principal de las convenciones de código?",
        "options": [
            "Reducir el tamaño del código.",
            "Acelerar la ejecución del programa.",
            "Mejorar la legibilidad y facilitar el mantenimiento.",
            "Evitar el uso de comentarios."
        ],
        "correct_answer": 2
    },
    {
        "question": "¿Qué tipo de ficheros son los ficheros fuente de Java?",
        "options": [
            "Binarios.",
            "De texto plano con extensión `.java`.",
            "XML.",
            "HTML."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué se debe hacer si una operación aritmética o lógica se compone de distintos tipos de operaciones con distinta jerarquía?",
        "options": [
            "Dejar que el compilador maneje la precedencia.",
            "Usar paréntesis para facilitar su legibilidad.",
            "Escribir cada operación en una línea separada.",
            "Convertirla en un método separado."
        ],
        "correct_answer": 1
    },
    {
        "question": "¿Qué Bad Smell se asocia con una clase que tiene demasiadas responsabilidades y podría ser dividida?",
        "options": [
            "Long Method.",
            "Large Class.",
            "Divergent Change.",
            "Shotgun Surgery."
        ],
        "correct_answer": 2
    }
]
