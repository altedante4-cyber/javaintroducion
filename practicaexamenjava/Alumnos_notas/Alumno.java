package Alumnos_notas;

public class Alumno {
    private String nombre ;
    private Nota [] not ;
    private int contador ; 


    public Alumno(String nombre ){
        this.nombre = nombre ;
        this.not = new Nota[5];
        this.contador = 0 ; 
    }

    public boolean addNota(Nota not ){
         if(contador < this.not.length){
            this.not[contador++]  = not ;
            return true ;
         }
    return false ; 
        }

        public double calcularMedia(){
            double total = 0 ; 
            for(int i = 0 ; i < not.length ; i++ ){

                  if(not[i] != null ){
                    total += not[i].dameNota();
                  }

            }

            return  total ;
        }


        public boolean estaAprobado(){

            return calcularMedia() >= 5;
        }

        public String toString(){

            String Notas_Alumnos = "El alumno " + nombre + " con Notas \n";

            for (int i = 0  ;  i < not.length ; i++ ){

                 if(not[i] != null ){

                    Notas_Alumnos += not[i].dameNota();
                 }
            }
        return Notas_Alumnos ; 
        
        }

}
