public class ejercicio51 {
    public static void main(String[] args ){

        String cadena = "En la habitación numero 3 hay un numero 5, pero en el numero 8 no hay nada";
        String cadena_split []= cadena.split(" ");
        String numeros = "0123456789";
        String na= "";

        for(int i = 0  ; i < cadena_split.length - 1 ; i++ ){
            
            if(cadena_split[i].equals("numero")){

                 String posibledigito = cadena_split[i + 1];

                 if(posibledigito.length() == 1 && numeros.contains(posibledigito)){
                        int valor = Integer.parseInt(posibledigito);

                        int duplicado = valor * 2 ; 
                    

                      na += duplicado + " ";
                 }
            }
                

            
        }
        
        System.out.println(na); 

        

    }




    
}
