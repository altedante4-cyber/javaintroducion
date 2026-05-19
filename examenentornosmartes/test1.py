#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script de 50 preguntas tipo test sobre Optimización y Documentación (Tema 4)
Basado en el contenido proporcionado.
"""

import sys

# Lista de preguntas: cada elemento es un diccionario con:
# 'text': enunciado, 'options': lista de opciones, 'correct': letra de la correcta (A, B, C, D)
preguntas = [
    {
        "text": "¿Qué es la refactorización de código?",
        "options": [
            "Un cambio que modifica el comportamiento del software para hacerlo más rápido",
            "Un cambio en la estructura interna del software para hacerlo más fácil de entender y modificar, sin cambiar su comportamiento",
            "Un proceso de optimización que busca mejorar el rendimiento a costa de la legibilidad",
            "La documentación automática del código fuente"
        ],
        "correct": "B"
    },
    {
        "text": "¿Cuál es el objetivo principal de la refactorización?",
        "options": [
            "Mejorar el rendimiento del programa",
            "Añadir nuevas funcionalidades",
            "Mejorar la estructura interna del código sin cambiar su comportamiento",
            "Eliminar todos los comentarios del código"
        ],
        "correct": "C"
    },
    {
        "text": "¿Qué diferencia fundamental hay entre refactorización y optimización?",
        "options": [
            "La refactorización mejora el rendimiento, la optimización mejora la estructura",
            "La optimización puede hacer el código más difícil de entender mientras que la refactorización busca mejorar la estructura interna",
            "No hay diferencia, son sinónimos",
            "La refactorización cambia el comportamiento observable, la optimización no"
        ],
        "correct": "B"
    },
    {
        "text": "¿Qué aspecto NO cambia durante una refactorización?",
        "options": [
            "La estructura interna del código",
            "El nombre de clases y métodos",
            "El comportamiento observable del software",
            "La organización de los métodos"
        ],
        "correct": "C"
    },
    {
        "text": "Según el texto, ¿cuál es un área problemática para la refactorización?",
        "options": [
            "Las interfaces gráficas",
            "Los bucles simples",
            "Las bases de datos",
            "Los métodos privados"
        ],
        "correct": "C"
    },
    {
        "text": "¿Qué se recomienda hacer cuando un código no funciona correctamente?",
        "options": [
            "Refactorizarlo inmediatamente",
            "Reescribirlo desde el principio",
            "Añadir más comentarios",
            "Optimizarlo primero"
        ],
        "correct": "B"
    },
    {
        "text": "¿En qué consiste el patrón de refactorización 'Renombrado' (rename)?",
        "options": [
            "Eliminar nombres que no se usan",
            "Cambiar el nombre de un paquete, clase, método o campo por uno más significativo",
            "Duplicar el nombre de los elementos para mayor claridad",
            "Intercambiar nombres entre dos métodos"
        ],
        "correct": "B"
    },
    {
        "text": "El patrón 'Sustituir bloques de código por un método' consiste en:",
        "options": [
            "Reemplazar un bloque de código repetido por una llamada a un nuevo método",
            "Eliminar todos los bloques de código y dejarlos vacíos",
            "Convertir cada línea de código en un método independiente",
            "Unir varios métodos en un solo bloque"
        ],
        "correct": "A"
    },
    {
        "text": "¿Qué aconseja el patrón 'Campos encapsulados'?",
        "options": [
            "Hacer todos los campos públicos",
            "Crear métodos getter y setter para cada campo de una clase",
            "Eliminar todos los campos de la clase",
            "Usar únicamente campos estáticos"
        ],
        "correct": "B"
    },
    {
        "text": "El patrón 'Mover la clase' permite:",
        "options": [
            "Eliminar una clase del proyecto",
            "Cambiar una clase de paquete o proyecto evitando duplicar código",
            "Renombrar una clase automáticamente",
            "Convertir una clase en interfaz"
        ],
        "correct": "B"
    },
    {
        "text": "¿Qué garantiza el patrón de 'Borrado seguro'?",
        "options": [
            "Que se eliminan todas las referencias a un elemento del código que ya no es necesario",
            "Que se borran los comentarios obsoletos",
            "Que se eliminan las versiones antiguas del repositorio",
            "Que se borran los archivos temporales"
        ],
        "correct": "A"
    },
    {
        "text": "¿Qué permite el patrón 'Cambiar los parámetros del proyecto'?",
        "options": [
            "Modificar solo el nombre del proyecto",
            "Añadir nuevos parámetros a un método y cambiar los modificadores de acceso",
            "Eliminar todos los parámetros de los métodos",
            "Cambiar el tipo de retorno de todos los métodos"
        ],
        "correct": "B"
    },
    {
        "text": "¿En qué consiste 'Extraer la interfaz' como patrón de refactorización?",
        "options": [
            "Eliminar una interfaz existente",
            "Crear una nueva interfaz a partir de métodos public non-static seleccionados de una clase o interfaz",
            "Convertir una clase en interfaz",
            "Unir dos interfaces en una"
        ],
        "correct": "B"
    },
    {
        "text": "El patrón 'Mover del interior a otro nivel' se refiere a:",
        "options": [
            "Mover una clase interna a un nivel superior en la jerarquía",
            "Mover un método de una clase a otra",
            "Mover un paquete a otro proyecto",
            "Mover un atributo de instancia a estático"
        ],
        "correct": "A"
    },
    {
        "text": "¿Qué son los analizadores de código estático?",
        "options": [
            "Herramientas que ejecutan el código para medir su rendimiento",
            "Herramientas que evalúan el software sin llegar a ejecutarlo, directamente sobre el código fuente",
            "Programas que traducen el código a otro lenguaje",
            "Editores de código con resaltado de sintaxis"
        ],
        "correct": "B"
    },
    {
        "text": "¿Cuál es la función principal de la herramienta PMD?",
        "options": [
            "Compilar código Java",
            "Detectar patrones que pueden ser errores en tiempo de ejecución, código inalcanzable, código optimizable, etc.",
            "Gestionar versiones del código",
            "Documentar automáticamente el código"
        ],
        "correct": "B"
    },
    {
        "text": "¿Qué hace la herramienta CPD (Copy-Paste Detector)?",
        "options": [
            "Detectar comentarios mal escritos",
            "Encontrar código duplicado",
            "Medir la complejidad ciclomática",
            "Generar diagramas de clases"
        ],
        "correct": "B"
    },
    {
        "text": "En NetBeans, ¿cómo se ejecuta PMD sobre un proyecto?",
        "options": [
            "Desde el menú Ejecutar -> Analizar",
            "Pulsando botón derecho sobre el directorio -> Herramientas -> Ejecutar PMD",
            "Mediante la línea de comandos únicamente",
            "No se puede ejecutar PMD en NetBeans"
        ],
        "correct": "B"
    },
    {
        "text": "¿Qué propone el Desarrollo Guiado por Pruebas (TDD) en relación con la refactorización?",
        "options": [
            "Refactorizar antes de escribir las pruebas",
            "Refactorizar el código tan pronto como pasa las pruebas para eliminar redundancia y hacerlo más claro",
            "No refactorizar nunca el código probado",
            "Refactorizar solo al final del proyecto"
        ],
        "correct": "B"
    },
    {
        "text": "¿Qué herramienta de ayuda a la refactorización incluye NetBeans?",
        "options": [
            "Un depurador de memoria",
            "Funciones integradas como Renombrar, Introducir método, Encapsular campos, etc.",
            "Un compilador específico para refactorización",
            "Un gestor de bases de datos"
        ],
        "correct": "B"
    },
    {
        "text": "¿Qué es una 'versión' en el contexto del control de versiones?",
        "options": [
            "Un error en el software",
            "La evolución de un único elemento dentro de un sistema en desarrollo",
            "La documentación asociada a un programa",
            "El conjunto de todos los archivos de un proyecto"
        ],
        "correct": "B"
    },
    {
        "text": "¿Cuál es una ventaja de utilizar un sistema de control de versiones?",
        "options": [
            "Permite que varios desarrolladores trabajen en el mismo proyecto de forma simultánea sin pisarse",
            "Aumenta la velocidad de ejecución del programa",
            "Elimina la necesidad de hacer pruebas",
            "Genera automáticamente la documentación"
        ],
        "correct": "A"
    },
    {
        "text": "¿Qué arquitectura utiliza CVS?",
        "options": [
            "Arquitectura monolítica",
            "Arquitectura peer-to-peer",
            "Arquitectura cliente-servidor",
            "Arquitectura de capas"
        ],
        "correct": "C"
    },
    {
        "text": "¿Qué es el repositorio en un sistema de control de versiones?",
        "options": [
            "La copia local del desarrollador",
            "El lugar central donde se almacenan los datos de los proyectos y su historial",
            "El archivo de configuración del proyecto",
            "El directorio donde se guardan los ejecutables"
        ],
        "correct": "B"
    },
    {
        "text": "En CVS, ¿qué es un 'módulo'?",
        "options": [
            "Un complemento del IDE",
            "Un directorio específico del repositorio que puede identificar una parte del proyecto o el proyecto completo",
            "Una rama del desarrollo",
            "Una etiqueta de versión"
        ],
        "correct": "B"
    },
    {
        "text": "¿Qué representa una 'revisión' en control de versiones?",
        "options": [
            "El nombre del autor del cambio",
            "Cada una de las versiones parciales o cambios en los archivos o en el repositorio completo",
            "La fecha de la última modificación",
            "Un comentario asociado al cambio"
        ],
        "correct": "B"
    },
    {
        "text": "¿Qué es una 'etiqueta' (tag) en un sistema de control de versiones?",
        "options": [
            "Un error marcado por el compilador",
            "Información textual que se añade a un conjunto de archivos para indicar información importante (por ejemplo una versión release)",
            "Un tipo de rama",
            "Un comando para eliminar archivos"
        ],
        "correct": "B"
    },
    {
        "text": "¿Qué es una 'rama' (branch) en control de versiones?",
        "options": [
            "La versión principal del proyecto",
            "Revisiones paralelas de un módulo para efectuar cambios sin afectar la evolución principal",
            "El historial completo de cambios",
            "Una copia de seguridad del repositorio"
        ],
        "correct": "B"
    },
    {
        "text": "¿Qué hace el comando 'checkout' en CVS?",
        "options": [
            "Actualiza la copia local con los cambios del repositorio",
            "Guarda los cambios locales en el repositorio",
            "Obtiene una copia del trabajo para poder trabajar con ella",
            "Aborta los cambios locales"
        ],
        "correct": "C"
    },
    {
        "text": "¿Qué hace el comando 'commit' en un sistema de control de versiones?",
        "options": [
            "Descarta los cambios locales",
            "Actualiza la copia local",
            "Almacena la copia modificada en el repositorio",
            "Crea una nueva rama"
        ],
        "correct": "C"
    },
    {
        "text": "¿Qué hace el comando 'update' en un sistema de control de versiones?",
        "options": [
            "Guarda los cambios en el repositorio",
            "Actualiza la copia local con cambios recientes del repositorio",
            "Elimina la copia local",
            "Crea una nueva versión"
        ],
        "correct": "B"
    },
    {
        "text": "¿Cuál de las siguientes herramientas NO es una herramienta de control de versiones?",
        "options": [
            "Subversion",
            "CVS",
            "Mercurial",
            "PMD"
        ],
        "correct": "D"
    },
    {
        "text": "¿Qué estándar regula la planificación de la Gestión de Configuraciones del Software?",
        "options": [
            "ISO 9001",
            "IEEE 828",
            "IEEE 802.11",
            "ISO 27001"
        ],
        "correct": "B"
    },
    {
        "text": "¿Cuáles son las cuatro tareas básicas de la Gestión de Configuraciones de Software?",
        "options": [
            "Diseño, implementación, pruebas, mantenimiento",
            "Identificación, control de cambios, auditorías de configuraciones, generación de informes",
            "Análisis, codificación, documentación, despliegue",
            "Planificación, desarrollo, verificación, validación"
        ],
        "correct": "B"
    },
    {
        "text": "Según el texto, ¿cuál NO es una tarea básica de la Gestión de Configuraciones de Software?",
        "options": [
            "Control de cambios",
            "Generación de informes",
            "Gestión del repositorio",
            "Auditorías de configuraciones"
        ],
        "correct": "C"
    },
    {
        "text": "¿Qué tipo de control de cambios ocurre durante la fase de mantenimiento y requiere evaluación por un Comité de Control de Cambios?",
        "options": [
            "Control individual",
            "Control de gestión",
            "Control formal",
            "Control automatizado"
        ],
        "correct": "C"
    },
    {
        "text": "En el grafo de evolución de versiones, ¿cómo se denomina la variante principal?",
        "options": [
            "Rama (branch)",
            "Cabeza (head)",
            "Tronco (trunk)",
            "Delta"
        ],
        "correct": "C"
    },
    {
        "text": "¿Qué técnica de almacenamiento guarda completa la primera versión y luego los cambios mínimos para reconstruir cada nueva versión a partir de la anterior?",
        "options": [
            "Deltas inversos",
            "Deltas directos",
            "Marcado selectivo",
            "Compresión incremental"
        ],
        "correct": "B"
    },
    {
        "text": "¿Qué es una 'entrega' en el contexto de la gestión de versiones?",
        "options": [
            "Una copia de trabajo del desarrollador",
            "Una instancia de un sistema que se distribuye a los usuarios externos al equipo de desarrollo",
            "La última versión del tronco",
            "Un cambio solicitado por el cliente"
        ],
        "correct": "B"
    },
    {
        "text": "¿Qué herramienta CASE de código abierto se menciona para la gestión de cambios (bug-tracking)?",
        "options": [
            "Jira",
            "Bugzilla",
            "Redmine",
            "Trac"
        ],
        "correct": "B"
    },
    {
        "text": "¿Qué clientes de control de versiones están integrados o disponibles como plug-in en entornos como NetBeans?",
        "options": [
            "CVS, Subversion, Mercurial",
            "SourceSafe, Team Foundation Server, Git",
            "PMD, CPD, FindBugs",
            "JavaDoc, Doxygen, SchemaSpy"
        ],
        "correct": "A"
    },
    {
        "text": "¿Qué cliente de gestión de versiones NO incorpora NetBeans según el texto?",
        "options": [
            "CVS",
            "Subversion",
            "Mercurial",
            "Visual Studio Team Foundation"
        ],
        "correct": "D"
    },
    {
        "text": "¿Para qué sirve documentar el código fuente?",
        "options": [
            "Para que el compilador genere mejores ejecutables",
            "Para explicar su funcionamiento, facilitar la detección de errores y el mantenimiento posterior",
            "Para aumentar el tamaño del programa",
            "Para ocultar la lógica del programa"
        ],
        "correct": "B"
    },
    {
        "text": "¿Cuál es la sintaxis correcta para un comentario JavaDoc en Java?",
        "options": [
            "// comentario",
            "/* comentario */",
            "/** comentario */",
            "<!-- comentario -->"
        ],
        "correct": "C"
    },
    {
        "text": "¿Qué etiqueta JavaDoc se utiliza para indicar el autor de una clase?",
        "options": [
            "@version",
            "@param",
            "@return",
            "@author"
        ],
        "correct": "D"
    },
    {
        "text": "¿Qué etiqueta JavaDoc se utiliza para indicar la versión de una clase?",
        "options": [
            "@version",
            "@author",
            "@since",
            "@see"
        ],
        "correct": "A"
    },
    {
        "text": "¿Qué etiqueta JavaDoc se emplea para describir los parámetros de un método?",
        "options": [
            "@return",
            "@param",
            "@throws",
            "@exception"
        ],
        "correct": "B"
    },
    {
        "text": "¿Qué etiqueta JavaDoc se usa para describir el valor devuelto por un método?",
        "options": [
            "@param",
            "@return",
            "@throws",
            "@deprecated"
        ],
        "correct": "B"
    },
    {
        "text": "¿Qué herramienta genera páginas HTML de documentación a partir de los comentarios incluidos en el código fuente Java?",
        "options": [
            "PMD",
            "CPD",
            "JavaDoc",
            "Doxygen"
        ],
        "correct": "C"
    },
    {
        "text": "¿Qué tipo de comentario es el que comienza con /** y termina con */?",
        "options": [
            "Comentario de una línea",
            "Comentario de bloque normal",
            "Comentario JavaDoc",
            "Comentario de depuración"
        ],
        "correct": "C"
    }
]

def ejecutar_test():
    """Ejecuta el test de 50 preguntas."""
    puntuacion = 0
    total = len(preguntas)
    
    print("=" * 70)
    print("TEST DE OPTIMIZACIÓN Y DOCUMENTACIÓN (TEMA 4)")
    print("Responde A, B, C o D (no sensible a mayúsculas).")
    print("=" * 70)
    print()
    
    for idx, p in enumerate(preguntas, start=1):
        print(f"\nPregunta {idx} de {total}:")
        print(p["text"])
        for letra, opcion in zip(["A", "B", "C", "D"], p["options"]):
            print(f"   {letra}) {opcion}")
        
        respuesta = ""
        while respuesta not in ["A", "B", "C", "D"]:
            respuesta = input("Tu respuesta: ").strip().upper()
            if respuesta not in ["A", "B", "C", "D"]:
                print("Opción no válida. Escribe A, B, C o D.")
        
        if respuesta == p["correct"]:
            print("✓ Correcto.")
            puntuacion += 1
        else:
            print(f"✗ Incorrecto. La respuesta correcta era {p['correct']}.")
    
    print("\n" + "=" * 70)
    print(f"Test finalizado. Puntuación: {puntuacion} de {total} ({puntuacion*100/total:.1f}%)")
    if puntuacion == total:
        print("¡Perfecto! Dominas el tema.")
    elif puntuacion >= 40:
        print("Muy bien, pero revisa algún concepto.")
    elif puntuacion >= 30:
        print("Aprobado, pero te falta repasar.")
    else:
        print("Es recomendable que estudies más el contenido.")
    print("=" * 70)

if __name__ == "__main__":
    ejecutar_test()
