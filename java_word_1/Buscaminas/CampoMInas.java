package Buscaminas;

public class CampoMInas {

    private char[][] tableroOculto = new char [4][4];
    private char[][] tableroVisible = new char [4][4];


    public CampoMInas(){
         
        for(int i = 0 ; i < 4 ; i++ ){
             
            for(int j = 0 ; j < 4 ; j++ ){
                 
                  tableroOculto[i][j] = '.'; // espacio vacio por defecto 
                  tableroVisible[i][j] = '?'; // espacio vacio por defecto 

            }

        }

        // colocamos las minas manualmente

// Colocamos minas solo en la matriz oculta
        tableroOculto[0][1] = 'M';
        tableroOculto[2][3] = 'M';
        tableroOculto[3][0] = 'M';
    }


    public void revelarCasilla(int fila , int columna ){

        // validacion de limites para evitar eerorres 

        if (fila < 0 || fila >= 4 || columna < 0 || columna >= 4 ){
             System.out.println("COordenada fuera de rang ");
            return ; 
            }


        // logica de juego 

        if(tableroOculto[fila][columna] == 'M'){
             System.out.println("BOOM Perdiste ");
        }else{

              // revelamos la casilla copiando el contenido de la coulta a la visible
              tableroVisible[fila][columna] = tableroOculto[fila][columna];
              System.out.println("aaislla revelada "); 
           }

    }

    public void dibujarTableroVisible(){
          
        for(int i = 0 ; i < 4 ; i++ ){

            for(int j = 0 ; j < 4 ; j++ ){
                 
                  System.out.print(tableroVisible[i][j] + " ");
            }

            System.out.println();
        }

        }
    }




    

