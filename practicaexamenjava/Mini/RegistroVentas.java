package Mini; 

public class RegistroVentas {

    private Producto [] productos;
    private int contador ; 

    public RegistroVentas(){
        this.productos = new Producto[30];
        this.contador = 0 ; 
    }

    public boolean agregarProducto(Producto p ){

          if(contador < productos.length ){
             
             productos[contador++ ] = p ; 
             return true ; 
          }

          return false; 
    }


    public Producto  buscarProducto(int id ) {
         
        Producto nuevo = null ; 
        for(int i = 0 ; i < contador ; i++ ){
             
             if(productos[i].getid() == id ){
                 nuevo = productos[i];
                 break;
             }
        }
        return nuevo ; 
    }


    public Producto buscarProducto(String nombre ){
        Producto nuevo = null ; 
        for(int i =0  ; i < contador ; i++ ){

            if(productos[i].getNombre().equals(nombre)){

                    nuevo = productos[i];
                    break ; 
            }
        }

        return nuevo ; 
    }


    public boolean buscarId(int id ){

        for(int i = 0 ; i < contador ; i++ ){
            if(productos[i].getid() == id  ){
                return true ; 
            }
        }
        return false ; 
    }
    public void  editarPrecio(int id , double nuevoPrecio ){
        // para editar el producto el producto tiene que existir 
        // busca po el id y asigna un nuevoprecio 

        for(int i = 0 ; i < contador ; i++ ){

            if(productos[i].getid() == id ){
                productos[i].setPrecio(nuevoPrecio);
                break; 
            }
        }
    }



    public void eliminarProducto(int id ){
    
        for(int i  = 0; i < contador ; i++ ){
            
             if(productos[i].getid()== id  ){

                productos[i] = null; 
                break; 
             }
        }
        

    } 



    public double calcularTOtalMensual(){

        double total = 0 ; 
        for(int i  = 0 ; i< contador ; i++ ){
            
            if(productos[i] != null ){
                 total += productos[i].getprecio();

            }
        }

        return total ; 
    }

    public void mostarProducto() {

        for (int i = 0 ; i < productos.length ; i++ ){
             if(productos[i]  != null ){
                 System.out.println(productos[i].toString());

             }
        }
    }

    
}
