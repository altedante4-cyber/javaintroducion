import java.io.FileReader;
import java.io.IOException;
public class p{
	public static void main(String[] args) throws IOException{
		FileReader leer = new FileReader("nombres.txt");
		int caracter,caracteranterios = 0 ;
		int contador= 0 ; 
		
		try{
			while((caracter = leer.read()) != -1){
				if(caracter == '\n'){
					contador ++;
				}
				if(caracter == '\n' && caracteranterios == '\n'){
					contador --;
				}

				caracteranterios = caracter;
		}

		System.out.println(contador);
	}catch(Exception e){
			System.out.println(e.getMessage());
	}finally{
		if(leer != null){
			try{
				leer.close();
			}catch(IOException e){
				System.out.println(e.getMessage());
			}
		}
	}
	}
}
