package javaintroducion;

public class Alumno {

        private String nombre ;
        private int nota;
    // Que gestiona las notas de una clase de 20 alumnos de los cuales sabemos el nombre y la nota . El programa debe ser vapaz de : 
    //1.Buscar un alumno
    // 2.MOdificar su nota
    // Realizar la media de todas las notas
    // Realizar la media de las notas menores de 5
    // Mostrar el alumno que mejores notas ha sacado
    //6.MOstra el alumnos que peores notas ha sacado 


    public Alumno(String nombre , int nota){
        this.nombre = nombre;
        this.nota = nota ; 
    }


    // necesitamos un geteer para saber si queremos el nombre del alumno o saber la nota del alumno


    public String damenombre(){
        return this.nombre; 
    }
    public int damenota(){
        return this.nota ; 
    }


    // necesitamos metodos seter para agregar las nota o querermodificar la nota  o el nombre del alumonnnn


    //necesitamos un metodo seter para poder modficiar  la nota 


    public void  modifi(String nombre , int nota ){

         this.nombre = nombre ;
         this.nota = nota ; 
    }




    public String toString(){

        return "el nombre " + nombre + "la nota " + nota ; 
    }

}
