package ejercicio2registrodeestudiantehasmap;

import java.util.HashMap;

public class Universidad {

    private HashMap<String,Estudiante> registros ;

    public Universidad(){
         this.registros = new HashMap<>();
    }

    public boolean registrarEstudiante(Estudiante e ){
         if (registros.containsKey(e.getMatricula())){return false ; }
         registros.put(e.getMatricula(), e);
         return true ; 
    }
    public Estudiante BuscarEstudiante(String matricula ){
        String clave_devolver = "";
        for(String claves : registros.keySet() ){
               if (claves.equals(matricula)){
                    clave_devolver += claves;
                    break;
            }
         }
         if(clave_devolver != ""){
               return registros.get(clave_devolver);
         }
         
         return null ; 
    }

    public boolean actualizarPromedioEstudiante(Estudiante e , double promedio_nuevo ){
         String clave_devol = "";
        for(String clave : registros.keySet() ){
             
              if(clave.equals(e.getMatricula())){
                    clave_devol += clave;
                    break;
              }
        }

        if (clave_devol != ""){
             Estudiante calcular_promedio=  registros.get(clave_devol);
             calcular_promedio.setPromedio(promedio_nuevo);
            return true ;
            }


            return false ; 
        }


    public void mostrarEstudiantesDeUnacarreraEspecifica(String nombre_carrera ){
          
         for(Estudiante e : registros.values() ){
              if(e.getCarrera().equals(nombre_carrera)){
                 System.out.println(e.toString());
              }
         }
    }

    
    
}
