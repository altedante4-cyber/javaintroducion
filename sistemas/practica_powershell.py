import random

ejercicios_logica = [
    {
        "pregunta": "¿Qué imprime este código?\n\nGet-Process | Where-Object { $_.CPU -gt 100 } | ForEach-Object { $_.Name }",
        "opciones": [
            "Todos los procesos",
            "Los nombres de procesos con CPU > 100",
            "Los procesos ordenados por CPU",
            "Los 100 procesos con más CPU",
            "Da error de sintaxis"
        ],
        "correcta": 1,
        "explicacion": "Where-Object filtra procesos con CPU > 100, ForEach-Object extrae solo el nombre."
    },
    {
        "pregunta": "¿Qué hace este código?\n\n1..5 | ForEach-Object { $_ * $_ }",
        "opciones": [
            "Imprime 1,2,3,4,5",
            "Imprime 1,4,9,16,25 (cuadrados)",
            "Imprime 2,4,6,8,10",
            "Imprime 5,10,15,20,25",
            "Da error porque $_ no es un número"
        ],
        "correcta": 1,
        "explicacion": "1..5 genera los números, ForEach-Object multiplica cada uno por sí mismo (cuadrado)."
    },
    {
        "pregunta": "¿Cuál es el resultado de?\n\n$suma = 0\n1..10 | ForEach-Object { $suma += $_ }\nWrite-Host $suma",
        "opciones": ["10", "55", "100", "45", "11"],
        "correcta": 1,
        "explicacion": "Suma los números del 1 al 10 = 55."
    },
    {
        "pregunta": "¿Qué hace?\n\nGet-ChildItem -File | Where-Object { $_.Length -gt 1MB } | ForEach-Object { $_.Name }",
        "opciones": [
            "Lista todos los archivos",
            "Lista archivos mayores de 1MB mostrando solo el nombre",
            "Elimina archivos mayores de 1MB",
            "Cuenta archivos mayores de 1MB",
            "Muestra el tamaño total de archivos"
        ],
        "correcta": 1,
        "explicacion": "Filtra archivos > 1MB y extrae solo el nombre con ForEach-Object."
    },
    {
        "pregunta": "¿Qué imprime?\n\nforeach ($i in 1..3) {\n    foreach ($j in 1..2) {\n        Write-Host ($i * $j)\n    }\n}",
        "opciones": [
            "1,2,3,1,2,3",
            "1,2,2,4,3,6",
            "1,2,3,4,5,6",
            "1,2,3",
            "1,1,2,2,3,3"
        ],
        "correcta": 1,
        "explicacion": "Bucles anidados: 1*1=1, 1*2=2, 2*1=2, 2*2=4, 3*1=3, 3*2=6."
    },
    {
        "pregunta": "¿Qué hace este código?\n\nGet-Service | Where-Object { $_.Status -eq 'Running' } | ForEach-Object { $_.Name }",
        "opciones": [
            "Lista todos los servicios",
            "Detiene los servicios en ejecución",
            "Muestra el nombre de servicios en ejecución",
            "Inicia servicios detenidos",
            "Cuenta los servicios"
        ],
        "correcta": 2,
        "explicacion": "Filtra servicios Running y extrae solo el nombre."
    },
    {
        "pregunta": "¿Cuántas iteraciones tiene?\n\nfor ($i = 0; $i -lt 5; $i++) {\n    Write-Host $i\n}",
        "opciones": ["4", "5", "6", "Infinitas", "0"],
        "correcta": 1,
        "explicacion": "i=0,1,2,3,4 → 5 iteraciones (cuando i=5 la condición i -lt 5 es falsa)."
    },
    {
        "pregunta": "¿Qué imprime?\n\n$i = 1\nwhile ($i -le 3) {\n    Write-Host ($i * 10)\n    $i++\n}",
        "opciones": ["1,2,3", "10,20,30", "10,20,30,40", "1,10,2,20,3,30", "10,10,10"],
        "correcta": 1,
        "explicacion": "i=1 → 10, i=2 → 20, i=3 → 30. Al llegar $i=4 la condición es falsa."
    },
    {
        "pregunta": "¿Qué hace?\n\nGet-Process | Sort-Object CPU -Descending | Select-Object -First 5 | ForEach-Object { $_.ProcessName }",
        "opciones": [
            "Los 5 procesos con menos CPU",
            "Los 5 procesos con más CPU ordenados",
            "Todos los procesos ordenados",
            "Procesos con CPU > 5",
            "Da error"
        ],
        "correcta": 1,
        "explicacion": "Sort-Object ordena descendente, Select-Object -First 5 toma los 5 primeros (más CPU)."
    },
    {
        "pregunta": "¿Cuál es el resultado de?\n\n$palabras = @('hola', 'mundo', 'powershell')\n$palabras | ForEach-Object { $_.Length }",
        "opciones": ["4,5,10", "hola,mundo,powershell", "5,6,11", "4,5,9", "3,4,8"],
        "correcta": 0,
        "explicacion": "'hola'=4, 'mundo'=5, 'powershell'=10 caracteres."
    },
    {
        "pregunta": "¿Qué imprime?\n\nfor ($i = 5; $i -ge 1; $i--) {\n    Write-Host $i\n}",
        "opciones": ["1,2,3,4,5", "5,4,3,2,1", "5,4,3,2,1,0", "1,2,3,4", "4,3,2,1"],
        "correcta": 1,
        "explicacion": "Bucle decreciente: i=5,4,3,2,1. Al llegar i=0 la condición -ge 1 es falsa."
    },
    {
        "pregunta": "¿Qué hace este código?\n\nGet-ChildItem -Directory | ForEach-Object {\n    Write-Host ('Carpeta: ' + $_.Name)\n}",
        "opciones": [
            "Lista archivos",
            "Lista carpetas con prefijo 'Carpeta: '",
            "Elimina carpetas",
            "Crea carpetas",
            "Cuenta carpetas"
        ],
        "correcta": 1,
        "explicacion": "Get-ChildItem -Directory obtiene carpetas, ForEach-Object las imprime con prefijo."
    },
    {
        "pregunta": "¿Cuántos procesos tienen CPU > 0?\n\nGet-Process | Where-Object { $_.CPU -gt 0 } | ForEach-Object { $_.Count }",
        "opciones": [
            "Cuenta los procesos con CPU > 0 (pero ForEach-Object no cuenta)",
            "Todos los procesos",
            "Da error",
            "Muestra el nombre de los procesos",
            "Cuenta el total de CPU"
        ],
        "correcta": 0,
        "explicacion": "ForEach-Object itera sobre cada objeto, pero cada objeto proceso no tiene propiedad 'Count'. No cuenta, solo itera."
    },
    {
        "pregunta": "¿Qué hace?\n\n$total = 0\nGet-ChildItem -File | ForEach-Object { $total += $_.Length }\nWrite-Host ('Total: ' + $total + ' bytes')",
        "opciones": [
            "Cuenta archivos",
            "Suma el tamaño de todos los archivos",
            "Elimina archivos",
            "Muestra el nombre de archivos",
            "Copia archivos"
        ],
        "correcta": 1,
        "explicacion": "Acumula Length (tamaño) de cada archivo en $total y lo muestra."
    },
    {
        "pregunta": "¿Qué imprime?\n\nforeach ($letra in 'a','b','c') {\n    if ($letra -eq 'b') { continue }\n    Write-Host $letra\n}",
        "opciones": ["a,b,c", "a,c", "a,b", "b,c", "c"],
        "correcta": 1,
        "explicacion": "continue salta la iteración cuando $letra='b', imprime solo 'a' y 'c'."
    },
]

