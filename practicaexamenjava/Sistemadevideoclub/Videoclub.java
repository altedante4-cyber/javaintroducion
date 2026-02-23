package Sistemadevideoclub;

public class Videoclub {
    
    private Pelicula [] p1 ;
    private  Alquiler [] alquileres;
    private int numPeliculas;
    private int numAlquileres;



    public Videoclub(){

        p1 = new  Pelicula[20];
        alquileres = new Alquiler[50];
        numAlquileres = 0;
        numPeliculas = 0 ; 
    }
 

     //agrtegar pelicula
     //buscarpelicula
     //alquilar
     //mostrardispionibles

    // metodo booleano para agregar una peliculo

    public boolean addPelicula(Pelicula p ){

        if (this.numPeliculas < this.p1.length ){

            p1[numPeliculas++] = p ; 
            return true ;
        }

        return  false ; 
    }

    // buscar pelicula

    public boolean buscarPelicula(String titulo ){

        boolean encontrado = false ;
        for (int i = 0 ; i < p1.length  ; i++ ){

             if(p1[i] != null && p1[i].dametitulo().equalsIgnoreCase(titulo)){
                 return true ; 
                 break;
             }
        }
        return false ; 
    }


    public boolean  alquilarPelicula(Cliente c , String titulo , int dias  ){


        Pelicula p = buscarPelicula(titulo);

       if (p == null || !p.estaLibrePelicula() ) return false ;        

       p.estaLibrePelicula();
       alquileres[numAlquileres] = new Alquiler(p, c, dias);
       numAlquileres ++ ; 
       return true ; 

   }


   public void mostrarDisponibles(){

    for(int i = 0 ; i < numPeliculas ; i++ ){
        if(p1[i].estaLibrePelicula()){
            System.out.println(p1[i]);
        }
    }
   }


   public double calculaRecaudacion(){
      double total = 0 ; 

      for(int i= 0  ; i < numAlquileres ;i++ ){

           total += alquileres[i].calcularPrecio();
      }

      return total ; 
   }
}