package javaintroducion;
import java.util.Random;

public class Password {

    private int longitud;
    private String contrasena;
<<<<<<< HEAD

    // Constructor por defecto
    public Password() {
        this.longitud = 8;
        // Inicializamos para que no sea null
        this.contrasena = ""; 
        generarPassword();       
    }

    // Constructor con longitud
    public Password(int longitud) {
        this.longitud = longitud;
        this.contrasena = ""; 
        generarPassword();
=======
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
         
>>>>>>> 2d09555dd2f2cd60cf52ab7c653db9238ceb4d37
    }

    public int devolverlongitud() {
        return this.longitud; 
    }

<<<<<<< HEAD
    public void generarPassword() {
        Random lete = new Random();
        String palabras_numeros = "0123456789qqwrtyuioppasdfghjklzxcvbnm";
        
        // Reiniciamos la contraseña por si ya tenía algo
        this.contrasena = ""; 
=======

     // creamos un seter que nos dara la password con la longiud que le passemos nosotros

     public String  setgenerarcontrasena(int longitud){
        
        Random lete = new Random();
        this.contrasena = "";
        String palabras_numeros="0123456789qqwrtyuioppasdfghjkl;zxcvbnmQWERTYUIOOOPPASDFGHJKLLL;XCVBNMM";
        char palabras_utilizar [] = new char[palabras_numeros.length()];
>>>>>>> 2d09555dd2f2cd60cf52ab7c653db9238ceb4d37
        
        for (int i = 0; i < this.longitud; i++) {
            // Sacamos un índice aleatorio
            int indice = lete.nextInt(palabras_numeros.length());
            
                this.contrasena += palabras_numeros.charAt(indice);

<<<<<<< HEAD
=======
                palabras_utilizar[i] = c ; 
        }
        
        
        for(int i = 0 ; i < longitud ;i++ ){
            int gerar_contrasena = lete.nextInt(palabras_utilizar.length);

             this.contrasena  += palabras_utilizar[gerar_contrasena]; 
>>>>>>> 2d09555dd2f2cd60cf52ab7c653db9238ceb4d37
        }
        
    return this.contrasena; 
    
}

<<<<<<< HEAD
    public String toString() {
        return "La longitud es " + longitud + " y la contraseña es: " + contrasena; 
    }
}
=======
  public String toString(){

        return "la longitud es " + longitud + "la contrasena es " + contrasena ; 
    }

}
  
>>>>>>> 2d09555dd2f2cd60cf52ab7c653db9238ceb4d37
