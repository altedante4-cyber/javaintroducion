public class Gato extends Animal {
    private String raza ,microchip ; 
    public Gato(String nombre , String raza, String fechaNacimiento , double peso , String microchip ){
         super(nombre, fechaNacimiento, "", peso);
         validar_especie(raza);
         this.microchip = microchip;
    }
    @Override
    public void validar_especie(String raza ){
         String valores_correctos [] = {"Siames","Persa","Angora","ScottishFold"};
         boolean encontrado = false ; 
         for(String valores : valores_correctos){
              if(valores.equals(raza)){
                encontrado = true ;
                break ; 
              }
         }
         if(!encontrado){
             this.raza = "";
         }

      this.raza = raza ; 
    }

    public String dameDatosAnimal(){
        return "Nombre: " + getNombre() + "\nRaza: " + raza + "\nFecha de Nacimiento: " + getFechaNacimiento() + "\nPeso: " + getPeso() + " kg" + "\nmicrochip: " + microchip + "\nComentarios: " + getComentarios();
    }

     public String toString(){
        return super.toString() + " Especi " + raza + "Microship" + microchip ;
    }


}
