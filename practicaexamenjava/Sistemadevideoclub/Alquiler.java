package Sistemadevideoclub;

public class Alquiler {
    
    private Pelicula mio ;
    private Cliente mio1 ; 
    private int minimo ;


    public Alquiler(Pelicula p , Cliente mio1  , int minimo ){

         this.mio = p ;
         this.mio1 = mio1 ; 
         diasAlquiler(minimo);
    }

    public void diasAlquiler(int minimo1){
          
        if(minimo1 < 0  ){
            this.minimo = 0 ; 
            System.out.println("Tienes que alquilarlo al menos un dia")
        }

        if (p.estaLibrePelicula()){
            this.minimo = minimo1 ;
        }else{
            System.out.println("El libro no esta disponible ");
        }



    }

    public double calcularPrecio(){
        //2.5 euros por dia 
        
    double   precio = this.minimo * 2.5;

        return precio ;  
        
    }

    


    public String toString(){

        return "La pelicula " + mio + " fue alquilado por " + mio1 + " por  " + minimo + " dias " + " por un precio de " + calcularPrecio();
    }

}
