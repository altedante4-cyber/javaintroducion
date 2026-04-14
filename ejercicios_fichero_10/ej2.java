import java.io.FileReader;
public class ej2 {

public static void main(String[] args) {

	LeeFicheroInt100("hola.txt");
}

public static void LeeFicheroInt100(String nombre_archivo) {
try{
	FileReader leer = new FileReader(nombre_archivo);

	int caracter ;
	while((caracter = leer.read()) != -1  ){
		System.out.println((char)caracter);
 	}
}catch( Exception e) {

	System.out.println(e.getMessage());
}


}

}
