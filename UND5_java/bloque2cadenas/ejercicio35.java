public class ejercicio35 {

    public static void main(String[] args ){
        String entrada = "hola";
        boolean esent = false;
        if(entrada){
                int entero = Integer.parseInt(entrada);
                 esent = true;
        }else{
             esent = false;

        }

        if(esent){
            System.out.println("es entero");
        }else{
            System.out.println("NO es entero");
        }
        
        
        


        boolean esdigito = false ;
        for(int i = 0 ; i < entrada.length() ;i++ ){

               char c = entrada.charAt(i);

               if(c >= '0' && c <= '9'){
                    esdigito = true ; 
                    break;

               }
        }

        if(esdigito){
            System.out.println("Es un digito");
        }else{
            System.out.println("Son letras ");
        }
         
    }
    
}
