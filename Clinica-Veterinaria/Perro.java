public class Perro extends Animal  {
    private String raza , microchip ;
    public Perro(String nombre , String raza , String fechaNacimiento , double peso, String microchip ){
        super(nombre, fechaNacimiento, "", peso);
        validar_especie(raza);
        this.microchip = microchip ; 
    }
    @Override
    public void validar_especie(String raza ){
         String valores_correctos [] = {"PastorAleman","Husky","FoxTerrier"};
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
    public String getRaza(){
        return raza ; 
    }
    public String getMicrochip(){
        return microchip;
    }

    public String dameDatosAnimal(){
        return "Nombre: " + getNombre() + "\nRaza: " + raza + "\nFecha de Nacimiento: " + getFechaNacimiento() + "\nPeso: " + getPeso() + " kg" + "\nMicrochip: " + microchip + "\nComentarios: " + getComentarios();
    }

     public String toString(){
        return super.toString() + " Raza " + raza  + " Microship " + microchip ;
    }


}
