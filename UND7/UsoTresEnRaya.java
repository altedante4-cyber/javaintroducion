
import java.util.Scanner;
import java.util.Random;

public class UsoTresEnRaya {

    static Scanner entrada = new Scanner(System.in);
    static Random random = new Random();

    static int ganadasJugador1 = 0;
    static int ganadasJugador2 = 0;
    static int empates = 0;

    public static void main(String[] args) {

        TresEnRaya tablero = new TresEnRaya();
        int opcion;

        do {
            System.out.println("\n1. 2 Jugadores");
            System.out.println("2. Jugador vs Maquina");
            System.out.println("3. Maquina  vs Maquina");
            System.out.println("4. Mostrar estadísticas");
            System.out.println("5. Salir");
            System.out.println("6.Ver la partida anterior ");
            System.out.print("Elige opción: ");

            opcion = entrada.nextInt();

            switch (opcion) {

                case 1:
                    jugarDosJugadores(tablero);
                    break;

                case 2:
                    jugarVsMaquina(tablero);
                    break;

                case 3:
                    jugarMaquinaVsMaquina(tablero);
                    break;

                case 4:
                    mostrarEstadisticas();
                    break;

                case 5:
                    System.out.println("Saliendo...");
                    break;

                case 6:
                    tablero.Vertableroespejo();
                    break ;

                default:
                    System.out.println("Opción no válida.");
            }

        } while (opcion != 5);
    }

    //

/*

Contador de tiempo/intentos: Añade una variable que cuente cuántas veces un jugador intenta poner una ficha en una casilla ocupada. 
Si un jugador se equivoca 3 veces en el mismo turno, pierde el turno automáticamente.*/
    // 

  
    public static void jugarDosJugadores(TresEnRaya tablero) {

        tablero.iniciar();
        boolean turnoJ1 = true;
   // el ejercicio va que le avise al jugador cuadno le quedden solo dos intentos 
        int contador = 0 ; 
        int guardar_primera_posicion = 0 ; 
        int contador_intentos_invalidos = 0 ; 
      
        while (tablero.quedanMovimientos()
                && !tablero.ganaJugador1()
                && !tablero.ganaJugador2()) {

            tablero.DibujarTablero();

         if (turnoJ1) {
    System.out.print("Jugador 1 (X), posición: ");
    int pos = entrada.nextInt();

    if (tablero.mueveJugador1(pos)) {
        // SI EL MOVIMIENTO ES VÁLIDO
        turnoJ1 = false; // Cambia el turno normal
        contador_intentos_invalidos = 0; // Resetea sus fallos
        contador++; // Aumenta el contador de fichas puestas en el tablero

        if(contador ==  1){
            guardar_primera_posicion = pos ; 
        }

    } else {
        // SI EL MOVIMIENTO ES INVÁLIDO
        contador_intentos_invalidos++;
        System.out.println("Movimiento inválido. Intento " + contador_intentos_invalidos + " de 3.");

        if (contador_intentos_invalidos == 3) {
            System.out.println("¡HAS FALLADO 3 VECES! Pierdes el turno.");
            turnoJ1 = false; // <--- AQUÍ CAMBIAMOS AL JUGADOR 2
            contador_intentos_invalidos = 0; // <--- RESETEAMOS PARA EL SIGUIENTE
        }
    }
} else {
                System.out.print("Jugador 2 (O), posición: ");
                int pos = entrada.nextInt();

                if (tablero.mueveJugador2(pos)){
                    

                    contador_intentos_invalidos = 0  ; //reseteamos 
                    turnoJ1 = true;
                    contador ++ ; // AUMENTAMOS EL COANTDOR DE FICHAS PUESTAS EN EL TABLERO

                    if (contador == 2 ){
                        guardar_primera_posicion = pos ; 
                    }

                }  else{

                    contador_intentos_invalidos ++ ; 
                    System.out.println("Movimiento inválido.");


                    if (contador_intentos_invalidos == 3 ){
             System.out.println("¡HAS FALLADO 3 VECES! Pierdes el turno.");
            turnoJ1 = true ; // <--- AQUÍ CAMBIAMOS AL JUGADOR 2
            contador_intentos_invalidos = 0; // <--- RESETEAMOS PARA EL SIGUIENTE
                        
                    }

                }
                    
            }



            switch (contador) {
                case 6 :
                    System.out.println("Te quedan 2 intentos ");
                    // desaparece una ficha del tablero 
                    // creamos un metodo en la clase treneraya donde le pasos por parametro el penultimo o cualquier moviemitneot que haya hecho e ljugador y el lo tiene que eliminar de la tabla actual
                    /// necesitamos saber que jugador esta   cuando llegamos al contador 6 segun ese jugador tenemos que eliminar la ficha
                    /// 
                    /// 
                    if(turnoJ1){   // aqui sabemos que es el jugador1  ahora el problem,a vine para saber cual es la primera posicion donde ha puesto ese jugador 
                        
                        // ponemos una condiicon si contador 1  guardamos esa posicion que luego nos va a servir 
                        tablero.eliminarFichae(guardar_primera_posicion);

                    }else{

                        tablero.eliminarFichae(guardar_primera_posicion);

                    }
                    break;
                case 7 :
                    System.out.println("Te quedan 1 intentos mas ");
                    break ;                 
                case 8:
                    System.out.println("ES TU ULTIMO INTENTO COMPA ");
                    break;
                    default:
                    break;
            }

            

       

           


        }

        tablero.DibujarTablero();
        comprobarResultado(tablero);
    }

