public class Reptil extends Animal {
    private String especie ;
    private boolean venenoso;
    public Reptil(String nombre , String especie   , String fechaNacimiento, double peso , boolean venenoso ){
         
         super(nombre, fechaNacimiento,"", peso);
         validar_especie(especie);
         this.venenoso = venenoso ; 
    }

     @Override
    public void validar_especie(String especie  ){
         String valores_correctos [] = {"Tortuga","Iguana","DragonDeComodo"};
         boolean encontrado = false ; 
         for(String valores : valores_correctos){
               if(valores.equals(especie)){
                 encontrado = true ;
                 break ; 
               }
         }
         if(encontrado){
             this.especie = especie ;
         } else {
             this.especie = "";
         }
    }

    public String dameDatosAnimal(){
        return "Nombre: " + getNombre() + "\nEspecie: " + especie + "\nFecha de Nacimiento: " + getFechaNacimiento() + "\nPeso: " + getPeso() + " kg" + "\nVenenoso: " + (venenoso ? "Si" : "No") + "\nComentarios: " + getComentarios();
    }

     public String toString(){
        return super.toString() + " Especi " + especie + " Venenoso " + (venenoso ? "Si" : "No");
    }

}
