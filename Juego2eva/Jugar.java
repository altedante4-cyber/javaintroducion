package Juego2eva;

import java.util.Scanner;

public class Jugar {

    static Scanner entrada = new Scanner(System.in);
    static int ganadasJugador1 = 0;
    static int ganadasJugador2 = 0;
    static int erroresJugador1 = 0;
    static int erroresJugador2 = 0;
    static int empates = 0;

    public static void main(String[] args) {
        UsoTResEnRaya tablero = new UsoTResEnRaya();
        int opcion;

        do {
            tablero.iniciar(); // Entiendo que esto imprime el menú inicial
            opcion = entrada.nextInt();

            switch (opcion) {
                case 1:
                
                    int contador = 9; 
                    boolean turnoJ1 = true; 

                    tablero.DibujarTablero();

                    while (contador > 0) {
                        if (turnoJ1) {
                            System.out.println("Turno del Jugador 1. Seleccione posición:");
                        } else {
                            System.out.println("Turno del Jugador 2. Seleccione posición:");
                        }

                        int posicion = entrada.nextInt();

                        if (turnoJ1) {
                            // Intentamos mover al J1
                            if (tablero.mueveJugador1(posicion)) {
                                turnoJ1 = false;  // aqui cambiamos el turno con el jugador
                                contador--;
                            } else {
                                System.out.println("¡Error! Posición inválida o ocupada. Intenta de nuevo.");
                                erroresJugador1++;
                            }
                        } else {
                            // Intentamos mover al J2
                            if (tablero.mueveJugador2(posicion)) {
                                turnoJ1 = true; //cambio de turno con el jugador1 
                                contador--;
                            } else {
                                System.out.println("¡Error! Posición inválida o ocupada. Intenta de nuevo.");
                                erroresJugador2++;
                            }
                        }

                        tablero.DibujarTablero();
                        
                        // Aquí podrías añadir una comprobación de victoria:
                        // if (tablero.comprobarGanador()) { break; }
                    }
                    System.out.println("Partida finalizada.");
                    break;

                case 2:
                    System.out.println("Estadísticas:");
                    System.out.println("J1 Ganadas: " + ganadasJugador1);
                    System.out.println("J2 Ganadas: " + ganadasJugador2);
                    break;

                case 3:
                    System.out.println("Saliendo ......");
                    break;

                default:
                    System.out.println("Opción no válida.");
                    break;
            }

        } while (opcion != 3);
    }
}