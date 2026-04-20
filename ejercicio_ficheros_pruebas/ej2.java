import java.io.FileWriter;
import java.util.Scanner;
public class ej2{
	public static void main(String[] args){
			Scanner sc = new Scanner(System.in);
		try(FileWriter escribir = new FileWriter("registro.log")){



		for(int i = 0 ; i < 4 ; i++){
			System.out.println("introduce texto " + i );
		        String n = sc.nextLine();
			n += "\n";
			escribir.write(n);
		}
		
	}catch(Exception e ){
		System.out.println(e.getMessage());
	}	

	}
}
