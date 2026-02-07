package pruebas2;
import java.util.Random;
public class Password {

    private int longitud;
    private String contrasena ;
    
    Random ran = new Random();
    char abe [] = {'a','e','i','o','u','1','2','3','4'};

    //creamos el constructor
    // constructor por defecto
    public Password(int longitud , String contrasena){

        this.longitud=8;
        this.contrasena = contrasena;

    }
    //contructor  que le pasems nostros la longitud 

    public Password(int longitud){
       
        this.longitud=longitud;
        this.contrasena=getgenerarcontrasena();
    }

     // comprobamos si la contrasena es fuerte con el siguiente metodo 

     public boolean esFuerte(){
        
        int contador_mayuscular = 0 ; 
        int contador_minusculas = 0 ; 
        int contador_numeros = 0 ; 

        for(int i = 0 ; i < contrasena.length() ; i++ ){
              char c = contrasena.charAt(i);
              
              if ( c >= 'A' || c <= 'Z'){
                     contador_mayuscular ++;
              }else if ( c >= 'a' || c <= 'z'){
                    contador_minusculas ++;
              }else{
                contador_numeros++ ;
              }
              
        }

        if(contador_mayuscular >= 2 && contador_minusculas >= 1 && contador_numeros >= 5 ){
              return true;
        }
        return false;
     }

     public void setmodificarlongitud(int longitud){
        this.longitud=longitud;
     }

     //generar contrasena 

     public String  getgenerarcontrasena(){
           //generar una contrasena aleatoria con esa longitud 
        String contrasena_generada = "";
        
        for (int i = 0 ; i < longitud ; i++ ){
            int generar_contrasena = ran.nextInt(abe.length);
            contrasena_generada += abe[generar_contrasena];
        }
        return contrasena_generada;
        
     }
    //mostramos la contrasena con tostring

    public String toString(){

        return contrasena;
    }


    
}
