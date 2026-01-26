package bloquealeatorios;
import java.util.Scanner;
import java.util.Random;

public class ejercicio2 {
    public static void main(String[] args) {
        Random num = new Random();
        int sumaTotal = 0; // Para guardar el total de los 3 dados

        System.out.println("Lanzando los dados...");

        for (int i = 1; i <= 3; i++) {
            // Rango [1, 6]: 6 opciones empezando en 1
            int dado = num.nextInt(6) + 1; 
            
            System.out.println("Dado " + i + ": " + dado);
            
            // Vamos acumulando el valor
            sumaTotal += dado; 
        }

        System.out.println("--------------------");
        System.out.println("Suma total: " + sumaTotal);
    }
}