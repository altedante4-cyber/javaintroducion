package javaintroducion;

public class Tienda {
    private Producto[] miproducto;
    private int contador;

    public Tienda() {
        this.miproducto = new Producto[10];
        this.contador = 0;
    }

    // fallos tipicos que en el constructor  no iniciliasar los vlaores y que los valores introducidos son valores y si son invalidos parasar  a un valor por defecto
    // un consturctor por defecto tiene dentor tambien  los atributos 
    //
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
        return null; // ojo  con este el objeto siempre devuevle null si no encutentra ninguno 
        
    }
   

     //borrar un producto del inventario 

    public boolean  getborrarproducto(String nombre ){
            Producto p  = getbuscarproducto(nombre);
             
            if( p != null ){
                p.setNombre("");
                p.setPrecio(contador -- );
                p.setStock(0);
                return true ; 
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