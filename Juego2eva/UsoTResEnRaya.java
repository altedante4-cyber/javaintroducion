package Juego2eva;

public class UsoTResEnRaya {

    private char tablero[][];
    private int intentos;

    public UsoTResEnRaya() {
        this.tablero = new char[3][3];
        this.intentos = 6;

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                this.tablero[i][j] = ' ';
            }
        }
    }

    public void DibujarTablero() {
        for (int i = 0; i < this.tablero.length; i++) {
            for (int j = 0; j < this.tablero[i].length; j++) {
                System.out.print(" " + tablero[i][j] + " ");
                if (j < tablero[i].length - 1) System.out.print("|");
            }
            System.out.println();
            if (i < tablero.length - 1) {
                System.out.println("-----------");
            }
        }
    }

   public boolean movimientoValido(int posicion) {
    switch(posicion) {
        case 1:
            return this.tablero[0][0] == ' ';
        case 2:
            return this.tablero[0][1] == ' ';
        case 3:
            return this.tablero[0][2] == ' ';
        case 4:
            return this.tablero[1][0] == ' ';
        case 5:
            return this.tablero[1][1] == ' ';
        case 6:
            return this.tablero[1][2] == ' ';
        case 7:
            return this.tablero[2][0] == ' ';
        case 8:
            return this.tablero[2][1] == ' ';
        case 9:
            return this.tablero[2][2] == ' ';
        default:
            return false; // Posición inválida (fuera de 1-9)
    }
}
public boolean mueveJugador1(int pos) {
    if (!movimientoValido(pos)) {
        return false; // Movimiento inválido
    }
    
    switch(pos) {
        case 1:
            this.tablero[0][0] = 'x';
            break;
        case 2:
            this.tablero[0][1] = 'x';
            break;
        case 3:
            this.tablero[0][2] = 'x';
            break;
        case 4:
            this.tablero[1][0] = 'x';
            break;
        case 5:
            this.tablero[1][1] = 'x';
            break;
        case 6:
            this.tablero[1][2] = 'x';
            break;
        case 7:
            this.tablero[2][0] = 'x';
            break;
        case 8:
            this.tablero[2][1] = 'x';
            break;
        case 9:
            this.tablero[2][2] = 'x';
            break;
    }
    return true; // Movimiento exitoso
}
public boolean mueveJugador2(int pos) {
    if (!movimientoValido(pos)) {
        return false; // Movimiento inválido
    }
    
    switch(pos) {
        case 1:
            this.tablero[0][0] = 'o';
            break;
        case 2:
            this.tablero[0][1] = 'o';
            break;
        case 3:
            this.tablero[0][2] = 'o';
            break;
        case 4:
            this.tablero[1][0] = 'o';
            break;
        case 5:
            this.tablero[1][1] = 'o';
            break;
        case 6:
            this.tablero[1][2] = 'o';
            break;
        case 7:
            this.tablero[2][0] = 'o';
            break;
        case 8:
            this.tablero[2][1] = 'o';
            break;
        case 9:
            this.tablero[2][2] = 'o';
            break;
    }
    return true; // Movimiento exitoso
}

    public boolean ganajugador1() {
        // Filas horizontales
        if (this.tablero[0][0] == 'x' && this.tablero[0][1] == 'x' && this.tablero[0][2] == 'x') return true;
        if (this.tablero[1][0] == 'x' && this.tablero[1][1] == 'x' && this.tablero[1][2] == 'x') return true;
        if (this.tablero[2][0] == 'x' && this.tablero[2][1] == 'x' && this.tablero[2][2] == 'x') return true;
        
        // Columnas verticales
        if (this.tablero[0][0] == 'x' && this.tablero[1][0] == 'x' && this.tablero[2][0] == 'x') return true;
        if (this.tablero[0][1] == 'x' && this.tablero[1][1] == 'x' && this.tablero[2][1] == 'x') return true;
        if (this.tablero[0][2] == 'x' && this.tablero[1][2] == 'x' && this.tablero[2][2] == 'x') return true;
        
        // Diagonales
        if (this.tablero[0][0] == 'x' && this.tablero[1][1] == 'x' && this.tablero[2][2] == 'x') return true;
        if (this.tablero[2][0] == 'x' && this.tablero[1][1] == 'x' && this.tablero[0][2] == 'x') return true;
        
        return false;
    }

    public boolean ganaJugador2() {
        // Filas horizontales
        if (this.tablero[0][0] == 'o' && this.tablero[0][1] == 'o' && this.tablero[0][2] == 'o') return true;
        if (this.tablero[1][0] == 'o' && this.tablero[1][1] == 'o' && this.tablero[1][2] == 'o') return true;
        if (this.tablero[2][0] == 'o' && this.tablero[2][1] == 'o' && this.tablero[2][2] == 'o') return true;
        
        // Columnas verticales
        if (this.tablero[0][0] == 'o' && this.tablero[1][0] == 'o' && this.tablero[2][0] == 'o') return true;
        if (this.tablero[0][1] == 'o' && this.tablero[1][1] == 'o' && this.tablero[2][1] == 'o') return true;
        if (this.tablero[0][2] == 'o' && this.tablero[1][2] == 'o' && this.tablero[2][2] == 'o') return true;
        
        // Diagonales
        if (this.tablero[0][0] == 'o' && this.tablero[1][1] == 'o' && this.tablero[2][2] == 'o') return true;
        if (this.tablero[2][0] == 'o' && this.tablero[1][1] == 'o' && this.tablero[0][2] == 'o') return true;
        
        return false;
    }

    // Método para verificar si hay empate (tablero lleno)
    public boolean hayEmpate() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (this.tablero[i][j] == ' ') {
                    return false; // Hay al menos una casilla vacía
                }
            }
        }
        return true; // Tablero lleno
    }

    // Método para resetear el juego
    public void reiniciar() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                this.tablero[i][j] = ' ';
            }
        }
    }

    // Método para obtener el estado actual del tablero
    public char[][] getTablero() {
        return this.tablero;
    }

    public void mueveOrdenador1() {
        // TODO: Implementar lógica del ordenador
    }

    public void mueveOrdenador2() {
        // TODO: Implementar lógica del ordenador
    }

    public void iniciar() {
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
}