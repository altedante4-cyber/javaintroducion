import java.util.Random;
public class Dron {

    private String modelo  , identificador  ;
    private int  carga_bateria ;
    private String estado ; 


    public Dron(String modelo , String  identificador ){
        this.modelo = modelo;
        this.identificador = getGeneraridentificador();
        this.carga_bateria = getGenerarbateria();
        this.estado = "base";
    }




 public String dameIdentificador(){

    return identificador ;
 }



 public int getGenerarbateria(){

    Random rand = new Random();

    int num = rand.nextInt(100) + 70 ; 

    return  num ; 
 }

 public String getGeneraridentificador(){

     String gen = "";

     for (int i = 0 ; i< this.modelo.length() ;i++ ){
                char c = this.modelo.charAt(i);
            if ( i < 3 ){

                gen += c ; 
            }
     }

     Random rand = new Random() ;


     int num = rand.nextInt(500)+ 1 ;

     gen += String.valueOf(num);


     return  gen ; 

 }

 public String toString(){

    return "El dron " + modelo + " con identificador  " + identificador + " con bateria " + carga_bateria + " se encuentra en " + estado ; 
 }

//  metdo para gasta bateria

public void setGastarBateria(int carga_bateria ){

    this.carga_bateria -= carga_bateria ;
}


/// metdo que verifque si el dron tiene poca bateria(considerando "poca") si es menor 15 %



    
}
