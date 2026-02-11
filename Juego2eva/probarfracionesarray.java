package Juego2eva;

import java.util.Scanner;

public class probarfracionesarray {

    public static void main(String[] args) {

        Fraccion[] mio = new Fraccion[3];
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < 3; i++) {
            System.out.println("Fracción " + (i + 1));
            System.out.print("Introduce numerador: ");
            int n = sc.nextInt();
            System.out.print("Introduce denominador: ");
            int p = sc.nextInt();

            mio[i] = new Fraccion(n, p);
        }

        // 2. Realizar la operación (Suma acumulada)
        // Inicializamos 'total' con la primera fracción del array
        Fraccion total = mio[0];

        // Empezamos el bucle desde el segundo elemento (índice 1) ESTO ES DONDE ESTABA FALLANDO POR QUE ESTABA EMPEZANDO A SUMAR DESDE EL PRIMER ELEMENTO  Y EL PRIMER ELEMENTO YA LO TENIA EN EL TOTAL DEFINIDO Y POR ENDE TENIA QUE EMPESAR  CON EL SEGUNDO ELEMENTO 
        for (int i = 1; i < 3; i++) {
            total = total.sumarFraccion(mio[i]); 
        }

        // 3. Mostrar resultados
        System.out.println("---------------------------");
        System.out.println("La suma total es: " + total.toString());
        
        System.out.println("Denominadores de las fracciones originales:");
        for (int i = 0; i < 3; i++) {
            System.out.println("Fracción " + i + ": " + mio[i].damedenomidor());
        }
    }
}