import java.io.FileReader;
import java.io.FileWriter;
import java.io.*;
public class GestionTareas{
	public static void escribirTareas(String nombrearchivo , String[] tareas){
		try{
			FileWriter escribir = new FileWriter(nombrearchivo);
			for(int i = 0 ; i < tareas.length ; i++){

				escribir.write(tareas[i] + "\n" );
			}

		escribir.close();
		}catch(IOException e ){

		System.out.println(e.getMessage());
		}
	}

	public static void leerTareas(String nombreArchivo){
		
		try{
				FileReader leer = new FileReader(nombreArchivo);
				int caracter;
				String cad ="";
				while((caracter = leer.read()) != -1){
					cad += (char) caracter;
				}

			leer.close();

			String [] mostrar = cad.split("\n");
			int contador_prioridad_alta = 0;
			String palabra_anterior="" ;
			String palabra_actual="";
			String mayor = "";
			for(int i = 0 ; i < mostrar.length ; i++){
				String m [] = mostrar[i].split(";");
				if ( m[1].equalsIgnoreCase("alta")){
					contador_prioridad_alta ++;
				}

				palabra_actual += m[0];
				palabra_anterior += m[0];
				if(palabra_anterior.length() > palabra_actual.length()){
						mayor += palabra_anterior ;
				}

				palabra_actual = palabra_anterior;

			}
				System.out.println(i +"."+ m[0] + "prioridad " + m[1]);  
			}				
			System.out.println("== ESTADISTICA==");
			System.out.println("Tareas co prioridad Alta " + contador_prioridad_alta);
			System.out.println(mayor);
		}catch(IOException p){
			System.out.println(p.getMessage());

		}

	}


	public static void main(String[] args){

		String archivo = "tareas.txt";
		        String[] tareas = {
            "Estudiar Java;Alta",
            "Hacer ejercicio;Media",
            "Comprar pan;Baja",
            "Repasar excepciones;Alta"
        };

	escribirTareas(archivo , tareas);
	leerTareas(archivo);
	}
}
