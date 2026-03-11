package Ejercicioclase;


import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner  ; 
public class eventodeportivo {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        ArrayList<String> email = new ArrayList<>();
        HashSet<String> registrosrecibidos  = new HashSet<String>();

        int opcion ; 
        char op;

        do{
            System.out.println("Ingresar email 1.s 2.n  ");
            op= sc.nextLine().charAt(0);

            if (op == 's'){
                  
                 System.out.println("ingrese el email ");
                 String email1 = sc.nextLine();
                 
                 email.add(email1);
                 registrosrecibidos.add(email1);
                 System.out.println("agregado correctamente");
                  
            }

            if (op == 'n'){
                System.out.println("SALIENDO ..................................");
            }
        }while(op != 'n');


        do{

            System.out.println("1.Numero totla de registor recibidos ,  \n 2.Numero total de asistentes unicos  , \n 3.que emails estan duplicados ");
            opcion = sc.nextInt();
            
            sc.nextLine();

            switch (opcion) {
                case 1:
                     int numero_recibidos = email.size();
                     System.out.println("el numero total de registro recibidos es " + numero_recibidos );
                    break;
            
                case 2 : 
                    int nmero_de_asistentes_unicos = registrosrecibidos.size(); 
                    System.out.println("el numero total de registros unicos es de  " + nmero_de_asistentes_unicos);
                 break ; 

                case 3 :
                        int contador = 0 ;




                            
                    }
                    }
                break ; 

                default:
                        System.out.println("affadfs");
                    break;

                        }
            
            

        }while(opcion != 4 );
         
    }
}
