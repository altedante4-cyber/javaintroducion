import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner ;
public class ejerciciocarrito {
    public static void main(String[] args ){

        Scanner sc = new Scanner(System.in );

        ArrayList<String> producto = new ArrayList<>();
        HashMap <String , Integer > carritocompra = new HashMap<>();


        int opcion;

        do{

            System.out.println("1.Agregar a carrtito \n 2.Ver carrito  ");
            opcion = sc.nextInt();

            sc.nextLine();
            switch (opcion) {
                case 1: 
                    int contador = 0 ; 

                System.out.println("Ingrese el nombre del producto  ");
                    String nombre = sc.nextLine();

                    producto.add(nombre);              
                    
                

                    for(int i = 0 ; i < producto.size() ; i++  ){
                        String pro = producto.get(i);
                           if(nombre.equals(pro)){
                    
                              contador ++; 
                             carritocompra.put(nombre,contador);
                              
                           }



                    }
                    
        
                    
                    

                    break;

                case 2 :


                Set<String> palabrasUnicas =  carritocompra.keySet();
    
                    for(String palabras : palabrasUnicas){
                         
                         System.out.println("palabra" + )
                    }
                            
                    break ; 
            
                default:
                    break;
            }

        }while(opcion != 3 );
         
          
    }
    
}
