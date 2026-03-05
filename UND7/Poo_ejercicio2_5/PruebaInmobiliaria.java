package Poo_ejercicio2_5;

public class PruebaInmobiliaria {
    public static void main(String[] args) {
        
        // Creamos un array de la clase padre para guardar distintos tipos de inmuebles
        Inmuebles[] listaInmuebles = new Inmuebles[4];

        // 1. Piso Nuevo (< 15 años) en Planta Baja (0)
        // Precio base 100.000 -> -1% por años = 99.000€
        listaInmuebles[0] = new Pisos("Calle Luna 10", 80, 100000.0, 5, 0);

        // 2. Piso Antiguo (> 15 años) en Planta 5
        // Precio base 100.000 -> -2% años + 3% planta = 101.000€
        listaInmuebles[1] = new Pisos("Avenida Sol 42", 95, 100000.0, 20, 5);

        // 3. Local Grande (> 50m2) con 1 ventana (Nuevo - 10 años)
        // Precio base 100.000 -> -1% años + 1% metros - 2% ventanas = 98.000€
        listaInmuebles[2] = new Locales("Calle Mayor 1", 60, 100000.0, 10, 1);

        // 4. Local Pequeño (< 50m2) con 6 ventanas (Antiguo - 30 años)
        // Precio base 100.000 -> -2% años + 2% ventanas = 100.000€
        listaInmuebles[3] = new Locales("Pasaje Centro 5", 40, 100000.0, 30, 6);

        System.out.println("===== INFORME DE INMOBILIARIA =====");
        double valorTotalCartera = 0;

        for (Inmuebles i : listaInmuebles) {
            if (i != null) {
                double precioFinal = i.calcularPrecioInmuble();
                valorTotalCartera += precioFinal;

                // Usamos el toString() que definiste para mostrar los datos
                System.out.println(i.toString());
                System.out.printf("   > Precio Final calculado: %.2f€%n", precioFinal);
                
                // Un pequeño extra: ¿Es Piso o Local?
                if (i instanceof Pisos) {
                    System.out.println("   > Tipo: Vivienda");
                } else if (i instanceof Locales) {
                    System.out.println("   > Tipo: Comercial");
                }
                System.out.println("-----------------------------------");
            }
        }

        System.out.printf("TOTAL VALOR DE MERCADO: %.2f€%n", valorTotalCartera);
    }
}