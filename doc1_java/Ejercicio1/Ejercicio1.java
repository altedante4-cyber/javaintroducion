public class Ejercicio1{

    private String nombre , correo ;
    private int edad;
    
    public Ejercicio1(String nombre , String correo , int edad ){

         this.nombre = nombre ;
         this.correo = correo ;
         this.edad = edad ; 
    }


    public void presentarse(){

         System.out.println("El nombre " + nombre + " su correo es  " + correo + " y su edad es " + edad );
    }


    public boolean esMayorDeEdad(){
         
          if(edad < 18 ){
            return false ;
          }

          return true ; 
    }



}