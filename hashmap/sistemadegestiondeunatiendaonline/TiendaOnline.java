package sistemadegestiondeunatiendaonline;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

public class TiendaOnline {
    private HashMap<Integer , Producto > productos ;
    private HashSet<Cliente> clientes;
    private ArrayList<ItemCarrito> carrito ;
    private String[] categorias ; 
    private int contador = 0 ; 
    public TiendaOnline(){
         this.productos = new HashMap<>();
         this.clientes = new HashSet<>();
         this.carrito = new ArrayList<>();
        this.categorias = new String[]{"Electronica", "Ropa", "Software", "Consultoria", "Libros"};
        this.contador= 0 ; 
    }


    public void  agregarProducto(Producto p ){
         productos.put(contador , p);
         contador += 1 ; 
         
    }
    public Producto   obtenerProducto(int id ){

        boolean encontrado = false ; 
        Producto p = null ; 
        for(Producto pro : productos.values()){
              
             if(pro.getid() == id ){
                encontrado = true ; 
                p = pro ; 
                break ;  
            }
        }

        if(encontrado){
            return p ;  
        }

        return null ; 
    }

    public void listarProductos(){
        
         
         for(Producto pro : productos.values() ){

                pro.obtenerDescripcion();
         }
    }


    public void listarProductosPorCategoria(String categoria ){
        // hay que validar que hayga productos con dicha categoria 

        boolean encontrado = false ; 
        for(Producto p : productos.values() ){

              if(p.getCategoria().equals(categoria)){
                 encontrado = true ; 
                 p.obtenerDescripcion();
              }
        }

        if(!encontrado){
            System.out.println("No se ha encontrado ningun producto con esa categoria");
        }
    }

    public boolean  registrarClientes(Cliente c ){
         return clientes.add(c);
    }

    public void listarClientes(){

         for(Cliente c : clientes ){
            System.out.println(c.toString());
        }
    }


    public boolean agregarAlCarrito(int idProducto , int cantidad ){

            Producto agregar_producto = null ; 
            for(Producto p : productos.values() ){

                 if(p.getid() == idProducto){
                     agregar_producto = p ;
                     break  ; 
                 }
            }
            if(agregar_producto != null ){
                ItemCarrito carrito_nuevo = new ItemCarrito(agregar_producto, cantidad);
                carrito.add(carrito_nuevo);
                return true ;                 
            }

            return false ; 
    }
    public void listarCarrito(){

         if(!carrito.isEmpty()){
             
            for(ItemCarrito i : carrito ){
                
                System.out.println(i.toString());
            }
         }
    }

    public boolean vaciarCarrito(){
          if(!carrito.isEmpty()){
          carrito.clear();
            return true  ; 
          }
          return false ; 
    }

    public double calcularTotal(){
        double total = 0 ;
        
        for(ItemCarrito i : carrito ){
             
             total += i.calcularSubtotal();
        }

        return total ; 
    }

    public double  aplicarDescuento(double porcentaje ){
            double total = calcularTotal();
            double descuento = total * (porcentaje / 100 );

            return total - descuento ; 
    }

    public void mostrarCategorias(){
         
        for(String cate : categorias){
             System.out.println(cate);
        }
    }



}
