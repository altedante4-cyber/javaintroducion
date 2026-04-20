import java.io.FileReader;
import java.io.FileWriter;
import java.util.Scanner ;
public class ej4{

	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		System.out.println("leer archivo origen");
		String archivo_origen=sc.nextLine();
		System.out.println("leer archivo destino");
		String destino=sc.nextLine();

	try(FileWriter escribir = new FileWriter(destino)){
		try(FileReader leer = new FileReader(archivo_origen)){

				int contador = 0 ; 
				int caracter ;
			while((caracter = leer.read()) != -1){
				char c = (char) caracter;
				contador ++;
				escribir.write(c);				
			}

			escribir.write("Se escribir tantos caracter " + String.valueOf(contador));
		}catch(Exception e){
			System.out.println(e.getMessage());
		}

	}catch(Exception p){ System.out.println(p.getMessage());}

	}
}
