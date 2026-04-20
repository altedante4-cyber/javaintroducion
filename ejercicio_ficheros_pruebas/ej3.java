import java.io.FileReader;
public class ej3{
	public static void main(String[] args){
			int contador_lineas=0;
			String num="";
			int posicion = 0;
		try(FileReader leer = new FileReader("numeros.txt")){
			int caracter ;
			while((caracter=leer.read()) != -1){
				char k = (char) caracter;
				if(k == '\n'){
				   contador_lineas ++;
				}
		}
		leer.close();
	}catch(Exception e){
		System.out.println(e.getMessage());
	}

	
	        try(FileReader col = new FileReader("numeros.txt")){

		      int [] numeros = new int[contador_lineas];
		
                          int re;
                        while((re=col.read()) != -1){
                                char p = (char) re ;
                                if( p >= '0' && p <= '9' ){
                                        num += p ;
                                }else{
                                        numeros[posicion]=Integer.valueOf(num);
                                        posicion += 1 ; 
                                        num = "";
                                }


                }

	for(Integer s : numeros){
		System.out.println(s + "," );
	}
	 }catch(Exception e){
	
		System.out.println(e.getMessage());
	}
	}

}
