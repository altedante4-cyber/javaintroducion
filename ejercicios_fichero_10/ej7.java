import java.io.FileReader;
import java.util.ArrayList;
public class ej7 {
	public static void main(String[] args){
		ArrayList<Integer>enteros = LeeFicheroIntLista("ejercicio5.txt"); 
		for (Integer c : enteros){
			System.out.println(c); 
		}
	 }
	public static ArrayList<Integer> LeeFicheroIntLista(String nombre_fichero)  {
		try{
			FileReader leer = new FileReader(nombre_fichero);
			int caracter;
			String numeros ="";
			ArrayList<Integer> listaenteros = new ArrayList<>();
			while ((caracter = leer.read()) != -1) {
	
			char c = (char) caracter;
				if ( c >= '0' && c <= '9'){
				 	numeros += c ;  
				}else if (!numeros.isEmpty()){
				  int agregar = Integer.parseInt(numeros);
				 listaenteros.add(agregar);
				numeros = "";
			}	
}	
			if(listaenteros.isEmpty()){
				return null ;
			}
			leer.close();
			return listaenteros;
		} catch(Exception e) {
			System.out.println(e.getMessage());
			return null;
		}
	}
}
