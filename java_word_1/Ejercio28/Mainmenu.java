package Ejercio28;

public class Mainmenu {
    public static void main(String[] args) {
        
        // Creamos un array del tipo PADRE
        ItemMenu[] pedido = new ItemMenu[3];

        // Guardamos HIJOS en el array del padre (Polimorfismo)
        pedido[0] = new Bebida("Jugo Mora", "Fruta natural", 10.0, "Grande");
        pedido[1] = new Postre("Mousse", "Chocolate amargo", 15.0, 300);
        pedido[2] = new PlatoPrincipal("Ensalada Caesar", "Con pollo", 25.0, 15);

        // Recorremos y cada uno calcula su precio diferente
        for (ItemMenu item : pedido) {
            System.out.println(item.toString() + " | Precio Final: " + item.calcularPrecioFinal());
        }
    }
}