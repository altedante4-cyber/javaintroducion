package javaintroducion;

public class Tienda {
    private Producto[] miproducto;
    private int contador;

    public Tienda() {
        this.miproducto = new Producto[10];
        this.contador = 0;
    }

    public boolean darAlta(Producto p) {
        if (contador < this.miproducto.length) {
            miproducto[contador] = p;
            contador++;
            return true;
        }
        return false;
    }

    public Producto getbuscarproducto(String nombre) {
        for (int i = 0; i < contador; i++) {
            // Comparamos el nombre ignorando mayúsculas/minúsculas
            if (miproducto[i].getNombre().equalsIgnoreCase(nombre)) {
                return miproducto[i];
            }
        }
        return null;
    }
   

     //borrar un producto del inventario 

        public boolean  getborrarproducto(String nombre ){
            
            for(int i = 0 ; i < contador  ; i++ ){

                    if( miproducto[i] != null && miproducto[i].getNombre().equals(nombre)){
                         miproducto[i] = null; 
                        return true ; 
                        
                    }

            }

            return false ; 
        }
    
    public boolean setmodificarstock(String nombre, double nuevoPrecio, int nuevoStock) {
        Producto p = getbuscarproducto(nombre);
        if (p != null) {
            p.setPrecio(nuevoPrecio);
            p.setStock(nuevoStock);
            return true;
        }
        return false;
    }
}