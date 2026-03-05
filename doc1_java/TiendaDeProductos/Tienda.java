package TiendaDeProductos;

import java.util.ArrayList;

public class Tienda {

    private ArrayList<Producto> catalogo = new ArrayList<>();


    public boolean agregarProducto(Producto p ){
        return catalogo.add(p);
    }
    public void mostrarCatalogo(){
        System.out.println("\n--- CATÁLOGO DE LA TIENDA ---");
        for(int i = 0 ; i< catalogo.size() ; i++ ){
            Producto p = catalogo.get(i);

            System.out.println(p);
        }
    }

    public double calcularValorTotal(){
        // ojo//
        double contador = 0 ; 
        for(int i = 0 ; i < catalogo.size() ; i++ ){

                Producto p  = catalogo.get(i);

                contador += (p.getPrecio() * p.getStock());             
        }
        return contador ;
    }

    public Producto  buscarPorNombre(String nombre ){
        
        for(int i = 0 ; i < catalogo.size() ; i++ ){

              Producto p = catalogo.get(i);

              if(p.getNombre().equals(nombre)){
                   return p ;  // si lo encuentra devolvemos el objeto completo  
              }
            
            }

            return null ; // si termina el for no llo vio devuevle null
    
    }


    
}
