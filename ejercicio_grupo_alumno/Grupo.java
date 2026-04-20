 import java.util.ArrayList;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.HashMap;
public class Grupo{

	private ArrayList<Alumno> lista_alumnos ;
	public Grupo(){
		lista_alumnos= new ArrayList<>();
	}

	public void InsertaAlumnoLista(String nombre , int edad,double calificacion){
		try{
			lista_alumnos.add(new Alumno(nombre,edad,calificacion));
	}catch(Exception e){
		System.out.println("El nombre esta vacio");
	}
	}

	public void Imprime(){
		for(Alumno a  : lista_alumnos){
			
		System.out.println(a.imprime()+ "\n");
	}
	}

	public void EscribeFicheroAlumnos(String nombre_fichero){

			try(FileWriter escribir = new FileWriter(nombre_fichero)){
			escribir.write(String.valueOf(lista_alumnos.size()) + "\n");
			for(Alumno a : lista_alumnos){
				String b = a.imprime();
				for(int i = 0 ; i < b.length() ; i++){
					char p = b.charAt(i);
					  escribir.write(p);
					if(p == ' '  ){
							escribir.write("--");

						
					}
				}
				escribir.write("\n");
			}
		 }catch(Exception e){
			System.out.println("Error no se pudo crear archivo");
		}
	}

	public void LeeFicheroAlumno(String nombre_fichero ){
		try(FileReader leer = new FileReader(nombre_fichero)){
			int caracter;
			ArrayList<String>palabras =new ArrayList<>();
			String palabra ="";
			while ((caracter = leer.read()) != -1 ){
				char c = (char) caracter;
				if ( c !='\n'){
					palabra += c;
				}else{
				 	palabras.add(palabra);
					palabra="";
				}
		}
		if(!palabra.isEmpty()){
			palabras.add(palabra);
		}

		leer.close();
		for(String p : palabras){
			String nueva = p.replace("--","");
			String n = nueva.trim();
			String k [] = n.split(" ");
				String al="";
				String ed="";
				String cal="";
			for(int i = 0 ; i < k.length ; i++){
				if (i ==0){
					al += k[i];
				}else if (i == 1){
					ed += k[i] ;
				}else{
					cal += k[i] ;
				}

			}
				if (k.length >= 3 && !al.isEmpty() && !ed.isEmpty() && !cal.isEmpty()){
					int a = Integer.valueOf(ed);
					double q =Double.valueOf(cal);
					lista_alumnos.add(new Alumno(al,a,q));
				}

		}
			
	}catch(Exception e){
		System.out.println(e.getMessage());
	}
	}
}
