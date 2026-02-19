public class Raices {
    private int a , b ,c ; 

    public Raices(int a , int b , int c  ){

        this.a = a ; 
        this.b =  b ; 
        this.c = c ; 
    }


    public void obtenerRaices(){

        int solucion_a = -this.b - getDiscriminante() ;
        int solucionn_b = -this.c - getDiscriminante();


        if(solucion_a.tieneRaices() && solucionn_b.tieneRaices){

        }

        System.out.println(solucion_a);
        System.out.println(solucionn_b);
        

    }


    public void obtenerRaiz(){
        

    }


    public double getDiscriminante(){

        double descriminador = Math.sqrt(Math.pow(this.b, 2) - 4 * this.a * this.c );

        return descriminador ; 
    }


    public boolean tieneRaices(){

        double descriminador = -this.b - getDiscriminante();
        double descriminador_2 = -this.b + getDiscriminante();


        
        if(descriminador > 0 && descriminador_2 > 0  ){
            return true ; 
        }
    return false ;
    }


    public boolean tieneRaiz(){

        if( getDiscriminante() == 0 ){
            return true ;
        }

        return  false ; 
    }

    public void calcular(){

        System.out.println("Tiene dos soluciones " + obtenerRaices());
        System.out.println("Tiene una unica solucion " + obtenerRaiz());
    }

    
    
}