comandos_recomendados = [
    {
        "comando": "Get-Process | Where-Object { $_.CPU -gt 10 } | Sort-Object CPU -Descending | Format-Table Name, CPU, Id",
        "explicacion": "Procesos con más de 10 de CPU, ordenados del que más consume al que menos",
        "dificultad": "Fácil"
    },
    {
        "comando": "Get-Service | Where-Object { $_.Status -eq 'Running' } | ForEach-Object { $_.Name }",
        "explicacion": "Lista solo los nombres de servicios que están en ejecución",
        "dificultad": "Fácil"
    },
    {
        "comando": "1..20 | ForEach-Object { if ($_ % 2 -eq 0) { Write-Host \"$_ es par\" } else { Write-Host \"$_ es impar\" } }",
        "explicacion": "Clasifica números del 1 al 20 como pares o impares usando el operador % (módulo)",
        "dificultad": "Media"
    },
    {
        "comando": "Get-ChildItem -File | Where-Object { $_.Length -gt 1MB } | Sort-Object Length -Descending | Format-Table Name, Length",
        "explicacion": "Archivos mayores de 1MB ordenados por tamaño descendente",
        "dificultad": "Fácil"
    },
    {
        "comando": "Get-Process | ForEach-Object { $_.Name } | Sort-Object -Unique",
        "explicacion": "Lista nombres de procesos únicos (sin repetir) ordenados alfabéticamente",
        "dificultad": "Fácil"
    },
    {
        "comando": "$suma = 0; Get-ChildItem -File | ForEach-Object { $suma += $_.Length }; Write-Host \"Total: $suma bytes\"",
        "explicacion": "Calcula el tamaño total de todos los archivos del directorio actual",
        "dificultad": "Media"
    },
    {
        "comando": "Get-Process | Group-Object -Property Company | Where-Object { $_.Count -gt 5 } | Format-Table Name, Count",
        "explicacion": "Agrupa procesos por empresa y muestra solo grupos con más de 5 procesos",
        "dificultad": "Media"
    },
    {
        "comando": "foreach ($i in 1..10) { foreach ($j in 1..10) { Write-Host (\"$i x $j = \" + ($i * $j)) } }",
        "explicacion": "Tabla de multiplicar del 1 al 10 usando bucles anidados",
        "dificultad": "Media"
    },
    {
        "comando": "Get-Date; 1..5 | ForEach-Object { Start-Sleep -Seconds 1; Get-Date }",
        "explicacion": "Muestra la hora actual 6 veces con 1 segundo de diferencia usando Start-Sleep",
        "dificultad": "Media"
    },
    {
        "comando": "Get-ChildItem -Recurse -File | Group-Object Extension | Sort-Object Count -Descending | Select-Object -First 10",
        "explicacion": "Las 10 extensiones de archivo más comunes en el directorio actual y subdirectorios",
        "dificultad": "Difícil"
    },
    {
        "comando": "Get-Process | Where-Object { $_.WorkingSet -gt 100MB } | Sort-Object WorkingSet -Descending | Format-Table Name, @{N='Memoria(MB)';E={[math]::Round($_.WorkingSet/1MB,2)}}",
        "explicacion": "Procesos que usan más de 100MB de RAM, ordenados por consumo, mostrando memoria en MB",
        "dificultad": "Difícil"
    },
    {
        "comando": "$contar = @{}; Get-ChildItem -Recurse -File | ForEach-Object { $ext = $_.Extension; if ($contar[$ext]) { $contar[$ext]++ } else { $contar[$ext] = 1 } }; $contar.GetEnumerator() | Sort-Object Value -Descending",
        "explicacion": "Cuenta archivos por extensión usando un hashtable (equivalente a diccionario)",
        "dificultad": "Difícil"
    },
    {
        "comando": "Get-Service | Where-Object { $_.StartType -eq 'Automatic' -and $_.Status -ne 'Running' } | ForEach-Object { Write-Host \"ATENCIÓN: $($_.Name) debería estar en ejecución\" }",
        "explicacion": "Detecta servicios que deberían estar running (automáticos) pero no lo están",
        "dificultad": "Difícil"
    },
    {
        "comando": "Get-EventLog -LogName System -Newest 100 | Where-Object { $_.EntryType -eq 'Error' } | Format-Table TimeGenerated, Message -Wrap",
        "explicacion": "Muestra los últimos 100 errores del registro de eventos del sistema",
        "dificultad": "Difícil"
    },
    {
        "comando": "$i = 1; while ($i -le 10) { if ($i -eq 5) { $i++; continue }; Write-Host \"Número: $i\"; $i++ }",
        "explicacion": "Imprime números del 1 al 10 saltándose el 5 usando continue",
        "dificultad": "Media"
    },
]

