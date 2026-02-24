package GESTIONiNGENTAIO;
import java.util.Scanner ; 
public class utilEscolar {

    private String nombre ;
    private double precio ; 



    public utilEscolar(String nombre , double precio  ){
         
        this.nombre = nombre ; 
        this.precio = precio ; 
    }


    // metodo seter para validar el preico 

    public void setPrecio(double precio ){
        this.precio = precio ;  
    }
    
    // para mostar el contenido de los utilizes 
    public String toString() {

        return "Nombre " + nombre + " el precio  " + precio ; 
    }
public static void main(String[] args ){
    Scanner sc = new Scanner(System.in );
    utilEscolar [] utiles = new utilEscolar[3];

    for(int i = 0 ; i < 3 ; i++   ){
    
         System.out.println("Ingrese el nombre del escolar ");
         String nombre = sc.nextLine();
        System.out.println("INgre el precio del producot ") ;
        double precio = sc.nextDouble();
         sc.nextLine();

        utilEscolar nuevo = new utilEscolar(nombre, precio);

        if(precio  < 0 ){
            nuevo.setPrecio(1.0);
        }

        utiles[i] = nuevo ;  

    }

    for(int i =0  ; i < 3 ; i++ ){
        System.out.println(utiles[i].toString() );
    }
}


    
}
