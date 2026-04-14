import java.io.FileReader;
public class ej5 {

public static void main(String[] args) {

	LeeFiccheroInt("ejercicio5.txt");
}

public static void LeeFiccheroInt (String nombre_archivo) {
try{
	FileReader leer = new FileReader(nombre_archivo);

	int caracter ;
	while((caracter = leer.read	()) != -1  ){
		char c = (char) caracter ;

		if ( c >= '0' && c <='9') {
		System.out.print(c + " " ); 
	}
 	}
	leer.close();
}catch( Exception e) {

	System.out.println(e.getMessage());
}


}

}
