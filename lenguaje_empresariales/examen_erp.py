#!/usr/bin/env python3

preguntas = [
    "1. \u00bfQu\u00e9 significan las siglas ERP?",
    "2. \u00bfCu\u00e1les son las tres caracter\u00edsticas principales de un sistema ERP?",
    "3. \u00bfQu\u00e9 ventaja ofrece la base de datos centralizada en un ERP?",
    "4. \u00bfQu\u00e9 m\u00f3dulo del ERP gestiona la relaci\u00f3n con los clientes?",
    "5. \u00bfQu\u00e9 diferencia hay entre la arquitectura Cliente-Servidor y la arquitectura SaaS?",
    "6. \u00bfQu\u00e9 tipos de licencias puede tener un sistema ERP?",
    "7. Nombra dos sistemas ERP propietarios y dos sistemas ERP libres.",
    "8. \u00bfQu\u00e9 m\u00f3dulo se encarga de la gesti\u00f3n del ciclo de vida de los productos?",
    "9. \u00bfCu\u00e1les son los dos requisitos imprescindibles para implantar un sistema ERP con \u00e9xito?",
    "10. \u00bfCu\u00e1l es el principal inconveniente econ\u00f3mico de adoptar un sistema ERP?",
]

respuestas = []

print("=" * 60)
print("  EXAMEN - SISTEMAS ERP")
print("  Responde cada pregunta con tus propias palabras.")
print("=" * 60)

for i, p in enumerate(preguntas, 1):
    print(f"\n--- Pregunta {i} de {len(preguntas)} ---")
    print(p)
    rta = input("> ").strip()
    respuestas.append(rta)

print("\n" + "=" * 60)
print("  EXAMEN COMPLETADO - TUS RESPUESTAS")
print("=" * 60)
for i, r in enumerate(respuestas, 1):
    print(f"\nPregunta {i}:")
    print(f"  {r}")

print("\n" + "-" * 60)
print("COPIA EL TEXTO DE ARRIBA (Pregunta 1 a 10) Y ENV\u00cdALO A OPENCODE")
print("PARA QUE TE EVAL\u00daE.")
print("-" * 60)
