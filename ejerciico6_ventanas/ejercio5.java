import java.util.HashMap;
import java.util.ArrayList;
public class ejercio5{
	public static void main(String[] args){
		String texto = "uno,dos|tres,cuatro|cinco,seis|cuatro,seis";
		HashMap<String, Integer> conteo = new HashMap<>();
		String palabra_separadas [] = texto.split("[,|]");
		int contador= 0;

		for(int i = 0 ; i < palabra_separadas.length;i++){
				String primera = palabra_separadas[i].trim();
			for(int j = 0 ; j < palabra_separadas.length ;j++){
				String segunda = palabra_separadas[j].trim();
			if(primera.equals(segunda)){
				contador ++;	
			}
		}
		conteo.put(primera,contador);
		contador=0;		
	}      

	ArrayList<String> claves = new ArrayList<>(conteo.keySet());
	for(int i = 0 ; i < claves.size();i++){
		String clave = claves.get(i);
		int valor = conteo.get(clave);
		System.out.println(clave + valor);
	}
   }
}
