#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def normalize(cmd):
    """Elimina espacios extra y convierte a minúsculas para comparación flexible."""
    # Eliminar espacios al inicio/final y reducir espacios múltiples a uno solo
    cmd = cmd.strip().lower()
    cmd = re.sub(r'\s+', ' ', cmd)
    return cmd

def check_answer(user_input, expected, alternatives=None):
    """Compara la respuesta normalizada con la esperada o sus alternativas."""
    norm_user = normalize(user_input)
    norm_expected = normalize(expected)
    if norm_user == norm_expected:
        return True
    if alternatives:
        for alt in alternatives:
            if norm_user == normalize(alt):
                return True
    return False

def main():
    preguntas = [
        {
            "texto": "🔹 1. Muestra la versión de PowerShell instalada (cmdlet que da información del host).",
            "esperado": "Get-Host",
            "alternativas": ["get-host", "gethost"]
        },
        {
            "texto": "🔹 2. Lista todos los comandos disponibles en PowerShell (cmdlets, alias, funciones).",
            "esperado": "Get-Command",
            "alternativas": ["get-command", "gcm"]
        },
        {
            "texto": "🔹 3. Muestra la ayuda del cmdlet Get-ChildItem.",
            "esperado": "Get-Help Get-ChildItem",
            "alternativas": ["help get-childitem", "get-help get-childitem", "man get-childitem"]
        },
        {
            "texto": "🔹 4. Crea un archivo llamado 'examen.txt' con el contenido 'Hola PowerShell'.\n   Usa el cmdlet New-Item con los parámetros adecuados.",
            "esperado": "New-Item -Name examen.txt -ItemType file -Value 'Hola PowerShell'",
            "alternativas": [
                "new-item -name examen.txt -itemtype file -value 'hola powershell'",
                "new-item -path examen.txt -itemtype file -value 'hola powershell'"
            ]
        },
        {
            "texto": "🔹 5. Elimina el archivo 'examen.txt' que acabas de crear.",
            "esperado": "Remove-Item examen.txt",
            "alternativas": ["remove-item -path examen.txt", "del examen.txt", "erase examen.txt"]
        },
        {
            "texto": "🔹 6. Muestra todos los procesos cuyo nombre sea 'powershell' en formato tabla con las columnas ID y Nombre.",
            "esperado": "Get-Process -Name powershell | Format-Table Id, Name",
            "alternativas": [
                "get-process -name powershell | ft id,name",
                "ps -name powershell | format-table id,name"
            ]
        },
        {
            "texto": "🔹 7. Obtén la fecha actual y luego muestra solo el año (usando una propiedad del objeto fecha).",
            "esperado": "(Get-Date).Year",
            "alternativas": ["(get-date).year", "get-date | select -expandproperty year"]
        },
        {
            "texto": "🔹 8. Usando Where-Object, filtra los servicios que estén detenidos (status 'Stopped').",
            "esperado": "Get-Service | Where-Object {$_.Status -eq 'Stopped'}",
            "alternativas": [
                "get-service | where {$_.status -eq 'stopped'}",
                "get-service | where-object status -eq stopped"
            ]
        },
        {
            "texto": "🔹 9. Escribe un bucle 'for' que muestre los números del 1 al 5 (cada uno en una línea).",
            "esperado": "for ($i=1; $i -le 5; $i++) {$i}",
            "alternativas": ["for($i=1;$i -le 5;$i++){$i}"]
        },
        {
            "texto": "🔹 10. ¿Qué cmdlet se usa para ver las propiedades y métodos de un objeto? (Ej: Get-Process | ???)",
            "esperado": "Get-Member",
            "alternativas": ["get-member", "gm"]
        }
    ]

    aciertos = 0
    total = len(preguntas)

    print("\n" + "="*60)
    print("🧪 EXAMEN INTERACTIVO DE POWERSHELL".center(60))
    print("="*60)
    print("Responde cada comando. Tienes 3 intentos por pregunta.\n")

    for i, p in enumerate(preguntas, 1):
        print(f"\n📌 Pregunta {i}/{total}")
        print(p["texto"])
        print("-" * 50)

        for intento in range(1, 4):
            respuesta = input("> ").strip()
            if check_answer(respuesta, p["esperado"], p.get("alternativas")):
                print("✅ ¡Correcto!\n")
                aciertos += 1
                break
            else:
                restantes = 3 - intento
                if restantes > 0:
                    print(f"❌ Incorrecto. Te quedan {restantes} intento(s).")
                    if intento == 1:
                        print("💡 Pista: Revisa la sintaxis y la capitalización de los cmdlets.")
                    elif intento == 2:
                        print(f"💡 Pista: El comando esperado se parece a: {p['esperado'][:60]}...")
                else:
                    print(f"❌ Has fallado. La respuesta correcta era:\n   {p['esperado']}\n")
        else:
            # Si se acaban los intentos, se considera fallo y se muestra la respuesta
            # ya se mostró arriba, solo continuamos
            pass

    print("\n" + "="*60)
    print(f"🏁 EXAMEN FINALIZADO - Aciertos: {aciertos}/{total}")
    if aciertos == total:
        print("🎉 ¡Perfecto! Dominas PowerShell.")
    elif aciertos >= total//2:
        print("👍 Buen trabajo. Sigue practicando para pulir detalles.")
    else:
        print("📚 Revisa los conceptos básicos. ¡Ánimo!")

if __name__ == "__main__":
    main()
