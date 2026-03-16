public class Pajaro  extends Animal {
    private String especie;
    private boolean cantor ;
    public Pajaro(String nombre , String especie, String fechaNacimiento , double peso , boolean cantor ){
         super(nombre, fechaNacimiento, "", peso);
         validar_especie(especie);
         this.cantor = cantor ; 
    }


    @Override
    public void validar_especie(String especie  ){
         String valores_correctos [] = {"Canario","Periquito","Agapornis"};
         boolean encontrado = false ; 
         for(String valores : valores_correctos){
              if(valores.equals(especie)){
                encontrado = true ;
                break ; 
              }
         }
         if(!encontrado){
             this.especie = "";
         }

         this.especie = especie; 
    }

    public String dameDatosAnimal(){
        return "Nombre: " + getNombre() + "\nEspecie: " + especie + "\nFecha de Nacimiento: " + getFechaNacimiento() + "\nPeso: " + getPeso() + " kg" + "\nCantor: " + (cantor ? "Si" : "No") + "\nComentarios: " + getComentarios();
    }

    public String toString(){
        return super.toString() + " Especi " + especie + " Cantor " + (cantor ? "Cantor" : "No cantor");
    }

    
}
