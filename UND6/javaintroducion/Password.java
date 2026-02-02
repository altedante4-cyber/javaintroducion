package javaintroducion;
import java.util.Random;
public class Password {

    private int longitud;
    private String contrasena;
    //constructor por defct6o 
    public Password(){
        this.longitud = 8 ; 
        this.contrasena = getgenerarPassword();       
    
    }

    public Password(int longitud ){

        this.contrasena =null;
        this.longitud = longitud;
          
    }
    
    //necesitamos un metodo geter para devolver la longitud

    public int devolverlongitud(){

        return this.longitud; 
    }


     // creamos un seter que nos dara la password con la longiud que le passemos nosotros

     public void  setgenerarcontrasena(int longitud){
        
        Random lete = new Random();
        
        String palabras_numeros="0123456789qqwrtyuioppasdfghjkl;zxcvbnm";
        char palabras_utilizar [] = new char[palabras_numeros.length()];
        
        
        for(int i = 0 ; i < palabras_numeros.length() ;i++ ){
                char c = palabras_numeros.charAt(i);

                palabras_utilizar[i] = c ; 
        }
        
        
        for(int i = 0 ; i < longitud ;i++ ){
            int gerar_contrasena = lete.nextInt(palabras_utilizar.length);

             this.contrasena += palabras_utilizar[gerar_contrasena]; 
        }
    }


    public String getgenerarPassword(){

        String cont = setgenerarcontrasena(devolverlongitud());


        return cont ; 
         
         
    }


    public String toString(){

        return "la longitud es " + longitud + "la contrasena es " + contrasena ; 
    }

    
}
