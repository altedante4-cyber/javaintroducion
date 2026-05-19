import random
from questions import questions

def run_quiz(questions):
    score = 0
    random.shuffle(questions) # Mezclar las preguntas

    print("\n--- ¡Bienvenido al examen de Refactorización y Buenas Prácticas de Código! ---")
    print("Responde a las siguientes preguntas seleccionando el número de la opción correcta.\n")

    for i, q in enumerate(questions):
        print(f"Pregunta {i + 1}: {q['question']}")
        for j, option in enumerate(q['options']):
            print(f"  {j + 1}. {option}")

        while True:
            try:
                user_answer = int(input("Tu respuesta (número): "))
                if 1 <= user_answer <= len(q['options']):
                    break
                else:
                    print("Por favor, introduce un número válido de opción.")
            except ValueError:
                print("Entrada inválida. Por favor, introduce un número.")

        if user_answer - 1 == q['correct_answer']:
            print("¡Correcto!\n")
            score += 1
        else:
            print(f"Incorrecto. La respuesta correcta era: {q['options'][q['correct_answer']]}\n")

    print("--- Examen Finalizado ---")
    print(f"Tu puntuación final es: {score} de {len(questions)}")
    percentage = (score / len(questions)) * 100
    print(f"Porcentaje: {percentage:.2f}%")

    if percentage >= 90:
        print("¡Excelente! ¡Matrícula de honor asegurada!")
    elif percentage >= 70:
        print("¡Muy bien! Buen conocimiento del tema.")
    elif percentage >= 50:
        print("Necesitas repasar un poco más.")
    else:
        print("Es necesario un repaso profundo.")

if __name__ == "__main__":
    run_quiz(questions)
