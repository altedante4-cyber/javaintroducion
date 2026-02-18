package javaintroducion;

public class Gestionnotas {

    private Alumno [] misalumnos;
    private int contado;
    


    // necesitamos inicialisar el consturctor   


    public Gestionnotas(){

        this.misalumnos = new Alumno[20];
        this.contado = 0 ; 
    }

    // para buscar un alumnos necesesitamos un booleano 

    public boolean buscaralumnos(String nombre ){

        for(int i  = 0 ; i < this.contado  ; i++ ){

             if(misalumnos[i].damenombre().equals(nombre)){
                 return true; 
             }
        }         
        
        return false ; 
    }


    /// ahora para poder modificar la nota tenemos que hacer un medtod seter que nos de  el nombre del alumno y la nota  que quiere modificar
    

    public boolean modificarnota(String nombre , int nota){
                
        for(int i  = 0 ; i < this.contado  ; i++ ){

             if(misalumnos[i].damenombre().equals(nombre)){
                
                this.misalumnos[i].modifi(nombre, nota);
                return true; 
             }
        }         
        
        return false ; 
         
    }

    // agregar a un alumno

    public boolean agregaralumon (Alumno a  ){

         if(contado < this.misalumnos.length){

                this.misalumnos[contado] = a;
                contado ++ ; 
                return true;
         }

         return false ; 
    }

    // tenemos que devolver un geter para saber la nota media de las notas de los alumnos

    public double mostrarmedianotas(){
        int contadorinterno = 0 ; 


        for (int i = 0 ; i < this.contado ; i++ ){

            contadorinterno +=  misalumnos[i].damenota();
              
        }

        return contadorinterno / this.misalumnos.length;
        
    }


    // 
    public double mostrarmedianotasmenores(){
        int contadorinterno = 0 ; 


        for (int i = 0 ; i < this.contado ; i++ ){
        
            if(misalumnos[i].damenota() < 5  ){
                contadorinterno +=  misalumnos[i].damenota();

            }
              
        }

        return contadorinterno / this.misalumnos.length;
        
    }


    public String mostraralumnosmejoresnotas(){
        
        String nombres_alumnos = "";


        for(int i = 0 ; i  < contado ; i++ ){

             if(misalumnos[i].damenota() > 9 ){
                  
                 nombres_alumnos += misalumnos[i].damenombre() + " ";
             }
        }

        return nombres_alumnos ; 
         
    }
    


    public String mostraralumnospeoresnotas(){
        
        String nombres_alumnos = "";


        for(int i = 0 ; i  < contado ; i++ ){

             if(misalumnos[i].damenota() < 4 ){
                  
                 nombres_alumnos += misalumnos[i].damenombre() + " ";
             }
        }

        return nombres_alumnos ; 
         
    }
    




    public String toString(){
        
            String valor = "";    
        for (int i = 0 ; i < contado  ; i++ ){

              valor += misalumnos[i].damenombre() + " ";
            
            }        



            return valor ; 
    }



}
