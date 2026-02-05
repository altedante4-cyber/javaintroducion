package Juego2eva;

public class UsoTResEnRaya{


    private int posicion_jugador1;
    private char posicion_jugador [][] ;  


    public  UsoTResEnRaya (){
        this.posicion_jugador = new char [6][6];
    }



    public void  DibujarTablero(){


        for(int i = 0 ; i < 6; i++ ){

            for(int j = 0 ; j < 6 ; j++ ){

                  
                 if( j % 2 == 0 ){
                    System.out.print(this.posicion_jugador[i][j] = 'x' );
                     
                 }else{
                    System.out.print(this.posicion_jugador[i][j] = '|' );

                 }
                
            }

            System.out.println();
        }


    }






    



}
    

