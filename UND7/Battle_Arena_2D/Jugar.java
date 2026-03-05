package Battle_Arena_2D;

public class Jugar {

    public static void main(String[] args ){


        Personaje [][] tablero = new Personaje[3][3];


        tablero[0][0] = new Guerrero("Mikael", 100, 0, 40);
        tablero[0][1] = new Mago("Axelito" , 70 , 15);

        System.out.println("-------------ARENA DE BATALLA --- ");
        for(int  i = 0 ;  i < tablero.length ; i++ ){

            for (int j = 0  ; j < tablero[i].length  ; j++ ){

                if(tablero[i][j] ==null){

                    System.out.print(" [ Vacio ] ");

                }else{

                    //Polimorfismo puro : llamamo a atacar () sin import quien sea 
                     int danio = tablero[i][j].atacar();

                     //Dowcastin para el grito
                     if (tablero[i][j] instanceof Guerrero){
                         ((Guerrero) tablero[i][j]).lanzarGrito();

                     }

                     System.out.print(" [ " + tablero[i][j].getnombre() + " D: " + danio + " ] ") ;
                }

            }
                System.out.println(); //salto de linea 

        }



  
    }
    
}
