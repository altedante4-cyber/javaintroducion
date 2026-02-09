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

                    default:
                        System.out.println("Opción no válida.");
                        break;
                }

            } while (opcion != 3);
        }
    }