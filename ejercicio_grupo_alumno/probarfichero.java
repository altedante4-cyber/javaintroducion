import java.io.FileReader;
import java.util.ArrayList;
public class probarfichero{

 public static void main(String[] args){
		leerarchivo("michael");
	}


	public static  void leerarchivo(String nombre_archivo){
		try(FileReader leer = new FileReader(nombre_archivo)){
			int caracter;
			ArrayList<String> palabras = new ArrayList<>();	
			String palabra="";
			while((caracter = leer.read()) != -1  ){
				char c = (char) caracter;
				if( c != '\n'){
					palabra += c;

				}else{
				     palabras.add(palabra);
					palabra="";
			 }
					
			}

	for(String p : palabras){
    
    String nuevo = p.replace("--", "");    
    String nuevamente = nuevo.trim();
    String temp[] = nuevamente.split(" ");
	for(int i = 0 ; i < temp.length ; i++){
			
			if(i == 1){
				System.out.print(temp[i]);
			}
	}

}

	}catch(Exception e){

		System.out.println(e.getMessage());
	}
	}
}
