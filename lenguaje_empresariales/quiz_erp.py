import random
import os

preguntas = [
    {
        "id": 1,
        "pregunta": "¿Qué significan las siglas ERP?",
        "respuesta": "Enterprise Resource Planning (Planificación de Recursos Empresariales)",
        "pista": "Empieza con 'Enterprise...'"
    },
    {
        "id": 2,
        "pregunta": "¿Cuáles son las tres características principales de un sistema ERP?",
        "respuesta": "Integral, Modular y Adaptable",
        "pista": "IMA"
    },
    {
        "id": 3,
        "pregunta": "¿Qué ventaja ofrece la base de datos centralizada en un ERP?",
        "respuesta": "Elimina redundancia, garantiza consistencia e integridad, y proporciona una única fuente de verdad (single source of truth)",
        "pista": "Elimina... garantiza... proporciona..."
    },
    {
        "id": 4,
        "pregunta": "¿Qué módulo del ERP gestiona la relación con los clientes?",
        "respuesta": "CRM (Customer Relationship Management)",
        "pista": "Son 3 siglas en inglés"
    },
    {
        "id": 5,
        "pregunta": "¿Qué diferencia hay entre la arquitectura Cliente-Servidor y la arquitectura SaaS?",
        "respuesta": "Cliente-Servidor: software instalado en servidores locales. SaaS: software en la nube por suscripción, sin gestionar infraestructura propia.",
        "pista": "Una es local, la otra es en la nube"
    },
    {
        "id": 6,
        "pregunta": "¿Qué tipos de licencias puede tener un sistema ERP?",
        "respuesta": "Propietaria (código cerrado, pago) y Libre/Open Source (código abierto, gratuito con posibles costes de servicio)",
        "pista": "Dos: una de pago y una gratuita"
    },
    {
        "id": 7,
        "pregunta": "Nombra dos sistemas ERP propietarios y dos sistemas ERP libres.",
        "respuesta": "Propietarios: SAP, Oracle. Libres: Odoo, ERPNext.",
        "pista": "Uno empieza con S, otro con O. Libres: Odoo y E..."
    },
    {
        "id": 8,
        "pregunta": "¿Qué módulo se encarga de la gestión del ciclo de vida de los productos?",
        "respuesta": "PLM (Product Lifecycle Management)",
        "pista": "Son 3 siglas en inglés"
    },
    {
        "id": 9,
        "pregunta": "¿Cuáles son los dos requisitos imprescindibles para implantar un sistema ERP con éxito?",
        "respuesta": "1) Compromiso de la dirección. 2) Formación adecuada de los usuarios.",
        "pista": "Uno es de arriba (directivos), otro es de abajo (usuarios)"
    },
    {
        "id": 10,
        "pregunta": "¿Cuál es el principal inconveniente económico de adoptar un sistema ERP?",
        "respuesta": "El alto coste de implantación (licencias, consultoría, personalización, migración y mantenimiento)",
        "pista": "No es la licencia en sí, es todo el proceso de..."
    },
]


def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


def menu_principal():
    limpiar()
    print("=" * 60)
    print("           🧠  QUIZ ERP - EXAMEN  🧠".center(60))
    print("=" * 60)
    print("  1. 📝  Responder preguntas en orden")
    print("  2. 🔀  Responder preguntas aleatorias")
    print("  3. 🎯  Practicar preguntas falladas")
    print("  4. 📖  Modo estudio (ver todo)")
    print("  5. 🚪  Salir")
    print("=" * 60)
    return input("  Elige una opción (1-5): ").strip()


def modo_estudio():
    limpiar()
    print("=" * 60)
    print("           📖  MODO ESTUDIO  📖".center(60))
    print("=" * 60)
    for p in preguntas:
        input(f"\n  Pulsa Enter para ver la pregunta {p['id']}...")
        print(f"\n  📌  {p['pregunta']}")
        input("  Pulsa Enter para ver la respuesta...")
        print(f"  ✅  {p['respuesta']}")
    print("\n  ✅  ¡Has repasado todas las preguntas!")
    input("\n  Pulsa Enter para volver al menú...")


def hacer_quiz(orden):
    falladas = []
    aciertos = 0
    total = len(orden)

    for i, idx in enumerate(orden, 1):
        p = preguntas[idx]
        limpiar()
        print(f"  Pregunta {i} de {total}\n")
        print(f"  📌  {p['pregunta']}")
        print(f"\n  [Escribe 'pista' para una ayuda]")
        print(f"  [Escribe 'saltar' para ver la respuesta]")
        print(f"  [Escribe 'salir' para terminar]")
        print("-" * 60)

        while True:
            user = input("  Tu respuesta: ").strip().lower()

            if user == "salir":
                print(f"\n  📊  Llevas {aciertos}/{i-1} aciertos")
                input("\n  Pulsa Enter para volver al menú...")
                return falladas

            if user == "pista":
                print(f"  💡  Pista: {p['pista']}")
                continue

            if user == "saltar":
                print(f"\n  ❌  Respuesta correcta: {p['respuesta']}")
                falladas.append(idx)
                break

            if len(user) >= 5:
                print(f"\n  ✅  Respuesta: {p['respuesta']}")
                aciertos += 1
                break
            else:
                print("  Escribe al menos 5 caracteres o usa 'saltar'.")

        input("\n  Pulsa Enter para continuar...")

    limpiar()
    nota = (aciertos / total) * 10
    print(f"\n  🎯  Resultado final: {aciertos}/{total}  ->  Nota: {nota:.1f}/10")
    if falladas:
        print(f"\n  📝  Preguntas a repasar: {len(falladas)}")
    if nota >= 10:
        print("\n  🏆  ¡PERFECTO! Listo para el examen.")
    elif nota >= 7:
        print("\n  👍  Bueno, pero repasa las falladas.")
    else:
        print("\n  📚  Sigue practicando, usa el modo estudio.")
    input("\n  Pulsa Enter para volver al menú...")
    return falladas


def main():
    falladas_global = []

    while True:
        opcion = menu_principal()

        if opcion == "1":
            falladas_global = hacer_quiz(list(range(len(preguntas))))

        elif opcion == "2":
            orden = list(range(len(preguntas)))
            random.shuffle(orden)
            falladas_global = hacer_quiz(orden)

        elif opcion == "3":
            if not falladas_global:
                print("\n  ❌  Aún no has fallado ninguna. ¡Haz un quiz primero!")
                input("  Pulsa Enter para continuar...")
                continue
            falladas_global = hacer_quiz(falladas_global)

        elif opcion == "4":
            modo_estudio()

        elif opcion == "5":
            print("\n  🍀  ¡Suerte en el examen!\n")
            break

        else:
            print("\n  ❌  Opción no válida.")
            input("  Pulsa Enter para continuar...")


if __name__ == "__main__":
    main()
