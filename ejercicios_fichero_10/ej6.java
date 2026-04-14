import java.io.FileReader;
public class ej6 {
	public static void main(String[] args){
		SumaFicheroInt("ejercicio5.txt");
	}
	public static void SumaFicheroInt(String nombre_fichero)  {
		try{
			FileReader leer = new FileReader(nombre_fichero);
			int caracter;
			int suma_valores = 0;
			String numeros = "";
			while ((caracter = leer.read()) != -1) {
	
			char c = (char) caracter;
				if ( c >= '0' && c <= '9'){
				  numeros += c ; 
				}else if (!numeros.isEmpty()){
		 		  suma_valores += Integer.parseInt(numeros);
				 numeros = "";
			}				
}	
			System.out.println(suma_valores);
			leer.close();
		} catch(Exception e) {
			System.out.println(e.getMessage());
		}
	}
}
