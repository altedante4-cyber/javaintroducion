import random
import sys

def run_test():
    questions = [
        {
            "question": "¿En qué consiste la refactorización?",
            "options": [
                "a) Cambiar la funcionalidad del código para que sea más rápido.",
                "b) Realizar pequeñas transformaciones para mejorar la estructura sin cambiar el comportamiento.",
                "c) Reescribir el código desde cero para corregir errores de diseño.",
                "d) Añadir nuevas características al software existente."
            ],
            "answer": "b"
        },
        {
            "question": "¿Cuál es el objetivo principal de la refactorización?",
            "options": [
                "a) Aumentar la velocidad de ejecución.",
                "b) Reducir el consumo de memoria.",
                "c) Limpiar el código y minimizar la posibilidad de introducir errores.",
                "d) Cambiar el comportamiento observable del software."
            ],
            "answer": "c"
        },
        {
            "question": "¿En qué se diferencia la refactorización de la optimización?",
            "options": [
                "a) La refactorización mejora el rendimiento y la optimización la estructura.",
                "b) La refactorización mejora la estructura interna y la optimización busca mejorar el rendimiento.",
                "c) No hay diferencia, son términos sinónimos.",
                "d) La refactorización siempre hace el código más difícil de entender."
            ],
            "answer": "b"
        },
        {
            "question": "¿Qué puede suceder con el código tras una optimización?",
            "options": [
                "a) Siempre se vuelve más fácil de entender.",
                "b) Puede hacerse más difícil de entender.",
                "c) No cambia su legibilidad.",
                "d) Se eliminan automáticamente todos los errores."
            ],
            "answer": "b"
        },
        {
            "question": "¿Por qué es difícil refactorizar aplicaciones asociadas a bases de datos?",
            "options": [
                "a) Porque las bases de datos no permiten cambios.",
                "b) Debido a las fuertes interdependencias.",
                "c) Porque el SQL no se puede refactorizar.",
                "d) No es difícil, es la parte más sencilla."
            ],
            "answer": "b"
        },
        {
            "question": "Si renombramos un método público en una interfaz, ¿cuál es el problema?",
            "options": [
                "a) No hay problema, el IDE lo hace todo.",
                "b) Hay que cambiar todas las referencias externas que lo usan.",
                "c) El compilador dará un error que no se puede arreglar.",
                "d) Se pierde la conexión con la base de datos."
            ],
            "answer": "b"
        },
        {
            "question": "¿Qué se debe hacer con el código que no funciona?",
            "options": [
                "a) Refactorizarlo poco a poco.",
                "b) Aplicar patrones de diseño.",
                "c) Reescribirlo desde el principio.",
                "d) Documentarlo mejor."
            ],
            "answer": "c"
        },
        {
            "question": "¿Qué técnica complementaria se usa junto a la refactorización?",
            "options": [
                "a) La optimización de hardware.",
                "b) La realización de pruebas.",
                "c) El diseño gráfico.",
                "d) La compilación cruzada."
            ],
            "answer": "b"
        },
        {
            "question": "El patrón 'Renombrado' (rename) consiste en:",
            "options": [
                "a) Cambiar el nombre de una variable local por uno más corto.",
                "b) Cambiar el nombre de un elemento por uno más significativo.",
                "c) Borrar nombres de clases duplicadas.",
                "d) Mover una clase a otro paquete."
            ],
            "answer": "b"
        },
        {
            "question": "¿Qué significa 'Encapsular campos'?",
            "options": [
                "a) Hacer todos los campos públicos.",
                "b) Crear métodos getter y setter para cada campo.",
                "c) Mover los campos a una clase externa.",
                "d) Borrar los campos que no se usan."
            ],
            "answer": "b"
        },
        {
            "question": "¿Para qué sirve 'Mover la clase'?",
            "options": [
                "a) Para cambiar el nombre de la clase.",
                "b) Para evitar la duplicación de código moviéndola a otro paquete o proyecto.",
                "c) Para borrar la clase de forma segura.",
                "d) Para convertirla en una interfaz."
            ],
            "answer": "b"
        },
        {
            "question": "¿Qué comprueba el 'Borrado seguro'?",
            "options": [
                "a) Que el archivo se elimine del disco duro.",
                "b) Que al borrar un elemento, se borren o gestionen todas sus referencias.",
                "c) Que el código siga compilando tras el borrado.",
                "d) Que no haya virus en el código."
            ],
            "answer": "b"
        },
        {
            "question": "¿En qué consiste el análisis estático de código?",
            "options": [
                "a) En ejecutar el programa y ver si falla.",
                "b) En evaluar el software sin ejecutarlo, directamente sobre el código fuente.",
                "c) En pedir a un usuario que pruebe la aplicación.",
                "d) En medir el tiempo de respuesta del servidor."
            ],
            "answer": "b"
        },
        {
            "question": "¿Qué es PMD?",
            "options": [
                "a) Un lenguaje de programación nuevo.",
                "b) Un analizador estático para Java.",
                "c) Un compilador optimizado.",
                "d) Una herramienta de diseño de bases de datos."
            ],
            "answer": "b"
        },
        {
            "question": "¿Qué detecta la herramienta CPD (parte de PMD)?",
            "options": [
                "a) Errores de sintaxis.",
                "b) Código duplicado.",
                "c) Falta de comentarios.",
                "d) Variables no inicializadas."
            ],
            "answer": "b"
        },
        {
            "question": "¿Qué contiene un informe de PMD en NetBeans?",
            "options": [
                "a) Solo el nombre del autor.",
                "b) Localización, nombre de la regla incumplida y recomendación.",
                "c) El código fuente corregido automáticamente.",
                "d) Una lista de todas las variables del proyecto."
            ],
            "answer": "b"
        },
        {
            "question": "¿Qué hace la opción 'Enable Scan' en la configuración de PMD?",
            "options": [
                "a) Borra el código mal escrito.",
                "b) Activa el escaneado automático a intervalos regulares.",
                "c) Envía el código a un servidor externo.",
                "d) Desactiva todas las reglas."
            ],
            "answer": "b"
        },
        {
            "question": "¿Qué permite 'Manage Rulesets' en PMD?",
            "options": [
                "a) Cambiar el color de la interfaz.",
                "b) Importar ficheros XML o JAR con reglas personalizadas.",
                "c) Borrar el proyecto actual.",
                "d) Instalar NetBeans."
            ],
            "answer": "b"
        },
        {
            "question": "¿Qué significan las siglas TDD?",
            "options": [
                "a) Total Design Development.",
                "b) Test Driven Development.",
                "c) Technical Data Documentation.",
                "d) Task Delivery Design."
            ],
            "answer": "b"
        },
        {
            "question": "En TDD, ¿cuándo se escriben las pruebas?",
            "options": [
                "a) Después de terminar todo el código.",
                "b) Antes que el código.",
                "c) Mientras se está ejecutando el programa.",
                "d) Solo si hay errores."
            ],
            "answer": "b"
        },
        {
            "question": "¿Cuál es el último paso del ciclo TDD?",
            "options": [
                "a) Escribir la documentación.",
                "b) Refactorizar el código tan pronto como pasa las pruebas.",
                "c) Borrar las pruebas.",
                "d) Cambiar los requisitos del cliente."
            ],
            "answer": "b"
        },
        {
            "question": "¿Cuál es el riesgo de la refactorización en TDD?",
            "options": [
                "a) Que el código sea demasiado limpio.",
                "b) Cometer errores que hagan que la unidad deje de pasar las pruebas.",
                "c) Que las pruebas tarden mucho en ejecutarse.",
                "d) Que no se pueda documentar."
            ],
            "answer": "b"
        },
        {
            "question": "La herramienta de NetBeans 'Introducir método' sirve para:",
            "options": [
                "a) Escribir un método desde cero.",
                "b) Seleccionar código y reemplazarlo por la llamada a un nuevo método.",
                "c) Borrar un método existente.",
                "d) Cambiar los parámetros de un método."
            ],
            "answer": "b"
        },
        {
            "question": "¿Qué debe explicar la documentación principalmente?",
            "options": [
                "a) Exactamente lo que hace cada línea de código.",
                "b) Por qué se hace algo, no solo qué se hace.",
                "c) El nombre del programador en cada línea.",
                "d) Cuánto tiempo tardó en programarse."
            ],
            "answer": "b"
        },
        {
            "question": "¿Cuál de estos NO es un elemento que deba documentarse según el texto?",
            "options": [
                "a) Finalidad de una clase.",
                "b) Qué algoritmo se usa.",
                "c) El sueldo del programador.",
                "d) Qué se podría mejorar."
            ],
            "answer": "c"
        },
        {
            "question": "¿Cuáles son los dos propósitos de los comentarios?",
            "options": [
                "a) Adornar el código y ocultar errores.",
                "b) Explicar el objetivo de las sentencias y qué realiza un método/clase.",
                "c) Contar chistes y poner fechas.",
                "d) Sustituir al código y mejorar la velocidad."
            ],
            "answer": "b"
        },
        {
            "question": "¿Qué tipo de comentario se usa en Java para JavaDoc?",
            "options": [
                "a) // comentario",
                "b) /* comentario */",
                "c) /** comentario */",
                "d) # comentario"
            ],
            "answer": "c"
        },
        {
            "question": "¿Qué herramienta genera páginas HTML a partir de comentarios en el código?",
            "options": [
                "a) PMD",
                "b) JavaDoc",
                "c) CPD",
                "d) NetBeans"
            ],
            "answer": "b"
        },
        {
            "question": "¿Qué herramienta genera documentación con modelos de BD gráficos?",
            "options": [
                "a) JavaDoc",
                "b) SchemaSpy",
                "c) PMD",
                "d) TDD"
            ],
            "answer": "b"
        },
        {
            "question": "¿Con qué deben comenzar los comentarios de clase en JavaDoc?",
            "options": [
                "a) /*",
                "b) //",
                "c) /**",
                "d) <!--"
            ],
            "answer": "c"
        },
        {
            "question": "¿Qué etiqueta de JavaDoc es obligatoria para indicar el autor?",
            "options": [
                "a) @user",
                "b) @creator",
                "c) @author",
                "d) @name"
            ],
            "answer": "c"
        },
        {
            "question": "¿Qué indica la etiqueta @version en JavaDoc?",
            "options": [
                "a) La versión de Java utilizada.",
                "b) La versión del software y la fecha.",
                "c) El número de métodos de la clase.",
                "d) La versión del sistema operativo."
            ],
            "answer": "b"
        },
        {
            "question": "¿Para qué sirve la etiqueta @see?",
            "options": [
                "a) Para ver el código fuente.",
                "b) Para hacer referencia a otras clases o métodos.",
                "c) Para activar la cámara web.",
                "d) Para buscar errores visualmente."
            ],
            "answer": "b"
        },
        {
            "question": "¿Qué etiqueta describe los parámetros de un método?",
            "options": [
                "a) @arg",
                "b) @param",
                "c) @input",
                "d) @data"
            ],
            "answer": "b"
        },
        {
            "question": "¿Qué etiqueta describe el valor devuelto por un método?",
            "options": [
                "a) @out",
                "b) @return",
                "c) @result",
                "d) @value"
            ],
            "answer": "b"
        },
        {
            "question": "¿Qué etiquetas se usan para las excepciones que puede lanzar un método?",
            "options": [
                "a) @error y @fail",
                "b) @exception y @throws",
                "c) @catch y @try",
                "d) @alert y @warn"
            ],
            "answer": "b"
        },
        {
            "question": "¿Para qué niveles de acceso se genera habitualmente la documentación JavaDoc?",
            "options": [
                "a) Solo para private.",
                "b) Para public y protected.",
                "c) Solo para public.",
                "d) Para todos, incluyendo los locales."
            ],
            "answer": "b"
        },
        {
            "question": "¿Qué indica la etiqueta @since?",
            "options": [
                "a) El autor original.",
                "b) La fecha desde la que está presente el elemento.",
                "c) El tiempo que tarda en ejecutarse.",
                "d) El final del comentario."
            ],
            "answer": "b"
        },
        {
            "question": "¿Qué indica la etiqueta @deprecated?",
            "options": [
                "a) Que el método es nuevo.",
                "b) Que el método es obsoleto y no se recomienda su uso.",
                "c) Que el método tiene errores.",
                "d) Que el método es privado."
            ],
            "answer": "b"
        },
        {
            "question": "En la refactorización, ¿qué significa 'Extraer la interfaz'?",
            "options": [
                "a) Borrar una interfaz existente.",
                "b) Crear una nueva interfaz a partir de métodos seleccionados.",
                "c) Copiar el código de una interfaz a una clase.",
                "d) Cambiar el nombre de una interfaz."
            ],
            "answer": "b"
        },
        {
            "question": "¿Qué es un 'analizador estático'?",
            "options": [
                "a) Un programador que no se mueve.",
                "b) Un programa que evalúa el código sin ejecutarlo.",
                "c) Un hardware que mide la electricidad.",
                "d) Un tipo de virus informático."
            ],
            "answer": "b"
        },
        {
            "question": "La refactorización 'Sustituir bloques de código por un método' ayuda a:",
            "options": [
                "a) Hacer el código más largo.",
                "b) Evitar la duplicación y mejorar la legibilidad.",
                "c) Que el programa ocupe más memoria.",
                "d) Cambiar lo que hace el programa."
            ],
            "answer": "b"
        },
        {
            "question": "¿Cuál de estas NO es una limitación de la refactorización mencionada?",
            "options": [
                "a) Bases de datos.",
                "b) Cambios en interfaces públicas.",
                "c) El color del monitor del programador.",
                "d) Errores de diseño estructural importantes."
            ],
            "answer": "c"
        },
        {
            "question": "¿Qué herramienta de NetBeans genera automáticamente getters y setters?",
            "options": [
                "a) Renombrar.",
                "b) Encapsular campos.",
                "c) Mover clase.",
                "d) Borrado seguro."
            ],
            "answer": "b"
        },
        {
            "question": "¿Qué debe hacer el programador después de implementar la unidad en TDD?",
            "options": [
                "a) Borrar las pruebas.",
                "b) Refactorizar el código.",
                "c) Entregar el proyecto.",
                "d) Dejar de programar."
            ],
            "answer": "b"
        },
        {
            "question": "Los comentarios JavaDoc pueden ocupar:",
            "options": [
                "a) Solo una línea.",
                "b) Varias líneas.",
                "c) Máximo 10 palabras.",
                "d) Solo el final del archivo."
            ],
            "answer": "b"
        },
        {
            "question": "¿Qué herramienta es similar a JavaDoc y genera diagramas?",
            "options": [
                "a) Doxygen.",
                "b) Notepad.",
                "c) Calculator.",
                "d) Paint."
            ],
            "answer": "a"
        },
        {
            "question": "¿Qué sucede si renombramos un elemento con la herramienta de NetBeans?",
            "options": [
                "a) Solo cambia el nombre en ese archivo.",
                "b) Actualiza automáticamente todas las referencias en el proyecto.",
                "c) Borra el elemento por seguridad.",
                "d) Crea una copia del elemento."
            ],
            "answer": "b"
        },
        {
            "question": "La documentación es fundamental para:",
            "options": [
                "a) Que el código ocupe más espacio.",
                "b) La detección de errores y el mantenimiento posterior.",
                "c) Engañar al cliente.",
                "d) Que el programa no compile."
            ],
            "answer": "b"
        },
        {
            "question": "¿Cuál es el primer paso en el ciclo TDD?",
            "options": [
                "a) Programar las pruebas.",
                "b) Pensar qué pruebas debe pasar la unidad.",
                "c) Implementar la unidad.",
                "d) Refactorizar."
            ],
            "answer": "b"
        }
    ]

    print("="*60)
    print("TEST DE REPASO: TEMA 4 - OPTIMIZACIÓN Y DOCUMENTACIÓN")
    print("="*60)
    print(f"Se presentarán {len(questions)} preguntas. ¡Buena suerte!\n")

    score = 0
    random.shuffle(questions)

    for i, q in enumerate(questions):
        print(f"Pregunta {i+1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        while True:
            user_answer = input("Tu respuesta (a, b, c, d): ").lower().strip()
            if user_answer in ['a', 'b', 'c', 'd']:
                break
            print("Por favor, introduce una opción válida (a, b, c o d).")

        if user_answer == q['answer']:
            print("¡CORRECTO!\n")
            score += 1
        else:
            print(f"INCORRECTO. La respuesta correcta era la {q['answer']}.\n")

    print("="*60)
    print("TEST FINALIZADO")
    print(f"Puntuación final: {score}/{len(questions)} ({(score/len(questions))*100:.2f}%)")
    print("="*60)

if __name__ == "__main__":
    try:
        run_test()
    except KeyboardInterrupt:
        print("\n\nTest cancelado por el usuario. ¡Hasta luego!")
        sys.exit(0)
