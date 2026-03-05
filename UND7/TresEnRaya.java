

import java.util.Random;

public class TresEnRaya {

    private int[][] tablero = new int [3][3];
    private int [] [] tablero_espejo = new int [3][3];

    private Random random;

    // Constructor
    public TresEnRaya() {
        random = new Random();
        iniciar();
    }

    // Inicializa tablero
    public void iniciar() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                tablero[i][j] = 0;
            }
        }

        /// segundo tablero espejo
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                tablero_espejo[i][j] = 0;
            }
        }

    }

    public  int[] convertirPosicion(int pos) {

        int fila = 0;
        int col = 0;

        switch (pos) {
            case 1: fila = 0; col = 0; break;
            case 2: fila = 0; col = 1; break;
            case 3: fila = 0; col = 2; break;
            case 4: fila = 1; col = 0; break;
            case 5: fila = 1; col = 1; break;
            case 6: fila = 1; col = 2; break;
            case 7: fila = 2; col = 0; break;
            case 8: fila = 2; col = 1; break;
            case 9: fila = 2; col = 2; break;
        }

        return new int[]{fila, col};
    }

    public boolean movimientoValido(int pos) {

        if (pos < 1 || pos > 9)
            return false;

        int[] c = convertirPosicion(pos);

        if (tablero[c[0]][c[1]] == 0)
            return true;
        else
            return false;
    }

    public boolean mueveJugador1(int pos) {

        if (!movimientoValido(pos))
            return false;

        switch (pos) {
            case 1: tablero[0][0]  = 1; break;
            case 2: tablero[0][1]   = 1; break;
            case 3: tablero[0][2] = 1; break;
            case 4: tablero[1][0] = 1; break;
            case 5: tablero[1][1] = 1; break;
            case 6: tablero[1][2]  = 1; break;
            case 7: tablero[2][0]  = 1; break;
            case 8: tablero[2][1] = 1; break;
            case 9: tablero[2][2] =  1; break;
        }
         switch (pos) {
            case 1: tablero_espejo[0][0] = 1; break;
            case 2: tablero_espejo[0][1] = 1; break;
            case 3:  tablero_espejo[0][2] = 1; break;
            case 4: tablero_espejo[1][0]= 1; break;
            case 5:  tablero_espejo[1][1]= 1; break;
            case 6:  tablero_espejo[1][2] = 1; break;
            case 7:   tablero_espejo[2][0]= 1; break;
            case 8:  tablero_espejo[2][1]= 1; break;
            case 9: tablero_espejo[2][2]= 1; break;
        }

        return true;
    }

    public boolean mueveJugador2(int pos) {

        if (!movimientoValido(pos))
            return false;

        switch (pos) {
            case 1: tablero[0][0] = 2; break;
            case 2: tablero[0][1] = 2; break;
            case 3: tablero[0][2] = 2; break;
            case 4: tablero[1][0] = 2; break;
            case 5: tablero[1][1] = 2; break;
            case 6: tablero[1][2] = 2; break;
            case 7: tablero[2][0] = 2; break;
            case 8: tablero[2][1] = 2; break;
            case 9: tablero[2][2] = 2; break;
        }

          switch (pos) {
            case 1: tablero_espejo[0][0]= 2; break;
            case 2:  tablero_espejo[0][0]= 2; break;
            case 3:  tablero_espejo[0][2]= 2; break;
            case 4:  tablero_espejo[1][0]= 2; break;
            case 5: tablero_espejo[1][1]= 2; break;
            case 6:  tablero_espejo[1][2]= 2; break;
            case 7:  tablero_espejo[2][0]= 2; break;
            case 8:  tablero_espejo[2][1]= 2; break;
            case 9:  tablero_espejo[2][2]= 2; break;
        }

        return true;
    }

    private boolean comprobarGanador(int jugador) {

        // Filas
        if (tablero[0][0] == jugador)
            if (tablero[0][1] == jugador)
                if (tablero[0][2] == jugador)
                    return true;

        if (tablero[1][0] == jugador)
            if (tablero[1][1] == jugador)
                if (tablero[1][2] == jugador)
                    return true;

        if (tablero[2][0] == jugador)
            if (tablero[2][1] == jugador)
                if (tablero[2][2] == jugador)
                    return true;

        // Columnas
        if (tablero[0][0] == jugador)
            if (tablero[1][0] == jugador)
                if (tablero[2][0] == jugador)
                    return true;

        if (tablero[0][1] == jugador)
            if (tablero[1][1] == jugador)
                if (tablero[2][1] == jugador)
                    return true;

        if (tablero[0][2] == jugador)
            if (tablero[1][2] == jugador)
                if (tablero[2][2] == jugador)
                    return true;

        // Diagonales
        if (tablero[0][0] == jugador)
            if (tablero[1][1] == jugador)
                if (tablero[2][2] == jugador)
                    return true;

        if (tablero[0][2] == jugador)
            if (tablero[1][1] == jugador)
                if (tablero[2][0] == jugador)
                    return true;

        return false;
    }

    public boolean ganaJugador1() {
        return comprobarGanador(1);

        
    }

    public void eliminarFichae(int pos ) {

        //tenemos que pasarle unas coredenada para que lo desmarque

        switch (pos) {
            case 1: tablero[0][0]  = 0; break;
            case 2: tablero[0][1]   = 0 ; break;
            case 3: tablero[0][2] = 0; break;
            case 4: tablero[1][0] = 0 ; break;
            case 5: tablero[1][1] = 0; break;
            case 6: tablero[1][2]  = 0; break;
            case 7: tablero[2][0]  = 0; break;
            case 8: tablero[2][1] = 0; break;
            case 9: tablero[2][2] =  0; break;
        }

    }


    // crear un metodo que muestre el procentaje de victorias del J1 

    
    public boolean ganaJugador2() {
        return comprobarGanador(2);
    }

    
    public boolean quedanMovimientos() {

        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (tablero[i][j] == 0)
                    return true;

        return false;
    }

   
    public void mueveOrdenador1() {
        int pos;
        do {
            pos = random.nextInt(9) + 1;
        } while (!movimientoValido(pos) && quedanMovimientos());

        if (quedanMovimientos())
            mueveJugador1(pos);
    }

    public void mueveOrdenador2() {
        int pos;
        do {
            pos = random.nextInt(9) + 1;
        } while (!movimientoValido(pos) && quedanMovimientos());

        if (quedanMovimientos())
            mueveJugador2(pos);
    }

    public void Vertableroespejo(){



for (int i = 0; i < 3; i++) {

            for (int j = 0; j < 3; j++) {

                if (tablero_espejo[i][j] == 1)
                    System.out.print(" X ");
                else if (tablero_espejo[i][j] == 2)
                    System.out.print(" O ");
                else
                    System.out.print("   ");

                if (j < 2) System.out.print("|");
            }

            System.out.println();
            if (i < 2)
                System.out.println("-----------");
        }
       
    }

        
        
    

    
    public void DibujarTablero() {
 for (int i = 0; i < 3; i++) {

            for (int j = 0; j < 3; j++) {

                if (tablero[i][j] == 1)
                    System.out.print(" X ");
                else if (tablero[i][j] == 2)
                    System.out.print(" O ");
                else
                    System.out.print("   ");

                if (j < 2) System.out.print("|");
            }

            System.out.println();
            if (i < 2)
                System.out.println("-----------");
        }
       
    }

}
