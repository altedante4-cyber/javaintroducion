package und4;

import java.util.Scanner;

public class Ejercicio3 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int num1;
        int num2;

        do {
            System.out.println("Ingrese el primer número entre 0 y 100: ");
            num1 = entrada.nextInt();

            System.out.println("Ingrese el segundo número entre 0 y 100: ");
            num2 = entrada.nextInt();

            if (num1 < 0 || num1 > 100 || num2 < 0 || num2 > 100 || num1 == num2) {
                System.out.println("Estás ingresando valores inválidos.");
            }

        } while (num1 < 0 || num1 > 100 || num2 < 0 || num2 > 100 || num1 == num2);

        // Caso ascendente
        if (num1 < num2) {
            for (int i = num1; i <= num2; i++) {
                System.out.println(i);
            }
        } 
        // Caso descendente
        else {
            for (int i = num1; i <= num2; i--) {
                System.out.println(i);
            }
        }

        entrada.close();
    }
}