    public static void jugarVsMaquina(TresEnRaya tablero) {

        tablero.iniciar();
        boolean turnoJ1 = random.nextBoolean();

        System.out.println("Empieza: " + (turnoJ1 ? "Jugador" : "Máquina"));

        while (tablero.quedanMovimientos()
                && !tablero.ganaJugador1()
                && !tablero.ganaJugador2()) {

            tablero.DibujarTablero();

            if (turnoJ1) {
                System.out.print("Jugador (X), posición: ");
                int pos = entrada.nextInt();
                if (tablero.mueveJugador1(pos))
                    turnoJ1 = false;
            } else {
                System.out.println("Máquina mueve...");
                tablero.mueveOrdenador2();
                turnoJ1 = true;
            }
        }

        tablero.DibujarTablero();
        comprobarResultado(tablero);
    }

    public static void jugarMaquinaVsMaquina(TresEnRaya tablero) {

        tablero.iniciar();
        boolean turnoJ1 = random.nextBoolean();

        while (tablero.quedanMovimientos()
                && !tablero.ganaJugador1()
                && !tablero.ganaJugador2()) {

            tablero.DibujarTablero();

            if (turnoJ1) {
                System.out.println("Máquina 1 mueve...");
                tablero.mueveOrdenador1();
            } else {
                System.out.println("Máquina 2 mueve...");
                tablero.mueveOrdenador2();
            }

            turnoJ1 = !turnoJ1;

        }

        tablero.DibujarTablero();
        comprobarResultado(tablero);
    }

    public static void comprobarResultado(TresEnRaya tablero) {

        if (tablero.ganaJugador1()) {
            System.out.println("¡Gana Jugador 1!");
            ganadasJugador1++;
        } else if (tablero.ganaJugador2()) {
            System.out.println("¡Gana Jugador 2!");
            ganadasJugador2++;
        } else {
            System.out.println("¡Empate!");
            empates++;
        }
    }

    public static void mostrarEstadisticas() {
        System.out.println("\nEstadísticas:");
        System.out.println("Jugador 1: " + ganadasJugador1);
        System.out.println("Jugador 2: " + ganadasJugador2);
        System.out.println("Empates: " + empates);
    }
}