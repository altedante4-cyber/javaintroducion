import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Baraja n1 = new Baraja(1, true);

        double puntos = 0;
        boolean plantado = false;

        System.out.println("=== JUEGO 7 Y MEDIA ===\n");

        while (!plantado && puntos <= 7.5) {
            System.out.println("Puntos actuales: " + puntos);
            System.out.print("Quieres otra carta? (s/n): ");
            String respuesta = sc.nextLine();

            if (respuesta.equalsIgnoreCase("n")) {
                plantado = true;
                break;
            }

            if (respuesta.equalsIgnoreCase("s")) {
                if (n1.Vacia()) {
                    System.out.println("No quedan cartas");
                    break;
                }

                Carta carta = n1.Robar();
                puntos += carta.Valor7ymedia();

                System.out.println("Carta robada: " + carta.NombreCarta());
                System.out.println("Valor: " + carta.Valor7ymedia());
                System.out.println("Total puntos: " + puntos);
                System.out.println();
            }
        }

        System.out.println("=== RESULTADO ===");
        System.out.println("Puntos finales: " + puntos);

        if (puntos > 7.5) {
            System.out.println("TE HAS PASADO! Has perdido");
        } else if (puntos == 7.5) {
            System.out.println("SIETE Y MEDIA! Ganaste!");
        } else {
            System.out.println("Te has plantado con " + puntos + " puntos");
        }

        sc.close();
    }
}
