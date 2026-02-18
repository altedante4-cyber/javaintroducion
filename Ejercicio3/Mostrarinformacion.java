import java.util.Scanner ; 
public class Mostrarinformacion {
		static  Scanner sc = new Scanner(System.in);
		static Persona per [] = new Persona[6];	
		static int contador = 0 ; 
		public static void main(String[] args) {
		Estudiante mik = new Estudiante("michael", "aguilar", "20239442", "solt", "dnasf");



		//1.Dar de alta a Estudiantes
		//2 . Dar de alta Profesor
		// 3.Dar de alta a Personal
		//4 Estadisticas
		// 5 salir 


		int opcion ; 

		do{
			System.out.println("\n Ingrese la opcion \n 1.Dar de alta a Estudiantes  \n 2.Sar de alta profesor \n 3.Dar de alta Personal \n 4.Mostrar Estadisticas \n 5.Salir ");
			opcion =sc.nextInt();

			sc.nextLine();

			switch (opcion) {
				case 1:
			
					ALtaEstudiante();
					
				case 2 :

				break;

				case 3 :
				
				break ; 


				case 4 :
				
				break ; 


				case 5 :
					System.out.println("saliendo");
				
					break ;
				
				    
			
				default:
				System.out.println("Numero incorrecto mal introducido ");
				break;
			}

		}while(opcion != 5 );
	}


public static void ALtaEstudiante(){
	System.out.println("ingrese el nombre del estudiante ");
	String nombre = sc.nextLine();
	System.out.println("INgrese el apellido del estudiante ");
	String apellido = sc.nextLine(); 
	System.out.println("Ingrese el numero de DNI del estudiante ");
	String dni = sc.nextLine();
	System.out.println("Ingrese el  estado civil  ");
	String civil = sc.nextLine();
	System.out.println("Ingrese el curso ");
	String curso = sc.nextLine();

	Estudiante  e1 = new Estudiante(nombre, apellido, dni, civil, curso);
	per[0] = e1 ;  // aqui estamos agregando a una persona 
	contador ++ ; 

}

public static void ALtaProfesor(){
	System.out.println("ingrese el nombre del profesoor");
	String nombre = sc.nextLine();
	System.out.println("INgrese el apellido del profesor ");
	String apellido = sc.nextLine(); 
	System.out.println("Ingrese el numero de DNI del profesor ");
	String dni = sc.nextLine();
	System.out.println("Ingrese el  estado civil  del profesor ");
	String civil = sc.nextLine();
	System.out.println("Ingrese el anio de empleado ");
	int anio = sc.nextInt() ; 
	System.out.println("Ingrese el numero de empleado ");
	int numero = sc.nextInt() ; 
	System.out.println("Ingrese el departamento del profesor ");
	String departamento = sc.nextLine();

	Profesores  e2 = new Profesores(nombre, apellido, dni, civil,anio, numero ,  departamento);
	per[1] = e2 ;  // aqui estamos agregando a una persona 
	contador ++ ; 
}



public static void ALtaPersonaServicio(){
	System.out.println("ingrese el nombre del Personal ");
	String nombre = sc.nextLine();
	System.out.println("INgrese el apellido del Personal  ");
	String apellido = sc.nextLine(); 
	System.out.println("Ingrese el numero de DNI del Personal  ");
	String dni = sc.nextLine();
	System.out.println("Ingrese el  estado civil  del Personal ");
	String civil = sc.nextLine();
	System.out.println("Ingrese el anio del Personal  ");
	int anio_incorporacion = sc.nextInt() ; 
	System.out.println("Ingrese el numero de Personal  ");
	int numero_despacho = sc.nextInt() ; 
	System.out.println("Ingrese el departamento del Personal  ");
	String numero_seccion = sc.nextLine();
	
	Persona e2 = new Personal(nombre, apellido, dni, civil, anio_incorporacion, numero_despacho, numero_despacho)
	per[3] = e2 ;  // aqui estamos agregando a una persona 
	contador ++ ; 
}



}


