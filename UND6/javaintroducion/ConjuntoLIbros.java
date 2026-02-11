package javaintroducion;

public class ConjuntoLIbros {

    private Libro [] milibro ;
    private int contador ; 

    // creamos el constructo rpor defceeto 

    public ConjuntoLIbros(){

        this.milibro = new Libro[10];
    }


    // anadimos el metod  para andir libro 

    public  boolean agregarlibro(Libro f ){
          
        
        if(milibro.length >  10 ){
             return false ;
        }

        milibro[contador] = f; 
        contador ++;
        return true ; 
        
           
    }


    // eliminamos el libro pero primero tenemos que asegurarno de que el libro exista en el array de objetos

    public boolean existelibro(String titulo ){

        for(int i = 0 ; i < milibro.length ; i++ ){

            if(milibro[i].dametitulolibro().equals(titulo)){
                return true ; 
            }
        }

        return false ; 
    }


    // tenemos que ir al array  y buscar el por el titulo de libro 


    public boolean eliminarlibro(String titulo){
         
        if(existelibro(titulo)){

            for(int i = 0 ; i < 10 ; i ++ ){

                if(milibro[i].dametitulolibro().equals(titulo)){
                     
                      milibro[i].eliminartitulo(null);
                }
            }
        }

        return false ; 
    }


    // MOSTRAMOS LOS LIBROS QUE TENGAMOS EN LA BASE DE DATOS 

public String toString() {
    String resultado = "--- Mis Libros ---\n";

    for (int i = 0; i < contador; i++) {
        if (milibro[i] != null) {
            resultado += milibro[i].dametitulolibro().toString() + "\n";
        }
    }

    return resultado;
}
   
}
