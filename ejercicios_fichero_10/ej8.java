import java.io.FileReader;
import java.io.FileWriter;
import java.util.ArrayList;
public class ej8 {
	public static void main(String[] args){
	ArrayList<Integer> resultado = OrdenaFIcheroInt("ejerc
	}
	public static ArrayList<Integer> OrdenaFIcheroInt(String nombre_fichero){
		int caracter;
		String numeros =""; 
		ArrayList<Integer> valores_ordenar = new ArrayList<>();
		
		try{
			FileReader leer = new FileReader(nombre_fichero);
			while((caracter = leer.read()) != -1) {
				char c = (char) caracter;
				if (c >= '0' && c <= '9'){
					numeros += c;
				} else if (!numeros.isEmpty()){
					valores_ordenar.add(Integer.parseInt(numeros));
					numeros = "";
				}
			}
			leer.close();

		}catch(Exception e ){
			System.out.println(e.getMessage());
		}

		for(int i = 0; i < valores_ordenar.size() - 1; i++){
			for(int j = 0; j < valores_ordenar.size() - 1 - i; j++){
				if(valores_ordenar.get(j) > valores_ordenar.get(j + 1)){
					int temp = valores_ordenar.get(j);
					valores_ordenar.set(j, valores_ordenar.get(j + 1));
					valores_ordenar.set(j + 1, temp);
				}
			}
		}
		return valores_ordenar;
	}
}
