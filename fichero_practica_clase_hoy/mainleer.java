import java.io.FileReader;
import java.util.ArrayList;
public class mainleer{

public static void main(String[] args){
	ArrayList<Persona> lista_personas = new ArrayList<>();
	
	try(FileReader leer = new FileReader("personas.txt")){
		int caracter;
		String cad = "";
		while((caracter = leer.read()) != -1){
			char c = (char) caracter;
			cad  += c ; 			
			
		}

		String separar[] = cad.split("\n");
		for(int i = 0 ; i < separar.length; i++){
			String separar_coma [] = separar[i].split(",");
			int entero =Integer.valueOf(separar_coma[1]);
			 lista_personas.add(new Persona(separar_coma[0],entero));

		}

	for(Persona p : lista_personas  ){
		System.out.println(p.getNombre()+","+p.getEdad() );
	}			

	}catch(Exception e ){

		System.out.println("no se pudo leer el archivo");
	}
	
}
}
