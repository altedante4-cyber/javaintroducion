package bloque2cadenas;
import java.util.Scanner; 
public class ejercico26 {

    public static void main(String[] args ){


         Scanner sc = new Scanner(System.in);

      String p1 = "patata";
String p2 = "coco";
String resultado = "";

// Buscamos el límite para el intercambio
int limite = Math.min(p1.length(), p2.length());

// 1. Alternamos letras hasta que una se acabe
for (int i = 0; i < limite; i++) {
    resultado += p1.charAt(i);
    resultado += p2.charAt(i);
}

// 2. Añadimos el "sobrante"
if (p1.length() > p2.length()) {
    resultado += p1.substring(limite); // Añade lo que queda de patata
} else if (p2.length() > p1.length()) {
    resultado += p2.substring(limite); // Añade lo que queda de coco
}

System.out.println(resultado); // Imprime: pcaotcaota
    }
    
}
