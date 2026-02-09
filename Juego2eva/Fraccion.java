package Juego2eva;

public class Fraccion {

    private int numerador, denominador ; 
    
    public Fraccion(int numerador , int denominador  ){
         
         this.numerador = numerador ;
         this.denominador = denominador;
    
    
    }

    public int damenumerador(){
        return this.numerador;
    }
    public int damedenomidor(){

        return this.denominador;
    }

    public Fraccion sumarFraccion(Fraccion f2 ){

        int denominadortotal = this.denominador * f2.damedenomidor();

        int numerador1 = (denominadortotal / this.denominador) * this.numerador + (denominadortotal / f2.damedenomidor() ) * f2.damenumerador() ;
 
        
        Fraccion rsdo = new Fraccion(numerador1, denominadortotal);

        return rsdo ; 
    }

    public Fraccion diviFraccion(Fraccion f2 ){

         int n = this.numerador*f2.damedenomidor();
        int d =this.denominador*f2.damenumerador();

        Fraccion rsdo = new Fraccion(n, d);
        
        return rsdo ; 


    }

     public Fraccion restaFraccion(Fraccion f2 ){

          int denominadortotal = this.denominador * f2.damedenomidor();

        int numerador1 = (denominadortotal / this.denominador) * this.numerador - (denominadortotal / f2.damedenomidor() ) * f2.damenumerador() ;
 
        
        Fraccion rsdo = new Fraccion(numerador1, denominadortotal);

        return rsdo ; 


    }


    

    public Fraccion multFraccion(Fraccion f2 ){

        int n = this.numerador*f2.damenumerador();
        int d =this.denominador*f2.damedenomidor();

        Fraccion rsdo = new Fraccion(n, d);
        
        return rsdo ; 
    }


    public String toString(){

        return this.numerador + "/" + this.denominador ;
    }




}
