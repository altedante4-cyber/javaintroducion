package juego;

import java.util.Scanner;

public class TresEnRaya {
    static Scanner entrada = new Scanner(System.in);
    static char[] tablero = new char[9];
    static int ganadasJugador1 = 0;
    static int ganadasJugador2 = 0;
    static int erroresJugador1 = 0;
    static int erroresJugador2 = 0;
    static int empates = 0;

    public static void main(String[] args) {
        dibujaTablero(); // iniciar tablero vacío

        do {
            mostrartable();
            int opcion = entrada.nextInt();
            int jugador = 1; // 1 = Jugador 1 (X), 2 = Jugador 2 (O)

            if (opcion == 3) {
                break;
            } else if (opcion == 1) {
                dibujaTablero(); // tablero vacío al iniciar partida
                boolean repetir = true;
                int contador = 0;

                while (repetir) {
                    while (contador < 9) {
                        int posicion;

                        // Pedir posición válida
                        do {
                            System.out.println("Jugador " + jugador + ", elige posición (1-9): ");
                            posicion = entrada.nextInt() - 1;

                            if (posicion < 0 || posicion > 8) {
                                System.out.println("Posición inválida");
                                if (jugador == 1) erroresJugador1++;
                                else erroresJugador2++;
                            }

                        } while (posicion < 0 || posicion > 8);

                        // Validar movimiento
                        if (movimientoValido(posicion)) {
                            if (jugador == 1) {
                                mueveJugador1(posicion);
                                iniciar();  // mostrar tablero actualizado
                                jugador = 2;
                            } else {
                                mueveJugador2(posicion);
                                iniciar();  // mostrar tablero actualizado
                                jugador = 1;
                            }
                        } else {
                            System.out.println("Movimiento inválido, casilla ocupada");
                            if (jugador == 1) erroresJugador1++;
                            else erroresJugador2++;
                            continue; // volver a pedir posición
                        }

                        contador++;

                        // Comprobar ganador
                        if (ganaJugador1()) {
                            System.out.println("Jugador X ha ganado");
                            ganadasJugador1++;
                            break;
                        } else if (ganaJugador2()) {
                            System.out.println("Jugador O ha ganado");
                            ganadasJugador2++;
                            break;
                        }

                        // Comprobar empate
                        if (contador == 9) {
                            System.out.println("¡Empate!");
                            empates++;
                            break;
                        }
                    }

                    dibujaTablero(); // limpiar tablero para nueva partida
                    repetir = false;
                }

            } else if (opcion == 2) {
                System.out.println("Victorias Jugador X: " + ganadasJugador1);
                System.out.println("Victorias Jugador O: " + ganadasJugador2);
                System.out.println("Errores Jugador X: " + erroresJugador1);
                System.out.println("Errores Jugador O: " + erroresJugador2);
                System.out.println("Empates: " + empates);
            }

        } while (true);

        System.out.println("Partida terminada");
    }

    public static void mostrartable() {
        System.out.println("\n1. Jugar una partida");
        System.out.println("2. Mostrar estadísticas");
        System.out.println("3. Salir");
        System.out.println("Seleccione una opción");
        System.out.println("-----------");
        System.out.println("| 1 | 2 | 3 |");
        System.out.println("-----------");
        System.out.println("| 4 | 5 | 6 |");
        System.out.println("-----------");
        System.out.println("| 7 | 8 | 9 |");
        System.out.println("-----------");
    }

    public static void iniciar() {
        System.out.println();
        for (int i = 0; i < 9; i++) {
            System.out.print("| " + tablero[i] + " ");
            if ((i + 1) % 3 == 0) {
                System.out.println("|");
                System.out.println("-------------");
            }
        }
        System.out.println();
    }

    public static void dibujaTablero() {
        for (int i = 0; i < tablero.length; i++) {
            tablero[i] = ' '; // tablero vacío
        }
    }

    public static void mueveJugador1(int pos) {
        tablero[pos] = 'X';
    }

    public static void mueveJugador2(int pos) {
        tablero[pos] = 'O';
    }

    public static boolean movimientoValido(int pos) {
        return pos >= 0 && pos <= 8 && tablero[pos] == ' ';
    }

    public static boolean ganaJugador1() {
        return (tablero[0] == 'X' && tablero[1] == 'X' && tablero[2] == 'X') ||
               (tablero[3] == 'X' && tablero[4] == 'X' && tablero[5] == 'X') ||
               (tablero[6] == 'X' && tablero[7] == 'X' && tablero[8] == 'X') ||
               (tablero[0] == 'X' && tablero[3] == 'X' && tablero[6] == 'X') ||
               (tablero[1] == 'X' && tablero[4] == 'X' && tablero[7] == 'X') ||
               (tablero[2] == 'X' && tablero[5] == 'X' && tablero[8] == 'X') ||
               (tablero[0] == 'X' && tablero[4] == 'X' && tablero[8] == 'X') ||
               (tablero[2] == 'X' && tablero[4] == 'X' && tablero[6] == 'X');
    }

    public static boolean ganaJugador2() {
        return (tablero[0] == 'O' && tablero[1] == 'O' && tablero[2] == 'O') ||
               (tablero[3] == 'O' && tablero[4] == 'O' && tablero[5] == 'O') ||
               (tablero[6] == 'O' && tablero[7] == 'O' && tablero[8] == 'O') ||
               (tablero[0] == 'O' && tablero[3] == 'O' && tablero[6] == 'O') ||
               (tablero[1] == 'O' && tablero[4] == 'O' && tablero[7] == 'O') ||
               (tablero[2] == 'O' && tablero[5] == 'O' && tablero[8] == 'O') ||
               (tablero[0] == 'O' && tablero[4] == 'O' && tablero[8] == 'O') ||
               (tablero[2] == 'O' && tablero[4] == 'O' && tablero[6] == 'O');
    }
}
