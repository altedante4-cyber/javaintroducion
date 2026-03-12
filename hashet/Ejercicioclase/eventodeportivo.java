package Ejercicioclase;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;

public class eventodeportivo {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        ArrayList<String> email = new ArrayList<>();
        HashSet<String> registrosrecibidos = new HashSet<String>();

        int opcion;
        char op;

        do {
            System.out.println("Ingresar email 1.s 2.n");
            op = sc.nextLine().charAt(0);

            if (op == 's') {

                System.out.println("ingrese el email ");
                String email1 = sc.nextLine();

                email.add(email1);
                registrosrecibidos.add(email1);
                System.out.println("agregado correctamente");

            }

            if (op == 'n') {
                System.out.println("SALIENDO ..................................");
            }

        } while (op != 'n');

        do {

            System.out.println("1.Numero total de registros recibidos");
            System.out.println("2.Numero total de asistentes unicos");
            System.out.println("3.Que emails estan duplicados");
            System.out.println("4.Salir");

            opcion = sc.nextInt();
            sc.nextLine();

            switch (opcion) {

                case 1:
                    int numero_recibidos = email.size();
                    System.out.println("el numero total de registros recibidos es " + numero_recibidos);
                    break;

                case 2:
                    int numero_de_asistentes_unicos = registrosrecibidos.size();
                    System.out.println("el numero total de registros unicos es de " + numero_de_asistentes_unicos);
                    break;

                case 3:

                    for (String correo : registrosrecibidos) {

                        int contador = 0;

                        for (String e : email) {
                            if (correo.equals(e)) {
                                contador++;
                            }
                        }

                        if (contador > 1) {
                            System.out.println("Email duplicado: " + correo);
                        }
                    }

                    break;

                default:
                    System.out.println("Opcion no valida");
                    break;
            }

        } while (opcion != 4);

    }
}