package otros;
public class GestionEmpresa {

    public static void main(String[] args ){

        // Creamo el array de tipo empleado (el padre)

        Empleado [] nomina = new Empleado[4];

        //llenamos el array con diferente tipo de empelados

        nomina[0]=new EmpleadoContador("analopez", 10);
        nomina[1]=new EmpleadoVendedor("Juan perez", 10, 20);
        nomina[2]=new EmpleadoContador("carlo ruiz", 1230);
        nomina[3]=new EmpleadoVendedor("marta gomez", 1200, 850);


        // RECORREMOS EL ARRAY

        for (int i = 0 ; i < nomina.length ; i++ ){

              System.out.println(nomina[i].getNombre() + " | Seudlo Final : $ " + nomina[i].calcularSueldo() );
        }
    


// para que  el downcastin tenga sentido imagina que ahora queremos 
    // imprimri un mensaje especial pero solo para los vendedores ( por ejemplo)
    // mostrar su comision mientras que  a los contadores los tratamos de forma nomral



    // el codigo con downcastin y instaceof

    for (int i =0 ; i < nomina.length ;i++){
            
        // 1. usamos polimorfismo (funcioan para todos)
        System.out.println("Empleado " + nomina[i].getNombre() + " | SUEDLO: $ " + nomina[i].calcularSueldo());
    
        if (nomina[i] instanceof EmpleadoVendedor ){
            // 'e' se comporta como empleado pero sabes que dentro hay un vendedor
            // hacemos el cast manual para recuperar sus poderes de vendedor
            
            EmpleadoVendedor v = (EmpleadoVendedor) nomina[i];


            System.out.println("  -->  Atencion Este vendeor tiene una comision de $  " + v.getComision());
        }
    
    }



    }
    
}