def menu_principal():
    while True:
        print("\n" + "=" * 60)
        print("  PRÁCTICA DE POWERSHELL - COMANDOS + BUCLES")
        print("=" * 60)
        print("1. Ejercicios de lógica (15 preguntas)")
        print("2. Comandos recomendados para practicar")
        print("3. Simulacro de examen completo (aleatorio)")
        print("4. Salir")
        opcion = input("\nElige una opción (1-4): ").strip()

        if opcion == "1":
            ejercicios_logica_interactivo()
        elif opcion == "2":
            mostrar_comandos()
        elif opcion == "3":
            examen_aleatorio()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

def ejercicios_logica_interactivo():
    random.shuffle(ejercicios_logica)
    correctas = 0

    for idx, ej in enumerate(ejercicios_logica, 1):
        print(f"\n--- Ejercicio {idx} ---")
        print(ej["pregunta"])
        for letra in range(5):
            print(f"  {'ABCDE'[letra]}) {ej['opciones'][letra]}")

        while True:
            resp = input("\nTu respuesta (A, B, C, D, E): ").strip().upper()
            if resp in "ABCDE":
                respuesta_idx = "ABCDE".index(resp)
                break
            print("No válido. Elige A, B, C, D o E.")

        if respuesta_idx == ej["correcta"]:
            print("  CORRECTO!")
            correctas += 1
        else:
            print(f"  INCORRECTO. La correcta era {chr(65 + ej['correcta'])}")
        print(f"  Explicación: {ej['explicacion']}")

    print(f"\n--- Resultados: {correctas}/{len(ejercicios_logica)} ---")

