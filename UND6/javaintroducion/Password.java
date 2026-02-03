package javaintroducion;
import java.util.Random;
public class Password {

    private int longitud;
    private String contrasena;
    //constructor por defct6o 
    public Password(){
        this.longitud = 8 ; 
        this.contrasena = "";
         setgenerarcontrasena(this.longitud);       
    
    }

    public Password(int longitud ){

        this.contrasena = "";
        this.longitud = longitud;
          
         setgenerarcontrasena(this.longitud);
    }

    //devolver un boolean si es fuertye o no 

    public boolean esFuerte(){
         
         int contador_mayuscula = 0 ;
         int contador_minuscula = 0 ;
         int contador_numeros = 0 ; 
         for (int i  = 0 ; i < this.contrasena.length() ;i++ ){

                char c = this.contrasena.charAt(i);


                if(c >= 'A' && c <= 'Z'){
                    contador_mayuscula ++ ; 
                }else if(c >= 'a' && c <= 'z'){
                    contador_minuscula ++  ; 
                }else{
                    contador_numeros ++  ; 
                }
                
         }

         if(contador_mayuscula >= 2 && contador_minuscula >= 1 && contador_numeros >= 5){
                return true ; 
         }

         return  false ; 
         
    }
    
    //necesitamos un metodo geter para devolver la longitud

    public int devolverlongitud(){

        return this.longitud; 
    }


     // creamos un seter que nos dara la password con la longiud que le passemos nosotros

     public String  setgenerarcontrasena(int longitud){
        
        Random lete = new Random();
        this.contrasena = "";
        String palabras_numeros="0123456789qqwrtyuioppasdfghjkl;zxcvbnmQWERTYUIOOOPPASDFGHJKLLL;XCVBNMM";
        char palabras_utilizar [] = new char[palabras_numeros.length()];
        
        
        for(int i = 0 ; i < palabras_numeros.length() ;i++ ){
                char c = palabras_numeros.charAt(i);

                palabras_utilizar[i] = c ; 
        }
        
        
        for(int i = 0 ; i < longitud ;i++ ){
            int gerar_contrasena = lete.nextInt(palabras_utilizar.length);

             this.contrasena  += palabras_utilizar[gerar_contrasena]; 
        }
        
    return this.contrasena; 
    
}

  public String toString(){

        return "la longitud es " + longitud + "la contrasena es " + contrasena ; 
    }

}
  