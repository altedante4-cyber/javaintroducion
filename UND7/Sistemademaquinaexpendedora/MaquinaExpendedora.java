package Sistemademaquinaexpendedora;

public class MaquinaExpendedora {

    private Producto [] estante = new Producto[5];
    private double saldoCaja;



    public void insertarProducto(int posicion , Producto p ){

          // guarda un producto en una posicion del array ( 0 - 4 )

          // para guardar un producto necesitamos validar que haya campo

          if(posicion < 0 || posicion > 4 ){
             
              System.out.println("Posicino invalida carnal ");
          }

          if ( estante[posicion] == null ){
                estante[posicion] = p ; 
                System.out.println("Agregado correctamente ");
          }else{
            System.out.println("La posicion que esta ingresando se encuentra ocupada ");
          }

        }

    public boolean   comprar(int poscino , double dineroIngresado){

        // 1 guardas : validamos los fallos primero  y salimos con return false

        if (poscino < 0 || poscino >= estante.length ){

            System.out.println("Error posciion fuera de rango ");
            return false ; 
        }

        Producto p = estante[poscino] ; // atajo para no escribir estante[posicion] muchas veces

        if(p == null ){
            System.out.println("Error Casilla vacia ");
            return false ;
        }

        if(dineroIngresado < p.getPrecio() ){
            System.out.println("Error dinero insuficeinte faltan : "+ (p.getPrecio() - dineroIngresado ));
            return false ;
        }

        if(p.getcatidadstock() <= 0 ){
            System.out.println("Error producto agotado ");
            return false ; 
        }

        // 2. flujo principal si llegamos aqui tood es correcto
        p.quitarCatidadstock();
        saldoCaja += p.getPrecio(); // solo sumamo el precio no el dineor total ingresado 

        double cambio = dineroIngresado - p.getPrecio();
        System.out.println("Venta existora su cambio " + cambio );

        return true ; 

    }

    public void getcatidadvendida(){
        System.out.println("La cantidad vendidad es de  " + saldoCaja );
    }


    public void verproducto(){

        for (int i = 0 ; i < estante.length ;i++ ){

            if(estante[i] != null ){

                System.out.println(estante[i].toString());
            }
        }
    }


    
}
