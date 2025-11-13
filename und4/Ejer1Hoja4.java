package und4;

public class Ejer1Hoja4 {

    public static void main(String[] args) {
        
        // Rellenar un array con los 100 primeros números enteros
        // y mostrarlos en pantalla en orden ascendente
        
        final int TAM = 100; // tamaño del array
        int[] numeros = new int[TAM];
        
        // Rellenamos el array
        for (int i = 0; i < TAM; i++) {
            numeros[i] = i + 1; // los números del 1 al 100
        }
        
        // Mostramos el array
        for (int i = 0; i < TAM; i++) {
            System.out.println(numeros[i]);
        }
    }
}
