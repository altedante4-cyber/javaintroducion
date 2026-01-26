package bloque1;
import java.util.Scanner ; 
public class ejercicio12bloque1 {
    public static void main(String [] args){

        // COMENTARIO

        /*

         al leer la opcion tenia problemas con el buffer lo que habia que hacer era limpiar el buffer para que no capture el salt de linea de la siguiete manera

         sc.nextLine()  pero al final adopte otra manera de hacerlo pero  mas larga convertir las lineas tipo string a entero con  el Integer ParseInt() osea que todas las lineas que leea tengo que hacerlo de esa manera
         pero al final croe que adoptare la la primera  teneiendo en cuenta  lo siguiente 

         si vamos a leer antes un  nextInt y luego vamos a leeer un nextLine siempre hay que limpiar el buffer   despues ddel nextInt con el sc.nextLine() para que se  leear de manera correcta


        */
        Scanner sc = new Scanner(System.in);

        String base_datos_producto [] = new String [10];
        int base_datos_precio [] = new int [10];
        int base_datos_stock [] = new int[10];

        int posicion_producto = 0 ;
        int opcion ; 
        do{
            System.out.println("1.Dar de alta un producto nuevo  , 2.Buscar un producto por su nombre , 3.Modificar el stock y precio de un producto dado ");
             opcion = Integer.parseInt(sc.nextLine());
            switch (opcion) {
                
                case 1:
                    System.out.println("Ingrese el nombre del producto ");
                    String producto = sc.nextLine();

                    System.out.println("Ingrese el precio del producto");
                    int precio = Integer.parseInt(sc.nextLine());
                    System.out.println("Ingrese la cantidad de stock ");
                    int stock = Integer.parseInt(sc.nextLine());
                    base_datos_producto[posicion_producto] = producto;
                    base_datos_precio[posicion_producto] = precio;
                    base_datos_stock[posicion_producto] = stock ; 

                    posicion_producto ++;
                    break;
                case 2 :
                     System.out.println("Ingrese el nombre del producto que desea consultar");
                     String nombre_producto_consultar = sc.nextLine();
                    boolean encontrado = false ;
                     int poscion = 0 ;
                     
                     
                     for (int i = 0 ; i < base_datos_producto.length ; i++ ){
                                String palabra = base_datos_producto[i];
                                if(palabra != null ){
                                        if (palabra.equals(nombre_producto_consultar)){
                                        encontrado = true ;
                                        poscion = i ;  
                                        break ;
                                }
                                }else{
                                    encontrado = false;
                                    break;
                                }
                                
                         
                     }

                     if(encontrado){
                        for (int i = 0 ; i < base_datos_precio.length ; i++ ){
                              if ( i == poscion){
                                System.out.println(base_datos_producto[i]);
                                System.out.println(base_datos_precio[i]);
                                System.out.println(base_datos_stock[i]);
                                break;

                              }
                        }
                    }else{
                        System.out.println("Producto no encontrado");
                     }
                     break ;
                
                case 3 :
                     System.out.println("Nombre del producto que desea modificar  ");
                     String nombre_producto_modificar = sc.nextLine();
                     boolean modificar = false ;
                     int poscion_modificar =  0 ; 
                     for (int i = 0 ; i < base_datos_producto.length ; i++ ){

                            if(nombre_producto_modificar.equals(base_datos_producto[i])){
                                modificar  = true;
                                poscion_modificar = i ; 
                                break;
                                  
                            }
                            
                     }

                     if(modificar){
                         System.out.println("Ingrese el nuevo valor del precio del producto ");
                         int precio_nuevo = Integer.parseInt(sc.nextLine());
                         System.out.println("Ingrese el nuevo valor del stock  ");
                         int precio_stock = Integer.parseInt(sc.nextLine());

                         base_datos_precio[poscion_modificar] = precio_nuevo;
                         base_datos_stock[poscion_modificar] = precio_stock;

                         System.out.println("Modificado correctamente ");
                     }
                  break ;
                default:
                    break;
            }
           
        }while(opcion != 4);



    }
    
}
