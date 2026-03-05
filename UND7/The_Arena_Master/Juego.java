package The_Arena_Master;
import java.util.Scanner ; 
public class Juego {
    static    Scanner sc = new Scanner(System.in);
      static   Entidad [] [] mapa = new Entidad[4][4];
     
    public static void main(String[] args) {

        // 1. colocamos al gueerero en la posicon inicial

        Guerrero mika = new Guerrero("Mika", 0, 0, 100, 10, 5);


        mapa[0][0] = mika;

        boolean juegoTerminado = false; 
int antigua1_filaaux = 0;
             int antigua1_columan = 0;

        while (!juegoTerminado){

            // PASO1 MOSTRAR EL TABLERO (SOLO DIBUJAR)

            System.out.println("\n===TABLERO ACTUAL ===");

            for(int i = 0 ; i< mapa.length ; i++){

                for(int j = 0 ; j < mapa[i].length ; j++ ){

                    if(mapa[i][j] == null ){

                        System.out.print("[ -  ]");
                    }else{
                        System.out.print("[ "+mapa[i][j].getNombre() + " ] ");
                    }
                }
                System.out.println();
            }

            System.out.println("\n?A que fila quieres mover a mika? (0-3) ");
            int nuevaF = sc.nextInt();
            System.out.println("?A que COLUMNA quieres mover a mika ? (0-3)");
            int nuevaC = sc.nextInt();

            // // PASO 3: LOGICA DE MOVIMIENTO (La clave )
            // int antigua1_filaaux = 0;
            // int antigua1_columan = 0;



            // moverPersonaje(antigua1_filaaux , antigua1_columan,nuevaF,nuevaC)  ; 
            
            //  antigua1_filaaux = nuevaF;
            //  antigua1_columan = nuevaC;

            // POR QUE TUBE EL EEROR AQUI el probelma dle reset (cuidado con el while)
            // si esas variable s(antiuga1_gilax y antigua1_colum) estan dentro del bucle whiel,
            // cada vez que el codigo de una  vuelta vovlera a valor 0 

            // las variable int de antigua1_fila au y el otro tienen que ir fguera del bucle

             moverPersonaje(antigua1_filaaux , antigua1_columan,nuevaF,nuevaC);
             // 4actualizr el ratos (para que la proxima vez sepa donde viene)

             antigua1_filaaux = nuevaF;
             antigua1_columan = nuevaC;
        
        }
        }






        public static void moverPersonaje(int fOrigen ,int cOrigen , int fDestino , int cDestino ){
 // validar que no se salga del mapa
 
   if(fDestino >= 0 && fDestino < 4 && cDestino >= 0 && cDestino < 4 ){
        // Guardamos el personaje que se va a mover 
        Entidad  viajero = mapa[fOrigen][cOrigen];
        // limpiarmos la casilla natigua (esto es lo que buscabas)

        mapa[fOrigen][cOrigen] = null ; 

        // 4 lo poensmo en la nueva casilla 
        mapa[fDestino][cDestino] = viajero ; 

        System.out.println("Movimiento realizado con exito");
   }else{

    System.out.println("Error: Posicion fuera de rango ");
   }
}

}




