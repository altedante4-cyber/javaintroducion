import java.util.ArrayList;

public class ClinicaVeterinaria {
    private ArrayList<Animal> listaAnimales ;

    public ClinicaVeterinaria(){
         this.listaAnimales= new ArrayList<>();          
    }

    public boolean insertaAnimal(Animal a ){
         return listaAnimales.add(a);
    }
    public Animal  buscaAnimal(String nombre){

        for(Animal a : listaAnimales ){
               if(a.getNombre().equals(nombre)){
                    return a ; 
               }
         }

            return null ; 
    }

    public boolean modificaComentarioAnimal(String nombre , String nuevo_comentario ){

         for(Animal a : listaAnimales ){
               if(a.getNombre().equals(nombre)){
                     a.setComentario(nuevo_comentario);
                    return true ; 
               }
         }
         return false ; 
    }

    @Override
    public String toString(){
        String resultado = "";
        for(Animal a : listaAnimales){
            resultado += a.dameDatosAnimal() + "\n\n";
        }
        return resultado;
    }


}
