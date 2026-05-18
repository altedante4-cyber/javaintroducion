import random

preguntas_ejercicios = [
    {
        "pregunta": "¿Qué cmdlet se usa para descubrir comandos relacionados con procesos?",
        "opciones": ["Get-Command -Noun Process", "Get-Process -Noun", "Find-Command Process", "Search-Command Process", "Get-Item Process"],
        "correcta": 0
    },
    {
        "pregunta": "¿Cuál es el alias de Set-Location?",
        "opciones": ["sl", "pwd", "gl", "ls", "dir"],
        "correcta": 0
    },
    {
        "pregunta": "¿Qué cmdlet permite ver propiedades y métodos de objetos?",
        "opciones": ["Get-Object", "Get-Member", "Show-Object", "Get-Property", "Get-Info"],
        "correcta": 1
    },
    {
        "pregunta": "¿Cómo se filtra un objeto en PowerShell?",
        "opciones": ["Select-Object", "Filter-Object", "Where-Object", "Find-Object", "Search-Object"],
        "correcta": 2
    },
    {
        "pregunta": "¿Qué parámetro de Copy-Item permite incluir subcarpetas?",
        "opciones": ["-Force", "-IncludeSubfolders", "-Deep", "-Recurse", "-All"],
        "correcta": 3
    },
    {
        "pregunta": "¿Qué cmdlet devuelve la fecha y hora actual?",
        "opciones": ["Get-Time", "Get-Date", "Get-Now", "Get-Current", "Get-Day"],
        "correcta": 1
    },
    {
        "pregunta": "¿Cómo se escribe salida que NO va al pipeline?",
        "opciones": ["Write-Output", "Write-Information", "Write-Host", "Write-Debug", "Write-Verbose"],
        "correcta": 2
    },
    {
        "pregunta": "¿Qué formato de salida visualiza una única propiedad?",
        "opciones": ["Format-List", "Format-Table", "Format-Custom", "Format-Wide", "Format-Grid"],
        "correcta": 3
    },
    {
        "pregunta": "¿Qué cmdlet se usa para crear archivos o carpetas?",
        "opciones": ["Create-Item", "Add-Item", "New-Item", "Make-Item", "Build-Item"],
        "correcta": 2
    },
    {
        "pregunta": "¿Cuál es la sintaxis correcta para obtener ayuda detallada de Get-Process?",
        "opciones": ["Get-Help Get-Process", "Get-Help Get-Process -Detailed", "Help Get-Process -Full", "Get-Help -Name Get-Process -Deep", "Get-Help Get-Process -All"],
        "correcta": 1
    },
    {
        "pregunta": "¿Qué variable automática representa el objeto actual en el pipeline?",
        "opciones": ["$this", "$it", "$_", "$PSItem", "$object"],
        "correcta": 2
    },
    {
        "pregunta": "¿Qué operador de comparación significa 'mayor o igual que'?",
        "opciones": ["-gt", "-ge", "-le", "-ne", "-eq"],
        "correcta": 1
    },
    {
        "pregunta": "¿Qué cmdlet permite ordenar objetos del pipeline?",
        "opciones": ["Order-Object", "Sort-Object", "Arrange-Object", "Sort-List", "Order-List"],
        "correcta": 1
    },
    {
        "pregunta": "¿Cómo se obtiene solo el día del mes con Get-Date?",
        "opciones": ["Get-Date -Day", "(Get-Date).Day", "Get-Date | Select Day", "Get-Date.Day", "Get-Day"],
        "correcta": 1
    },
    {
        "pregunta": "¿Qué cmdlet obtiene los usuarios locales del sistema?",
        "opciones": ["Get-User", "Get-LocalUser", "Get-Users", "Get-Account", "Get-SystemUser"],
        "correcta": 1
    },
    {
        "pregunta": "¿Para qué sirve Select-Object?",
        "opciones": ["Filtrar objetos", "Ordenar objetos", "Seleccionar propiedades específicas", "Agrupar objetos", "Contar objetos"],
        "correcta": 2
    },
    {
        "pregunta": "¿Qué hace el parámetro -Force en Remove-Item?",
        "opciones": ["Acelerar la eliminación", "Eliminar archivos de solo lectura", "Forzar eliminación sin preguntar", "Ocultar el progreso", "Deshacer la eliminación"],
        "correcta": 2
    },
    {
        "pregunta": "¿Qué formato de salida permite agrupar por valor de una propiedad?",
        "opciones": ["Format-List -GroupBy", "Format-Table -GroupBy", "Format-Wide -GroupBy", "Format-Custom -GroupBy", "Format-Group -Property"],
        "correcta": 1
    },
    {
        "pregunta": "¿Cómo se añade un usuario a un grupo local?",
        "opciones": ["Add-UserToGroup", "Add-LocalGroupMember", "New-LocalGroupMember", "Set-LocalGroupMember", "Add-GroupMember"],
        "correcta": 1
    },
    {
        "pregunta": "¿Qué cmdlet se usa para leer entrada del usuario?",
        "opciones": ["Read-Input", "Get-Input", "Read-Host", "Get-Host", "Input-Host"],
        "correcta": 2
    },
    {
        "pregunta": "¿Cómo se cuentan los procesos en el sistema?",
        "opciones": ["(Get-Process).Length", "(Get-Process).Count", "Get-Process | Count-Object", "Measure-Process", "Get-Process -Count"],
        "correcta": 1
    },
    {
        "pregunta": "¿Qué cmdlet lista servicios del sistema?",
        "opciones": ["Get-Process", "Get-Service", "Get-System", "Get-Task", "Get-Running"],
        "correcta": 1
    },
    {
        "pregunta": "¿Qué hace Format-List?",
        "opciones": ["Muestra en tabla", "Muestra en lista vertical", "Muestra en cuadrícula", "Muestra en ancho completo", "Muestra en columnas"],
        "correcta": 1
    },
    {
        "pregunta": "¿Cuál es la sintaxis para añadir 4 días a la fecha actual?",
        "opciones": ["(Get-Date).Add(4)", "(Get-Date).AddDays(4)", "Get-Date + 4", "Add-Date -Days 4", "(Get-Date).PlusDays(4)"],
        "correcta": 1
    },
    {
        "pregunta": "¿Qué hace el comando Get-Command -CommandType Alias?",
        "opciones": ["Muestra solo alias", "Muestra solo cmdlets", "Muestra solo funciones", "Crea un alias nuevo", "Elimina alias"],
        "correcta": 0
    }
]

