package Poo_ejerciio2_repasoEJ1;

public class Circulo extends Punto  {
    private int radio ; 

    public Circulo(int x , int y , int radio ){

        super(x , y );
        this.radio = radio ;
    }


    public void  verificarCuadrante(){

        if(getX() > 0 && getY() > 0 ){
             System.out.println("Es la zona de arriba a la dereha");
        }else if( getX() < 0 && getY() > 0 ){
            System.out.println("Es la zona de arriab a la izquierda ");
        }else if (getX() > 0 && getY() < 0 ){

             System.out.println("Es la zona de abajo a la derecha ");
        }else{
            System.out.println("Es la zona de abajo a la izquierda ");
        }
          
    }
    // METDO  ADICIONAL PARA DARLE UTILIDAD A LA CLASE

    public double calcularArea(){
        return Math.PI * Math.pow(radio,2 );
    }


    // cuadno dibujas unos ejes de corodenadas ( el eje AX horizontal y el eje
    // y  vertical ) el plano queda dividio en cuatro zonas infinitas 
    // esas zonas son las cuadradantes
    // para saber en que cuadrante esta un punto solo tienes que mirar los signos  de sus coordenadas
    // (x,y)
    /* cuadrante I => tanto la x como la y son positivas es la zona arriba a la derecha ejemplo (5,10)

    */
    public String toString(){

         // aprovechamos que es un punto para decir donde esta su centro 
         return "Circulo con centro ( " + getX() + "," + getY() + ") y rado " + radio ; 
    }




    
}
