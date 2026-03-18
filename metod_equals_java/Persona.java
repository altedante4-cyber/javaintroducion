public class Persona {

      private String nombre;
      private int edad ;

      public Persona(String nombre , int edad ){
         this.nombre = nombre ;
         this.edad = edad ; 
      }


      public String getNombre(){
         return nombre ;
      }
      public int getEdad(){
         return edad ; 
      }
      
      public boolean equals(Object obj  ){
         boolean soniguales=false;


         if(!(obj instanceof Persona ))    
                return false ; 
        
        Persona p =(Persona) obj ;

         soniguales=this.nombre.equals( p.getNombre() ) && this.edad == p.getEdad();
          
         return soniguales;
      
        }
         
      

    
}