preguntas_bucles = [
    {
        "pregunta": "¿Cuál es el alias de ForEach-Object?",
        "opciones": ["fo", "fe", "%", "&", "#"],
        "correcta": 2
    },
    {
        "pregunta": "¿Qué sintaxis es correcta para un bucle for en PowerShell?",
        "opciones": ["for ($i=0; $i -lt 10; $i++) { }", "for ($i=0, $i<10, $i++) { }", "for $i=0 to 10 { }", "loop ($i=0; $i<10; $i++) { }", "foreach $i in 0..10 { }"],
        "correcta": 0
    },
    {
        "pregunta": "¿Qué bucle se ejecuta al menos una vez?",
        "opciones": ["for", "foreach", "do-while", "while", "for ($i=0; $i -lt 10; $i++)"],
        "correcta": 2
    },
    {
        "pregunta": "¿Cómo se recorre un array con ForEach-Object en el pipeline?",
        "opciones": ["$array | ForEach-Object { $_.Name }", "$array | ForEach { $it.Name }", "$array | Each-Object { $_.Name }", "ForEach-Object -Array $array { $_.Name }", "$array | Loop-Object { $_.Name }"],
        "correcta": 0
    },
    {
        "pregunta": "¿Qué hace 'break' dentro de un bucle?",
        "opciones": ["Salta a la siguiente iteración", "Sale del bucle inmediatamente", "Reinicia el bucle", "Pausa el bucle", "Invierte el orden del bucle"],
        "correcta": 1
    },
    {
        "pregunta": "¿Qué hace 'continue' dentro de un bucle?",
        "opciones": ["Sale del bucle", "Reinicia el bucle desde el principio", "Salta a la siguiente iteración", "Pausa la ejecución", "Duplica la iteración actual"],
        "correcta": 2
    },
    {
        "pregunta": "¿Qué sintaxis es correcta para un bucle foreach?",
        "opciones": ["foreach ($item in $coleccion) { }", "foreach $item = $coleccion { }", "foreach ($item : $coleccion) { }", "foreach $item <- $coleccion { }", "foreach $item en $coleccion { }"],
        "correcta": 0
    },
    {
        "pregunta": "¿Cómo se itera sobre cada objeto en el pipeline?",
        "opciones": ["ForEach-Object { $_ }", "ForEach-Object { $this }", "ForEach-Object { $item }", "ForEach-Object { $PSItem }", "ForEach-Object { $current }"],
        "correcta": 0
    },
    {
        "pregunta": "¿Cuándo se usa un bucle while?",
        "opciones": ["Siempre se ejecuta al menos una vez", "Se ejecuta mientras la condición sea verdadera", "Itera sobre elementos de una colección", "Se ejecuta un número fijo de veces", "Se ejecuta hasta que se cumple una condición"],
        "correcta": 1
    },
    {
        "pregunta": "¿Qué diferencia hay entre while y do-while?",
        "opciones": ["Ninguna", "do-while ejecuta el bloque antes de evaluar la condición", "while se ejecuta más rápido", "do-while solo funciona con números", "while no puede usar operadores de comparación"],
        "correcta": 1
    },
    {
        "pregunta": "¿Cómo se itera sobre números del 1 al 10?",
        "opciones": ["1..10 | ForEach-Object { $_ }", "For ($i=0; $i -lt 10) { }", "foreach $i in 1-10 { }", "while ($i -le 10) { }", "1-10 | ForEach { $it }"],
        "correcta": 0
    },
    {
        "pregunta": "¿Qué ocurre si la condición de un while es falsa desde el inicio?",
        "opciones": ["Da error de sintaxis", "El bucle no se ejecuta ninguna vez", "El bucle se ejecuta una vez", "El bucle se ejecuta infinitamente", "PowerShell lanza una excepción"],
        "correcta": 1
    },
    {
        "pregunta": "¿Qué sintaxis permite recorrer un array de procesos y mostrar su nombre?",
        "opciones": ["Get-Process | ForEach { $_.Name }", "Get-Process | ForEach-Object { $this.Name }", "Get-Process | ForEach-Object { Name }", "ForEach-Object -InputObject (Get-Process) { Name }", "Get-Process | While { $_.Name }"],
        "correcta": 0
    },
    {
        "pregunta": "¿Cómo se sale de un bucle for antes de tiempo?",
        "opciones": ["exit", "stop", "break", "end", "return"],
        "correcta": 2
    },
    {
        "pregunta": "¿Qué hace el siguiente código? for ($i=0; $i -lt 5; $i++) { Write-Host $i }",
        "opciones": ["Imprime 0,1,2,3,4", "Imprime 1,2,3,4,5", "Imprime 0,1,2,3,4,5", "Imprime 1,2,3,4", "Imprime 0,1,2,3,4,5,6"],
        "correcta": 0
    },
    {
        "pregunta": "¿Qué bucle es más adecuado para recorrer colecciones de objetos?",
        "opciones": ["while", "do-while", "for", "foreach", "if-else"],
        "correcta": 3
    },
    {
        "pregunta": "¿Cómo se crea un bucle infinito en PowerShell?",
        "opciones": ["while (1) { }", "while ($true) { }", "for (;;) { }", "do { } while ($true)", "Todas son correctas"],
        "correcta": 4
    },
    {
        "pregunta": "¿Cuál es la estructura de un bucle for?",
        "opciones": ["for (inicialización; condición; incremento)", "for (condición; inicialización; incremento)", "for (inicialización; incremento; condición)", "for (incremento; condición; inicialización)", "for (inicialización, condición, incremento)"],
        "correcta": 0
    },
    {
        "pregunta": "¿Qué parámetro de ForEach-Object permite ejecutar código al inicio?",
        "opciones": ["-Begin", "-Start", "-Init", "-First", "-Setup"],
        "correcta": 0
    },
    {
        "pregunta": "¿Qué parámetro de ForEach-Object permite ejecutar código al final?",
        "opciones": ["-Final", "-End", "-Finish", "-Last", "-Close"],
        "correcta": 1
    },
    {
        "pregunta": "¿Cómo se recorre un array multidimensional con bucles anidados?",
        "opciones": ["Usando un solo bucle for", "Usando bucles for anidados (uno dentro de otro)", "No se puede en PowerShell", "Usando foreach con índice", "Usando while con contador"],
        "correcta": 1
    },
    {
        "pregunta": "¿Qué operador se usa para comparar dentro de un while?",
        "opciones": ["==", "=", "-eq", "equals", "is"],
        "correcta": 2
    },
    {
        "pregunta": "¿Cuál es el resultado de: foreach ($i in 1..3) { Write-Host ($i * 2) }",
        "opciones": ["1,2,3", "2,4,6", "2,3,4", "1,4,9", "3,6,9"],
        "correcta": 1
    },
    {
        "pregunta": "¿Cómo se evita un bucle infinito?",
        "opciones": ["Usando break", "Asegurando que la condición termine siendo falsa", "Usando continue", "Usando exit", "Todas son formas válidas"],
        "correcta": 4
    },
    {
        "pregunta": "¿Qué hace 'continue' en un bucle for?",
        "opciones": ["Sale del bucle for", "Vuelve a la condición del for", "Reinicia la variable del contador", "Sale del script", "Detiene la ejecución"],
        "correcta": 1
    }
]