def mostrar_comandos():
    while True:
        print("\n" + "=" * 60)
        print("  COMANDOS RECOMENDADOS PARA PRACTICAR")
        print("=" * 60)
        print("F) Fáciles    M) Medios    D) Difíciles    T) Todos    X) Volver")

        filtro = input("\nFiltro: ").strip().upper()
        if filtro == "X":
            break

        filtrados = []
        for cmd in comandos_recomendados:
            if filtro == "T":
                filtrados.append(cmd)
            elif filtro == "F" and cmd["dificultad"] == "Fácil":
                filtrados.append(cmd)
            elif filtro == "M" and cmd["dificultad"] == "Media":
                filtrados.append(cmd)
            elif filtro == "D" and cmd["dificultad"] == "Difícil":
                filtrados.append(cmd)

        if not filtrados:
            print("No hay comandos con ese filtro.")
            continue

        for i, cmd in enumerate(filtrados, 1):
            print(f"\n--- Comando {i} [{cmd['dificultad']}] ---")
            print(f"  $ {cmd['comando']}")
            print(f"  → {cmd['explicacion']}")
            print(f"  {'=' * 50}")

def examen_aleatorio():
    todas = ejercicios_logica.copy()
    random.shuffle(todas)
    correctas = 0

    for idx, ej in enumerate(todas, 1):
        print(f"\n--- Pregunta {idx}/{len(todas)} ---")
        print(ej["pregunta"])
        for letra in range(5):
            print(f"  {'ABCDE'[letra]}) {ej['opciones'][letra]}")

        while True:
            resp = input("\nRespuesta (A, B, C, D, E): ").strip().upper()
            if resp in "ABCDE":
                respuesta_idx = "ABCDE".index(resp)
                break
            print("No válido.")

        if respuesta_idx == ej["correcta"]:
            print("  CORRECTO!")
            correctas += 1
        else:
            print(f"  INCORRECTO → {chr(65 + ej['correcta'])}")

    nota = round((correctas / len(todas)) * 10, 1)
    print(f"\n--- Resultado: {correctas}/{len(todas)} = {nota}/10 ---")
    if nota >= 5:
        print("APROBADO!")
    else:
        print("SUSPENSO. Sigue practicando.")

if __name__ == "__main__":
    menu_principal()
