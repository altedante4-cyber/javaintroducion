import java.util.Scanner;
import java.util.Random;


public class juego {
     static String palabras[] = {
        "arbol", "banco", "atomo", "clase", "color",
        "dados", "dulce", "exito", "feliz", "fugaz",
        "gente", "goles", "jugar", "labio", "lapiz",
        "libro", "clavo", "nubes", "perro", "playa"
    };

    static int numIntentosConsumidos = 0;
    static Scanner sc = new Scanner(System.in);
    static Random leter = new Random();
    static int elegir_palabra = leter.nextInt(palabras.length);
    static String usuario = null;
    static String palabraSecreta = generaPalabra(palabras, elegir_palabra);
    static int numLetrasAdivinadas = 0;
    static int partidas_ganadas_maquina = 0;
    public static void main(String[] args) {
        char opcion;
        char[] caracteresEspeciales = {
            '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
            '{', '}', '[', ']', '|', '\\', ':', ';', '"', '\'', '<', '>', ',', '.', '?', '/',
            '¿', '¡', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
        };
        char[] consonantes = {
            'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
            'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'
        };
        char vocales_comprobar[] = {'a', 'e', 'i', 'o', 'u'};
        char palabras_no_admitidas_ultimo_caracter[] = {'q', 'w', 'x'};
        int contador_partidas = 0;
        do {
            System.out.println("\n--- JUEGO DE PALABRAS ---");
            System.out.println("Desea jugar una partida s(si) o n(no)");
            opcion = sc.nextLine().toLowerCase().charAt(0);


            if (opcion == 's') {
                // ESTA PARTE ES PARA EL REINICIO DE PARTIDA PARA CUANDO EL USUARIO QUIERA JUGAR OTRA PARTIDA
                numIntentosConsumidos = 0;
                elegir_palabra = leter.nextInt(palabras.length);
                palabraSecreta = generaPalabra(palabras, elegir_palabra);
                usuario = null;


               
                while (numIntentosConsumidos < 6) {
                    boolean salir_bucle_errores = false;
                    int contador_interno = 0;
                   
                    // variables de error reseteadas para cada nueva palabra introducida
                    boolean no_tiene_vocales = false;
                    boolean tiene_caracteres_especiales = false;
                    boolean encontrado_consonantes = false;
                    boolean encontrado_palabra_no_admitida = false;


                    do {
                        tiene_caracteres_especiales = false;
                        encontrado_consonantes = false;
                        encontrado_palabra_no_admitida = false;


                        System.out.println("\nIntento " + (numIntentosConsumidos + 1) + "/6");
                        System.out.println("Ingrese la palabra (5 letras y 2-3 vocales):");
                        usuario = sc.nextLine().toLowerCase();

                        if (usuario.length() != 5) {
                            System.out.println("Error: Debe tener exactamente 5 letras.");
                            contador_interno++;
                        } else {
                            // Validar cantidad de vocales
                            int contador_vocales = 0;
                            for (int i = 0; i < usuario.length(); i++) {
                                char c = usuario.charAt(i);
                                for (int j = 0; j < vocales_comprobar.length; j++) {
                                    if (c == vocales_comprobar[j]) {
                                        contador_vocales++;
                                    }
                                }
                            }


                            if (contador_vocales < 2 || contador_vocales > 3) {
                                System.out.println("Error: Debe contener entre 2 y 3 vocales.");
                                no_tiene_vocales = true;
                                contador_interno++;
                            } else {
                                no_tiene_vocales = false;
                            }


                            // Validar caracteres especiales o números
                            for (int i = 0; i < usuario.length(); i++) {
                                char c = usuario.charAt(i);
                                for (int k = 0; k < caracteresEspeciales.length; k++) {
                                    if (c == caracteresEspeciales[k] || c == ' ') {
                                        tiene_caracteres_especiales = true;
                                    }
                                }
                            }


                            // Validar consonantes seguidas (máximo 2)
                            int contadorConsonantesAux = 0;
                            for (int i = 0; i < usuario.length(); i++) {
                                char letra = usuario.charAt(i);
                                boolean esConsonante = false;
                                for (int j = 0; j < consonantes.length; j++) {
                                    if (letra == consonantes[j]) {
                                        esConsonante = true;
                                        break;
                                    }
                                }
                                if (esConsonante) {
                                    contadorConsonantesAux++;
                                    if (contadorConsonantesAux >= 3) {
                                        encontrado_consonantes = true;
                                    }
                                } else {
                                    contadorConsonantesAux = 0;
                                }
                            }


                            // Validar ultimo caracter prohibido
                            char ultimo = usuario.charAt(4);
                            for (int j = 0; j < palabras_no_admitidas_ultimo_caracter.length; j++) {
                                if (ultimo == palabras_no_admitidas_ultimo_caracter[j]) {
                                    encontrado_palabra_no_admitida = true;
                                }
                            }




                            // Validar vocales seguidas
                            int contdor_vocal_seguida = 0;
                            for (int i = 0; i < usuario.length(); i++) {
                                char c = usuario.charAt(i);
                                boolean esVocal = false;
                                for (int j = 0; j < vocales_comprobar.length; j++) {
                                    if (c == vocales_comprobar[j]) {
                                        esVocal = true;
                                    }
                                }
                                if (esVocal) {
                                    contdor_vocal_seguida++;
                                    if (contdor_vocal_seguida >= 2) {
                                        tiene_caracteres_especiales = true;
                                    }
                                } else {
                                    contdor_vocal_seguida = 0;
                                }
                            }
                        }


                        if(tiene_caracteres_especiales || encontrado_consonantes || encontrado_palabra_no_admitida ){
                            System.out.println("Tiene un formato invalido.Vuelva a introducir la cadena ");
                        }
                   
                        if (haTerminadoJuego(contador_interno)) {
                            salir_bucle_errores = true;
                        }


                    } while ((usuario.length() != 5 || no_tiene_vocales || tiene_caracteres_especiales || encontrado_consonantes || encontrado_palabra_no_admitida) && !salir_bucle_errores);


                    if (salir_bucle_errores) {
                        System.out.println("Demasiados errores de formato. Turno perdido.");
                        partidas_ganadas_maquina++;
                        break;
                    }


                    // Comprobar aciertos
                    char resultado[] = compruebaLetrasAcertadas(usuario);
                    System.out.print("Resultado: ");
                    for (int i = 0; i < resultado.length; i++) {
                        System.out.print(resultado[i]);
                    }
                    System.out.println();


                    if (haGanadoJugador(usuario)) {
                        System.out.println("¡Has acertado la palabra!");
                        numLetrasAdivinadas++;
                        break;
                    }


                    numIntentosConsumidos++;
                }


                if (numIntentosConsumidos == 6 && !haGanadoJugador(usuario)) {
                    System.out.println("Se acabaron los intentos. La palabra era: " + palabraSecreta);
                    partidas_ganadas_maquina++;
                }


                contador_partidas++;
                System.out.println("\nTú: " + numLetrasAdivinadas + " | Máquina: " + partidas_ganadas_maquina);
                System.out.println("Partidas jugadas: " + contador_partidas);
            }


        } while (opcion != 'n');


        System.out.println("FIN JUEGO");
    }


    public static boolean haGanadoJugador(String user) {
        if (user == null) return false;
        return user.equals(palabraSecreta);
    }


    public static boolean haTerminadoJuego(int cont) {
        return cont == 6;
    }


    public static char[] compruebaLetrasAcertadas(String user) {
        char resultado[] = new char[palabraSecreta.length()];


        // lo que hacemos con este for es rellenar resultado que es tipo char  con el string que ingreso el usuario
        for (int i = 0; i < user.length(); i++) {
            char letraUsuario = user.charAt(i);
            char letraSecreta = palabraSecreta.charAt(i);


            if (letraUsuario == letraSecreta) {
                resultado[i] = (char) (letraUsuario - 32); // Convertir a mayúscula
            } else {
                boolean existeEnOtraPosicion = false;
                for (int j = 0; j < palabraSecreta.length(); j++) {
                    if (letraUsuario == palabraSecreta.charAt(j)) {
                        existeEnOtraPosicion = true;
                    }
                }
                if (existeEnOtraPosicion) {
                    resultado[i] = letraUsuario;
                } else {
                    resultado[i] = '*';
                }
            }
        }
        return resultado;
    }


    public static String generaPalabra(String a[], int elegir_palabra) {
        return a[elegir_palabra];
    }
}

