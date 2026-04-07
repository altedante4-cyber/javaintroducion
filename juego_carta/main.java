import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Baraja baraja = new Baraja(1, true);

        double puntos = 0;
        boolean plantado = false;

        while (!plantado) {
            System.out.println("Puntos: " + puntos);
            System.out.print("Carta (s) o plantarse (n)? ");
            String resp = sc.nextLine();

            if (resp.equalsIgnoreCase("n")) {
                plantado = true;
                break;
            }

            if (resp.equalsIgnoreCase("s")) {
                Carta c = baraja.Robar();
                puntos += c.Valor7ymedia();
                System.out.println(c.NombreCarta()+"=>"+ c.Valor7ymedia());
                System.out.println("Total" + puntos + "\n");

                if (puntos > 7.5) {
                    System.out.println("TE HAS PASADO");
                    break;
                }
            }
        }

        System.out.println("Puntos finales "+puntos);
    }
}
