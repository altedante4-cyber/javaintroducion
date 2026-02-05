package javaintroducion;
import java.util.Scanner ; 
public class Probaralumnos {

    
    public static void main(String[] args ){
            Scanner sc = new Scanner(System.in);
          Gestionnotas mio = new Gestionnotas();

            int opcion ; 
          do{

            System.out.println("1.Agregar alumno \n 2.Buscar un alumno \n 3.Modificar su nota  \n 4.Realizar la media de todas las notas  \n 5.Realizar la media de las notas menores de 5 \n 6.Los alumnos con mejores notas han sacado \n 7.Los alumnos con peores notas que han sacado  ");
            opcion = sc.nextInt();
            sc.nextLine();

            switch (opcion){
                case 1 :
                    System.out.println("INgrese el nombre del alumno a guardar ");
                    String name = sc.nextLine();
                    System.out.println("Ingrese la nota de dicho alumno ");
                    int nota = sc.nextInt(); 
                    //creo el costructor alumonn 

                    Alumno misalumnos = new Alumno(name, nota);

                    // guardo en gestinnotas

                    if(mio.agregaralumon(misalumnos)){
                        System.out.println("Agregado correctamente");
                    }else{
                        System.out.println("NO se ha agregado ");
                    }

                case 2:
                    System.out.println("Ingrese el nombre del alumno");
                    String n= sc.nextLine();

                    if(mio.buscaralumnos(n)){
                        System.out.println("encontrado" + mio.toString());
                    }else{
                        System.out.println("no encontrado");
                    }
                    
                    break;
                case 3:
                    System.out.println("Ingrese el nombre del alumnos que desea modificar la nota ");
                    String nam = sc.nextLine();
                    System.out.println("Ingrese la nota que le quiere poner ");
                    int not = sc.nextInt();

                    if(mio.modificarnota(nam, not)){
                        System.out.println("La nota ha sido modificada correctamente ");
                    }else{
                        System.out.println("La nota no se ha modficicado ");
                    }

                    break; 
                
                case 4:
                    System.out.println("LA MEDIA DE LAS NOTAS ES " + mio.mostrarmedianotas());
                    break; 
                case 5 :
                     System.out.println("La nota media de los alumnos que tienen una nota inferiro a 5  es  " + mio.mostrarmedianotasmenores() );
                     break ;
                case 6 :
                     System.out.println("Los alumnos que mejores notas han sacado es  " + mio.mostraralumnosmejoresnotas());
                    break ;
                case 7:
                    System.out.println("mostrar alumnoes con peores notas " + mio.mostraralumnospeoresnotas());
                    default:
                    break;
            }

            
          }while(opcion !=8 );
          




    }
}
