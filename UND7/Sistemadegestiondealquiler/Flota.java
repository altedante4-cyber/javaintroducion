package Sistemadegestiondealquiler;

public class Flota{

        private Vehiculo [] inventario = new Vehiculo[10]  ;
        private int contador = 0 ; 



        public boolean agregarVehiculo(Vehiculo v ){

            // validar que hayga espacio 


            // if(contador < 0 || contador > 10 ){
            //     return false ; 

            // } esto es esta mal por uqe si el array inventario tiene tamano 10 los indices validos son del 0 al 9 
            //  si el contador llega a 10 e intentas hacer inventario[10] el programa explitara con un arrayIndexoutboundexception

            ///ESTO ES LA SOLUCION
            /// 
            /// 
            /// 
            /// 
            /// /
            /// 
            /// 
            
            if (contador >= inventario.length ){ // si ya esta lleno 
                System.out.println("Errro flota llena ");
                return false ; 

            }

            inventario[contador++] = v ;
            return true ; 
        }


        public void mostrarPresupuesto(String matricula , int dias ){

             // buscamos el vehivulo por matricula
             //validamos que hayga vehiculos en el inventario 
            

             if(inventario.length > 0 ){
                    boolean encontrado  = false ; 
                    for (int i = 0 ; i  < inventario.length ; i++ ){

                        if(inventario[i] != null && inventario[i].getMatricula().equals(matricula) ){
                            // calculamos precio 
                            encontrado = true ; 

                            inventario[i].calcularAlquiler(dias);
                            break;

                        }
                    }

                    if (!encontrado){
                        System.out.println("No se ha encontrado ningun vehivculo con esa matricula ");
                    }
                 
             }else{
                System.out.println("No hay ningun vehiculo en el inventrario ");
             }
        }

        public void mostrarFlota(){

            double ganancia = 0 ; 

            for (int i = 0 ; i < inventario.length ; i++ ){

                if(inventario[i] != null ){

                    System.out.println(inventario[i].toString() );

                    ganancia += inventario[i].getTarifaBase();
                }
            }
            System.out.println("=============ganancia por alquilar la flota por un dia ");
            System.out.print("GANANCIA ES " + ganancia );
        }
}
