package Ejercicio4;

public class Electrodomestico {

    private double precio_base ;
    private String color ;
    private char Consumo_energetico ;
    private double peso ; 

    public Electrodomestico(){
         this.precio_base = 0 ;
        comprobarColor(color);
         this.Consumo_energetico = 0;
         this.peso = 0 ; 
    }
     public Electrodomestico(double precio_base , double peso  ){

            this.precio_base = precio_base  ;
             comprobarColor(color);
            this.Consumo_energetico = 'F';
            this.peso = peso ; 
    }




    


    public Electrodomestico(double precio_base , String color , char Consumo_energetico , double peso  ){

            this.precio_base = precio_base ;
             comprobarColor(color);
            this.Consumo_energetico = Consumo_energetico;
            this.peso = peso ; 
    }


    public void   comprobarColor(String color ){
           
         String colores_disponibles []= {"blanco","negro","rojo","azul","gris"};
         // pensar en utilizar el contains
         for (int i = 0 ; i < colores_disponibles.length ; i++ ){
              if (colores_disponibles.equals(color)){
                this.color = color ; 
              }
         }
         this.color = "blanco";
    }



    public boolean comprobarCOnsumoENergetico(char letra ){
         return letra == 'A' || letra == 'F'; // comprobar que devuelve la letra por defecto
    }

    public double precioFinal(){
          double precio_energetico = 0 ; 
          switch (Consumo_energetico) {
                 case 'A':
                        precio_energetico += 100; 
                break;
                     case 'B':
                     precio_energetico += 80 ; 
                break;
                case 'D':
                    precio_energetico += 60 ; 
                
                break;

                case 'E':

                     precio_energetico += 30 ; 
                
                break;

                case 'F':
                    precio_energetico += 10 ; 
                break;
            default:
                break;
          }

        if (peso >= 0 &&peso  <= 19 ) precio_energetico += 10 ;
        if (peso >= 20 &&peso  <= 49 ) precio_energetico += 50 ;
        if (peso >= 50 &&peso  <= 79 ) precio_energetico += 80;
        if (peso >= 80 ) precio_energetico += 100 ;

        
         return  this.precio_base + precio_energetico ; 
         
    }


    public double getprecio_base(){

        return precio_base ;
    }
    public double getpeso(){
        return peso ; 
    }

    public String getcolor(){
        return color;
    }

    public char getConsumoEnergetico(){
        return Consumo_energetico;

    }


    public String toString(){
        return "El electrodomestico  de color " + color + " con precio base  " + precio_base + " consumo energtetico  " + Consumo_energetico + " con un peso de   " + peso ; 
    }

}
