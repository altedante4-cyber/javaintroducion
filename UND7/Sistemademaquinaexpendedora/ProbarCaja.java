package Sistemademaquinaexpendedora;

import java.util.Scanner ; 
public class ProbarCaja {
    public static void main(String[] args ){

        Scanner sc  = new Scanner(System.in );
        MaquinaExpendedora maquinas = new MaquinaExpendedora() ; 

        Producto p1 = new Producto("cocacolar", 14, 15);
        Producto p2 = new Producto("sprite", 10, 4);
        Producto p3 = new Producto("mendozina", 4, 6);


        maquinas.insertarProducto(0, p1);
        maquinas.insertarProducto(1, p2);
        maquinas.insertarProducto(2, p3);


        int opcion = 0 ; 

        do{
            System.out.println("1.Ver Producto ");
            System.out.println("2.Comprar");
            System.out.println("3.Salir y Ver Caja ");
            opcion  = sc.nextInt();

            sc.nextLine();

            switch (opcion) {
                case 1:
                    maquinas.verproducto();
                    break;
                case 2 :
                    System.out.println("ingrese la poscion  ");
                    int pos = sc.nextInt() ; 
                    System.out.println("Ingrese la cantidad ");
                    double precio = sc.nextDouble() ; 


                
                    maquinas.comprar(pos, precio);

                 break ;
                case 3 :
                    System.out.println("=====================saliendo ================");
                    maquinas.getcatidadvendida() ;
                    break;
                default:
                    break;
            }

        }while(opcion != 3 );
        

    }
}
