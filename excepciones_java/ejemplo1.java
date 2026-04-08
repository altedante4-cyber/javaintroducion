public class ejemplo1 {

public static double  divide(double a , double b ){
    if (b == 0 ){
         throw new ArithmeticException("No se puede dividir por cero");
    }  
    
    return a % b ;

}
 
public static void main(String[] args ){
     try{ // dentro ponemos la linea  donde es subtible a generer una exception
        System.out.println(divide(5, 0));

     }catch(ArithmeticException a){
         System.out.println(a.getMessage());
     }
    
}

}
