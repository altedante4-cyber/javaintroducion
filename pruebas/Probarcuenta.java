package pruebas;
import java.util.Scanner ; 
public class Probarcuenta {

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Cuantas cuentas va crear");
        int cuenta = sc.nextInt();
        sc.nextLine();
     
    // Creamos el objeto Cuenta 
        Cuenta mio = null;
        Banco mibanco = new Banco(2);
        for (int i = 0 ; i < cuenta ;i++ ){
        System.out.println("Ingrese el nombre de la nueva cuenta " + i);
        String nombre = sc.nextLine();
        System.out.println("Ingrese la cantidad que desea ingresar a dicha cuenta" + i);
        double cantidad = sc.nextInt();
        sc.nextLine();
        mio= new Cuenta(nombre,cantidad);
        mibanco.setanadircuenta(mio);
    }

     System.out.println("Ingrese el nombre del titular para ingresar dinero ");
     String nombre = sc.nextLine();
     if(mibanco.setingresardinero(nombre)){
          System.out.println("Ingrese la cantidad que desea ingresar a la cuenta");
          double cantidad_ingresar = sc.nextInt();
          sc.nextLine();
          mio.ingresarcantidad(cantidad_ingresar);
     }else{
         System.out.println("No existe el usuario ");
     }

    System.out.println("Ingrese el nombre del titular para retirar el dinero ");
    String nombre_titular = sc.nextLine();
    if(mibanco.setretirdinero(nombre_titular)){
        System.out.println("Ingrese la cantidad a retirar dinero ");
        double cantidad_retirar = sc.nextInt();
        sc.nextLine();
        mio.retirardinero(cantidad_retirar);
        System.out.println(mibanco.toString());
        
    }



        
        System.out.println(mibanco.toString());


    }
    
}
