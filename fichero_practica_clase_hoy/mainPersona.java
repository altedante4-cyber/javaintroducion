import java.util.ArrayList;
import java.util.Scanner;
import java.io.FileWriter;

public class mainPersona{

	public static void main(String[] args){
		ArrayList<Persona> lista_personas = new ArrayList<>();
		Scanner sc = new Scanner(System.in);
		int opcion;

		do{
			System.out.println("Introduce la opcion 1.Introduce Persona 2.Salir ");
			opcion = sc.nextInt();
			sc.nextLine();
			switch(opcion){
				case 1 :
					System.out.println("Introduce el nombre de la persona");
					String nombre = sc.nextLine();
					System.out.println("Introduce la edad de la persona");
					int edad = sc.nextInt();

					lista_personas.add(new Persona(nombre,edad));
				break;
				case 2:
					System.out.println("Saliendo");
					try(FileWriter escribir = new FileWriter("personas.txt")){
						   
						  for(Persona p : lista_personas){

							escribir.write(p.getNombre() + "," + p.getEdad());
													escribir.write("\n");

								
						}
					}catch(Exception e){
							 System.out.println("No se pudo guardar correctamente");
				}
		
				break;
			}
			
		}while(opcion != 2);
	}
}


