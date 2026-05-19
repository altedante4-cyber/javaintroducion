#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Segundo test: 50 preguntas tipo test sobre Optimización y Documentación (Tema 4)
Con opciones mezcladas aleatoriamente en cada ejecución.
"""

import random

# Base de preguntas (enunciado + lista de opciones + índice de la correcta)
preguntas_base = [
    {
        "text": "¿Qué significa que la refactorización 'no cambia el comportamiento observable'?",
        "options": [
            "El software sigue cumpliendo la misma función que antes, ningún usuario nota el cambio",
            "El software se ejecuta más rápido",
            "Se modifican los mensajes de error visibles al usuario",
            "La interfaz de usuario cambia completamente"
        ],
        "correct_index": 0
    },
    {
        "text": "¿Cuándo NO es recomendable refactorizar según el texto?",
        "options": [
            "Cuando el código tiene código duplicado",
            "Cuando hay un error de diseño crítico o el código no funciona correctamente",
            "Cuando los nombres de variables no son significativos",
            "Cuando hay métodos demasiado largos"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Qué se debe hacer si nos encontramos con un código que no funciona, pero se podría refactorizar?",
        "options": [
            "Refactorizarlo inmediatamente antes de corregirlo",
            "Reescribirlo desde el principio",
            "Añadir más comentarios y luego refactorizar",
            "Dejarlo tal cual porque la refactorización no arregla errores"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Cuál es un problema específico de la refactorización en bases de datos?",
        "options": [
            "Las bases de datos no tienen estructura interna",
            "La gran cantidad de interdependencias hace que cualquier modificación sea muy costosa",
            "Las bases de datos no permiten cambios una vez creadas",
            "La refactorización de bases de datos no existe"
        ],
        "correct_index": 1
    },
    {
        "text": "Cuando refactorizamos y renombramos un método público, ¿qué problema puede surgir?",
        "options": [
            "El método dejará de funcionar",
            "Habrá que cambiar todas las referencias, y si es una interfaz pública se genera incompatibilidad",
            "El programa dejará de compilar para siempre",
            "No hay problema, es automático"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Qué solución se propone para mantener la compatibilidad al renombrar un método público?",
        "options": [
            "Eliminar el método antiguo inmediatamente",
            "Mantener las dos interfaces (la nueva y la vieja) temporalmente",
            "No cambiar nunca el nombre de métodos públicos",
            "Cambiar solo la documentación, no el código"
        ],
        "correct_index": 1
    },
    {
        "text": "Según el texto, ¿qué relación hay entre el análisis estático de código y la refactorización?",
        "options": [
            "El análisis estático ejecuta el código para probar la refactorización",
            "Los analizadores de código sugieren mejoras que pueden aplicarse mediante refactorización",
            "Son dos términos sinónimos",
            "La refactorización impide el análisis estático"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Qué tipo de análisis se realiza sobre el código fuente sin ejecutarlo?",
        "options": [
            "Análisis dinámico",
            "Análisis de rendimiento",
            "Análisis estático de código",
            "Análisis de seguridad en tiempo real"
        ],
        "correct_index": 2
    },
    {
        "text": "¿Cuál de las siguientes NO es una función típica de un analizador de código estático?",
        "options": [
            "Encontrar partes del código que reduzcan el rendimiento",
            "Detectar código con excesiva complejidad",
            "Compilar el código a lenguaje máquina",
            "Señalar posibles problemas de seguridad"
        ],
        "correct_index": 2
    },
    {
        "text": "PMD es una herramienta que se centra en:",
        "options": [
            "Gestionar versiones del código",
            "Detectar defectos de forma preventiva en el código fuente",
            "Generar documentación HTML",
            "Optimizar el rendimiento en tiempo de ejecución"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Qué tipo de problemas detecta PMD?",
        "options": [
            "Solo errores de sintaxis",
            "Posibles errores en tiempo de ejecución, código inalcanzable, expresiones simplificables, malos usos del lenguaje",
            "Únicamente código duplicado",
            "Problemas de conexión con la base de datos"
        ],
        "correct_index": 1
    },
    {
        "text": "En NetBeans, ¿cómo se activa el escaneado automático con PMD?",
        "options": [
            "No es posible, solo manual",
            "Desde Herramientas -> Opciones -> Varios -> PMD y marcando 'Enable Scan'",
            "Ejecutando un comando desde la terminal",
            "Reiniciando el IDE tres veces"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Qué propone el Desarrollo Guiado por Pruebas (TDD) respecto a las pruebas de unidad?",
        "options": [
            "Las pruebas las realiza un equipo independiente al final del desarrollo",
            "El programador escribe las pruebas antes de escribir el código a probar",
            "Las pruebas son opcionales",
            "Se escriben las pruebas después de tener el código funcionando"
        ],
        "correct_index": 1
    },
    {
        "text": "En TDD, ¿cuándo se refactoriza el código?",
        "options": [
            "Antes de escribir cualquier prueba",
            "Tan pronto como el código pasa las pruebas, para eliminar redundancia y mejorar claridad",
            "Solo al final del proyecto",
            "Nunca, TDD prohíbe la refactorización"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Qué es la 'cabeza' (head) en la gestión de versiones?",
        "options": [
            "La primera versión del tronco",
            "La última versión del tronco",
            "Una rama secundaria",
            "Un tipo de etiqueta"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Qué son las 'ramas' (branches) en un sistema de control de versiones?",
        "options": [
            "Las versiones principales del proyecto",
            "Variantes secundarias que permiten desarrollo paralelo sin afectar el tronco",
            "Los archivos de configuración",
            "Los comentarios del repositorio"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Qué es un 'delta' en el contexto de versiones?",
        "options": [
            "Una rama completa",
            "El cambio de una revisión respecto a la anterior",
            "El repositorio central",
            "La última versión estable"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Qué operación permite aplicar un cambio de una rama a otra?",
        "options": [
            "Checkout",
            "Merge (fusión)",
            "Commit",
            "Tag"
        ],
        "correct_index": 1
    },
    {
        "text": "La técnica de almacenamiento 'deltas inversos' consiste en:",
        "options": [
            "Guardar completa la primera versión y luego los cambios hacia adelante",
            "Guardar completa la última versión del tronco y los cambios necesarios para reconstruir versiones anteriores",
            "Guardar todas las versiones completas",
            "No guardar ningún cambio"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Qué es la 'marca selectiva' (selective marking) en almacenamiento de versiones?",
        "options": [
            "Guardar solo las versiones más recientes",
            "Almacenar el texto refundido de todas las versiones como secuencia lineal, marcando secciones con números de versión",
            "No almacenar código duplicado",
            "Comprimir todo el repositorio"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Qué elementos suele incluir una 'entrega' (release) de software?",
        "options": [
            "Solo los ejecutables",
            "Ejecutables, archivos de configuración, datos, instalador, documentación, embalaje y publicidad",
            "Únicamente el código fuente",
            "Solo la documentación del usuario"
        ],
        "correct_index": 1
    },
    {
        "text": "Según IEEE 828, la planificación de la Gestión de Configuraciones NO incluye:",
        "options": [
            "Introducción (propósito, alcance)",
            "Gestión de GCS (organización, responsabilidades)",
            "Código fuente de la aplicación",
            "Recursos GCS (herramientas, humanos)"
        ],
        "correct_index": 2
    },
    {
        "text": "En la Gestión de Configuraciones, la 'identificación' consiste en:",
        "options": [
            "Ocultar la configuración al equipo",
            "Establecer estándares de documentación y un esquema de identificación de documentos",
            "Realizar pruebas de software",
            "Controlar el acceso al repositorio"
        ],
        "correct_index": 1
    },
    {
        "text": "Las 'auditorías de configuraciones' sirven para:",
        "options": [
            "Aumentar el rendimiento del software",
            "Garantizar junto con revisiones técnicas que el cambio se ha implementado correctamente",
            "Eliminar versiones antiguas",
            "Generar informes automáticos de errores"
        ],
        "correct_index": 1
    },
    {
        "text": "El 'control formal' de cambios se realiza durante:",
        "options": [
            "La fase de desarrollo inicial",
            "La fase de pruebas unitarias",
            "La fase de mantenimiento, evaluado por un Comité de Control de Cambios",
            "La fase de diseño"
        ],
        "correct_index": 2
    },
    {
        "text": "¿Qué es el 'control individual' en la gestión del cambio?",
        "options": [
            "Un sistema automático sin revisión humana",
            "Cuando el programador responsable cambia la documentación sin generar documento formal",
            "Un control que requiere aprobación de todo el equipo",
            "El control realizado por un comité externo"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Qué herramienta de Microsoft se menciona como sustituta de SourceSafe?",
        "options": [
            "GitHub Desktop",
            "Visual Studio Team Foundation Server",
            "Azure DevOps",
            "TortoiseSVN"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Quién diseñó la herramienta de control de versiones Git?",
        "options": [
            "Richard Stallman",
            "Linus Torvalds",
            "Guido van Rossum",
            "Dennis Ritchie"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Qué característica destacada tiene Mercurial?",
        "options": [
            "Solo funciona en Windows",
            "Permite desarrollo distribuido, maneja texto y binarios, tiene interfaz web",
            "Es la herramienta más antigua",
            "No permite ramificación"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Qué entorno de trabajo de Gestión de Configuraciones integra ClearCase y ClearQuest?",
        "options": [
            "Entorno abierto",
            "Entorno integrado (por ejemplo, Rational Unified Process)",
            "Entorno basado en web",
            "Entorno cliente-servidor simple"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Qué es un comentario en el código fuente?",
        "options": [
            "Una instrucción que el compilador ejecuta",
            "Una anotación ignorada por el compilador que sirve para documentar el código",
            "Un error que impide la compilación",
            "Una variable especial del sistema"
        ],
        "correct_index": 1
    },
    {
        "text": "Según el texto, ¿qué dos propósitos principales tienen los comentarios?",
        "options": [
            "Mejorar el rendimiento y reducir el tamaño",
            "Explicar el objetivo de las sentencias y explicar qué realiza un método o clase (no cómo)",
            "Ocultar funcionalidad y encriptar el código",
            "Generar ejecutables más rápidos"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Cómo se escriben los comentarios de una sola línea en Java?",
        "options": [
            "/* comentario */",
            "// comentario",
            "<!-- comentario -->",
            "# comentario"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Qué herramienta de documentación genera también modelos gráficos de bases de datos y diagramas?",
        "options": [
            "JavaDoc",
            "Doxygen y SchemaSpy",
            "PMD",
            "CVS"
        ],
        "correct_index": 1
    },
    {
        "text": "En un comentario de clase JavaDoc, ¿qué etiqueta se usa para referenciar a otras clases o métodos?",
        "options": [
            "@link",
            "@see",
            "@ref",
            "@doc"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Qué etiqueta JavaDoc se utiliza para indicar la fecha desde la que una clase está presente?",
        "options": [
            "@version",
            "@since",
            "@date",
            "@created"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Qué etiqueta JavaDoc se emplea para indicar que un método es obsoleto?",
        "options": [
            "@obsolete",
            "@deprecated",
            "@old",
            "@remove"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Para qué sirve la etiqueta @throws en JavaDoc?",
        "options": [
            "Indicar el valor de retorno",
            "Especificar las excepciones que puede lanzar un método",
            "Documentar un parámetro",
            "Indicar la versión del método"
        ],
        "correct_index": 1
    },
    {
        "text": "Según el caso práctico, ¿quién se encarga de la Gestión de Configuraciones del Software?",
        "options": [
            "Juan",
            "María",
            "Ada",
            "Carlos"
        ],
        "correct_index": 2
    },
    {
        "text": "En el caso práctico, ¿qué herramienta de documentación deciden utilizar?",
        "options": [
            "Doxygen",
            "JavaDoc",
            "SchemaSpy",
            "PMD"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Qué dos miembros del equipo tienen menor experiencia y generan documentación automatizada?",
        "options": [
            "Juan y María",
            "Ada y Juan",
            "Carlos y Ana",
            "María y Carlos"
        ],
        "correct_index": 2
    },
    {
        "text": "¿Cuál es una ventaja del análisis automático de código frente al manual?",
        "options": [
            "Es más subjetivo",
            "Reduce la complejidad para detectar problemas base siguiendo reglas predefinidas",
            "Puede detectar errores de arquitectura",
            "No requiere configuración"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Cuál de los siguientes NO es un patrón de refactorización mencionado?",
        "options": [
            "Eliminar parámetros de un método",
            "Renombrado",
            "Extraer la interfaz",
            "Mover clase"
        ],
        "correct_index": 0
    },
    {
        "text": "¿Qué riesgo existe al refactorizar sin pruebas automatizadas?",
        "options": [
            "El código se vuelve más lento",
            "Se pueden introducir errores sin detectarlos fácilmente",
            "El código ocupa más memoria",
            "No hay riesgo, la refactorización es siempre segura"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Cómo ayuda la refactorización a encontrar errores?",
        "options": [
            "No ayuda, solo cambia estructura",
            "Al simplificar y clarificar el código, los errores se hacen más evidentes",
            "Genera informes automáticos de bugs",
            "Ejecuta pruebas de integración"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Qué es Subversion?",
        "options": [
            "Un analizador de código estático",
            "Un generador de documentación",
            "Un sistema de control de versiones, sucesor natural de CVS",
            "Un entorno de desarrollo integrado"
        ],
        "correct_index": 2
    },
    {
        "text": "¿Qué tipo de control de versiones permite hacer commits sin conexión (locales)?",
        "options": [
            "CVS",
            "Subversion",
            "Sistemas distribuidos como Darcs, Git o Mercurial",
            "SourceSafe"
        ],
        "correct_index": 2
    },
    {
        "text": "¿Qué se almacena en un repositorio de control de versiones?",
        "options": [
            "Solo el código fuente de la última versión",
            "Toda la información y datos de un proyecto, incluyendo el historial de versiones",
            "Solo los ejecutables",
            "Únicamente la documentación"
        ],
        "correct_index": 1
    },
    {
        "text": "¿Qué comando de CVS se usa para descartar cambios locales y volver a la versión del repositorio?",
        "options": [
            "Update",
            "Commit",
            "Checkout",
            "Abort"
        ],
        "correct_index": 3
    },
    {
        "text": "¿Qué etiqueta JavaDoc se usa para documentar una excepción en un método?",
        "options": [
            "@param",
            "@return",
            "@exception (o @throws)",
            "@see"
        ],
        "correct_index": 2
    }
]

def ejecutar_test():
    """Ejecuta el test con las preguntas mezcladas en orden y opciones aleatorias."""
    # Copiar y mezclar el orden de las preguntas
    preguntas = preguntas_base.copy()
    random.shuffle(preguntas)
    
    # Para cada pregunta, mezclar sus opciones
    for p in preguntas:
        opciones_con_indices = list(enumerate(p["options"]))
        random.shuffle(opciones_con_indices)
        nuevas_opciones = [opt for idx, opt in opciones_con_indices]
        nuevo_indice_correcto = next(i for i, (idx_orig, _) in enumerate(opciones_con_indices) if idx_orig == p["correct_index"])
        p["options"] = nuevas_opciones
        p["correct_index"] = nuevo_indice_correcto
    
    puntuacion = 0
    total = len(preguntas)
    
    print("=" * 70)
    print("SEGUNDO TEST: OPTIMIZACIÓN Y DOCUMENTACIÓN (TEMA 4)")
    print("50 nuevas preguntas. Responde A, B, C o D.")
    print("El orden de las opciones se ha mezclado aleatoriamente.")
    print("=" * 70)
    print()
    
    for idx, p in enumerate(preguntas, start=1):
        print(f"\nPregunta {idx} de {total}:")
        print(p["text"])
        letras = ["A", "B", "C", "D"]
        for i, opcion in enumerate(p["options"]):
            print(f"   {letras[i]}) {opcion}")
        
        respuesta = ""
        while respuesta not in letras:
            respuesta = input("Tu respuesta: ").strip().upper()
            if respuesta not in letras:
                print(f"Opción no válida. Escribe {', '.join(letras)}.")
        
        indice_respuesta = letras.index(respuesta)
        if indice_respuesta == p["correct_index"]:
            print("✓ Correcto.")
            puntuacion += 1
        else:
            letra_correcta = letras[p["correct_index"]]
            print(f"✗ Incorrecto. La respuesta correcta era {letra_correcta}.")
    
    print("\n" + "=" * 70)
    print(f"Test finalizado. Puntuación: {puntuacion} de {total} ({puntuacion*100/total:.1f}%)")
    if puntuacion == total:
        print("¡Excelente! Dominas completamente el tema.")
    elif puntuacion >= 40:
        print("Muy bien, solo algunos detalles por pulir.")
    elif puntuacion >= 30:
        print("Aprobado, pero revisa los conceptos más específicos.")
    else:
        print("Es recomendable que estudies más detenidamente el contenido.")
    print("=" * 70)

if __name__ == "__main__":
    ejecutar_test()
