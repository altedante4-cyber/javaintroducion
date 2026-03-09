package Teatr;
public class Teatro {

    private Asiento[][] sala = new Asiento[5][8];

    public Teatro() {
        // Inicializar cada celda con un nuevo objeto Asiento
        for (int i = 0; i < sala.length; i++) {
            for (int j = 0; j < sala[i].length; j++) {
                sala[i][j] = new Asiento();
            }
        }
    }

    public void reservarAsiento(int fila, int columna, String nombre) {
        // Validación dinámica usando las dimensiones de la matriz
        if (fila >= 0 && fila < sala.length && columna >= 0 && columna < sala[0].length) {
            if (!sala[fila][columna].estaReservado()) {
                sala[fila][columna].reservar(nombre);
                System.out.println("Asiento reservado para " + nombre);
            } else {
                System.out.println("Error: El asiento ya está ocupado.");
            }
        } else {
            System.out.println("Error: Fila o columna inválida.");
        }
    }

    public void mostrarMapaAsientos() {
        System.out.println("\n--- Mapa de Asientos ---");
        System.out.print("    ");
        // Cabecera de columnas
        for (int col = 1; col <= sala[0].length; col++) System.out.print(col + "  ");
        System.out.println();

        // Recorrido de la matriz
        for (int i = 0; i < sala.length; i++) {
            System.out.print((i + 1) + " "); 
            for (int j = 0; j < sala[i].length; j++) {
                if (sala[i][j].estaReservado()) {
                    System.out.print("[X] ");
                } else {
                    System.out.print("[ ] ");
                }
            }
            System.out.println();
        }
    }

    // Nuevo método para practicar el recorrido de matrices y lógica
    public int contarAsientosLibres() {
        int contador = 0;
        for (int i = 0; i < sala.length; i++) {
            for (int j = 0; j < sala[i].length; j++) {
                if (!sala[i][j].estaReservado()) {
                    contador++;
                }
            }
        }
        return contador;
    }

    public static void main(String[] args) {
        Teatro miTeatro = new Teatro();

        miTeatro.reservarAsiento(0, 2, "Juan");
        miTeatro.reservarAsiento(1, 4, "Maria");
        
        miTeatro.mostrarMapaAsientos();
        
        System.out.println("\nAsientos libres disponibles: " + miTeatro.contarAsientosLibres());
    }
}