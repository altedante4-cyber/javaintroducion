import java.io.FileReader;
import java.util.Scanner;

public class DebugCaracteres {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int caracteranterior = 0;
        int caracter = 0;
        int contador = 0;

        System.out.println("╔══════════════════════════════════════════════════════════════╗");
        System.out.println("║                    DEPURACIÓN VISUAL                     ║");
        System.out.println("╚══════════════════════════════════════════════════════════════╝\n");

        System.out.println("[1] Estado inicial:");
        System.out.println("    caracteranterior = " + caracteranterior + " (0)");
        System.out.println("    caracter       = " + caracter + " (0)");
        System.out.println("    contador       = " + contador + "\n");

        try(FileReader leer = new FileReader("nombres.txt")) {
            System.out.println("[2] Iniciando bucle while...\n");
            System.out.println("    ┌──────────────────────────────────────────────────────────────┐");
            System.out.println("    │ ITERACIÓN │ caracter │ caracteranterior │ Condición      │ Contador │");
            System.out.println("    ├──────────────────────────────────────────────────────────────┤");

            int iteracion = 0;
            while((caracter = leer.read()) != -1) {
                iteracion++;

                String condicion = "";
                boolean saltaLinea = false;

                // Verificar condición
                if (caracteranterior == '\n' && caracter == '\n') {
                    condicion = "\n --> DOUBLE \\n detected!";
                    saltaLinea = true;
                } else if (caracter == '\n') {
                    condicion = "\\n (salto de línea)";
                }

                // Solo mostrar primeras 20 iteraciones para no saturar
                if (iteracion <= 20) {
                    char cAnterior = (caracteranterior == 0) ? ' ' : (char)caracteranterior;
                    char cActual = (char)caracter;

                    System.out.printf("    │ %-8d │ %-7c │ %-14c │ %-13s │ %-7d │%n",
                        iteracion, cActual, cAnterior, condicion.trim(), contador);
                }

                if (saltaLinea) {
                    //continue; // Aquí se saltaría la línea
                } else {
                    contador++;
                }

                caracteranterior = caracter;
            }

            System.out.println("    └──────────────────────────────────────────────────────────────┘\n");

            // Agregar 1 al final
            contador += 1;

            System.out.println("[3] Después del bucle:");
            System.out.println("    contador += 1 → " + contador);
            System.out.println("\n[RESULTADO FINAL] Contador = " + contador);

        } catch(Exception e) {
            System.out.println("Error: " + e.getMessage());
        }

        sc.close();
    }
}