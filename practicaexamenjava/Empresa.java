import java.util.Scanner ; 
public class Empresa {

    private Dron [] drones ;

    private String nombre_empresa ;
    private int contador_drones ; 
    
    
    public Empresa(String nombre_empresa){

        this.nombre_empresa = nombre_empresa ;
        this.drones = new Dron[8];
        this.contador_drones = 0 ; 
    }


    // agregar un dron 

    public boolean addDron(Dron d ){

        if (this.contador_drones < this.drones.length ){

                this.drones[contador_drones++] = d; 
                return true ; 
        }

        return  false ; 

    }

   @Override
public String toString() {

    String resultado = "Drones:\n";

    for (int i = 0; i < this.drones.length; i++) {

        if (this.drones[i] != null) {
            resultado += drones[i].toString();
            resultado += "\n";
        }
    }

    return resultado;
}

    public void  BuscarID(String identificador ){

        boolean encontrado = false ; 
        int posicion = 0 ; 
        for(int i = 0 ; i < this.drones.length ; i++ ){

             if( this.drones[i] != null && this.drones[i].dameIdentificador().equalsIgnoreCase(identificador)){
                encontrado = true ;
                posicion =  i ;  
                break ;
             }

         }

         if(encontrado){

            System.out.println(this.drones[posicion].toString());
         }else{
            System.out.println("No ha sido encontrado el dron ");
         }

        }


    public static void main(String[] args ){
        Scanner sc = new Scanner(System.in);
        Empresa em = new Empresa("Michael ");

        Dron d1= new Dron("nokia ", "12345");
        Dron d2 = new Dron("sansun ", "12346");
        Dron d3= new Dron("motorola ", "12347");



        em.addDron(d1);
        em.addDron(d2);
        em.addDron(d3);


        System.out.println(em.toString());


        System.out.println("Ingrese el identificador del dron ");
        String identif = sc.nextLine() ;

        em.BuscarID(identif);

        d1.setGastarBateria(20);

        System.out.println(em.toString());


    }
    
}