def hacer_examen():
    random.shuffle(preguntas_ejercicios)
    random.shuffle(preguntas_bucles)

    todas = preguntas_ejercicios[:25] + preguntas_bucles[:25]
    random.shuffle(todas)

    correctas = 0
    total = len(todas)

    print("=" * 60)
    print("EXAMEN DE POWERSHELL - 50 PREGUNTAS")
    print("=" * 60)

    for idx, p in enumerate(todas, 1):
        print(f"\nPregunta {idx}: {p['pregunta']}")
        for letra in range(5):
            print(f"  {'ABCDE'[letra]}) {p['opciones'][letra]}")

        while True:
            resp = input("\nTu respuesta (A, B, C, D, E): ").strip().upper()
            if resp in "ABCDE":
                respuesta_idx = "ABCDE".index(resp)
                break
            print("Respuesta no válida. Elige A, B, C, D o E.")

        if respuesta_idx == p["correcta"]:
            print("  CORRECTO!")
            correctas += 1
        else:
            print(f"  INCORRECTO. La respuesta correcta era {chr(65 + p['correcta'])}")

    print("\n" + "=" * 60)
    print("RESULTADOS")
    print("=" * 60)
    print(f"Total preguntas: {total}")
    print(f"Correctas: {correctas}")
    print(f"Incorrectas: {total - correctas}")
    nota = round((correctas / total) * 10, 1)
    print(f"Nota: {nota}/10")
    if nota >= 5:
        print("APROBADO!")
    else:
        print("SUSPENSO")

if __name__ == "__main__":
    hacer_examen()
