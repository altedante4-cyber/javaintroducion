    package Juego2eva;

    import java.util.Scanner;
    import java.util.Random;
    public class Jugar {

        static Scanner entrada = new Scanner(System.in);
        static int ganadasJugador1 = 0;
        static int ganadasJugador2 = 0;
        static int erroresJugador1 = 0;
        static int erroresJugador2 = 0;
        static int empates = 0;

        public static void main(String[] args) {
            Random jugador_aleatorio = new Random();
            
            UsoTResEnRaya tablero = new UsoTResEnRaya();
            int opcion;
            do {
                tablero.iniciar(); // Entiendo que esto imprime el menú inicial
                opcion = entrada.nextInt();

                switch (opcion) {
                case 1:
    int contador = 9; 
    

    boolean turnoJ1 = true; 
    boolean partidaTerminada = false;


    //elegir aleatoriamente quien comiensa la partida 

    tablero.DibujarTablero();

    while (contador > 0 && !partidaTerminada) {
        if (turnoJ1) {
            System.out.println("Turno del Jugador 1. Seleccione posición:");
            int posicion = entrada.nextInt();

            if (tablero.mueveJugador1(posicion)) {
                tablero.DibujarTablero();
                // Validamos si ha ganado J1
                if (tablero.ganajugador1()) {
                    System.out.println("¡Ha ganado el Jugador 1!");
                    tablero.reiniciar();

                    ganadasJugador1++;
                    partidaTerminada = true;
                } else {
                    turnoJ1 = false; // Solo cambiamos turno si no ha ganado
                    contador--;
                }
            } else {
                System.out.println("¡Error! Posición inválida u ocupada.");
                erroresJugador1++;
            }
        } else {
            System.out.println("Turno del Jugador 2. Seleccione posición:");
            int posicion = entrada.nextInt();            
            if (tablero.mueveJugador2(posicion)) {
                tablero.DibujarTablero();
                // Validamos si ha ganado J2
                if (tablero.ganaJugador2()) {
                    System.out.println("¡Ha ganado el Jugador 2!");
                    tablero.reiniciar();
                    ganadasJugador2++;
                    partidaTerminada = true;
                } else {
                    turnoJ1 = true;
                    contador--;
                }
            } else {
                System.out.println("Error posición inválida u ocupada.");
                erroresJugador2++;
            }
        }

        // Si se acaban los movimientos y nadie ha ganado
        // if (contador == 0 && !partidaTerminada) {
        //     System.out.println("¡Empate!");
        //     empates++;
        // }

        if(tablero.hayEmpate()){
            System.out.println("empates");
        }
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

      case 4: 
    System.out.println("--- DUELO AUTOMÁTICO DE ORDENADORES ---");
    tablero.iniciar(); 
    
        boolean turnoJ1s = jugador_aleatorio.nextBoolean(); 
        System.out.println("Empieza el Ordenador " + (turnoJ1s ? "1 (X)" : "2 (O)"));

    while (tablero.quedanMovimientos() && !tablero.ganajugador1() && !tablero.ganaJugador2()) {
        if (turnoJ1s) {
            tablero.mueveOrdenador1();
            System.out.println("Ordenador 1 mueve:");
        } else {
            tablero.mueveOrdenador2();
            System.out.println("Ordenador 2 mueve:");
        }
        
        tablero.DibujarTablero();
        System.out.println("*****************");

        // Cambiamos el turno para la siguiente iteración
        turnoJ1 = !turnoJ1s;
    }

    // Comprobación de resultados finales
    if (tablero.ganajugador1()) {
        System.out.println("¡Victoria para el Ordenador 1!");
        ganadasJugador1++;
    } else if (tablero.ganaJugador2()) {
        System.out.println("¡Victoria para el Ordenador 2!");
        ganadasJugador2++;
    } else {
        System.out.println("¡Empate técnico!");
        empates++;
    }
    break;

                    default:
                        System.out.println("Opción no válida.");
                        break;
                }

            } while (opcion != 3);
        }
    }