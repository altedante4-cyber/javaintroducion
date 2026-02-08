package Juego2eva;

public class probar {
    public static void main(String[] args) {

        char[][] posicion = new char[3][3];

    for (int i = 0; i < posicion.length; i++) {
        for (int j = 0; j < posicion[i].length; j++) {
            System.out.print(" " + posicion[i][j] + " ");
            if (j < posicion[i].length - 1) System.out.print("|"); // No pone barra al final
        }
        System.out.println();
        if (i < posicion.length - 1) {
            System.out.println("-----------"); // No pone línea al final
        }
    }



    }
}