import java.util.HashMap;
import java.util.ArrayList;
public class prueba{
	public static void main(String[] args){
		String texto [] = {"hola","como estas ","donde estas","como te va","hola"};

		int contador = 0;
		HashMap<String,Integer> cont = new HashMap<>();
		for(int i = 0 ; i < texto.length ; i++){ 
			String primer = texto[i].trim();
			for(int j=0; j < texto.length  ;j++){
				String segunda = texto[j].trim();
			//	String seguda = texto[j+1].trim();
			if(primer.equals(segunda)){
				 contador ++;
			}
		}
		cont.put(primer,contador);
		contador = 0 ; 
	}


	ArrayList<String> claves = new ArrayList<>(cont.keySet());

	for(int i = 0 ; i <  claves.size(); i++){
		String clave = claves.get(i);
		int valor = cont.get(clave);
		System.out.println(clave + valor);
	}
	}
}

// el rimer for es el numero de veces que vamos a mostrar y el for es el que muesra
