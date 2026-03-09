package EJERCICIOIMPRESORA;

public class Main {

    public static void main(String[] args ){
        // 1. Instanciamos la Impresora (El motor del sistema)
        Impresora miImpresora = new Impresora();

        System.out.println("--- PRUEBA 1: Sobrecarga (Mensajes Simples) ---");
        // Probamos imprimir un String simple
        miImpresora.imprimir("Iniciando sistema de impresión universal...");

        // Probamos imprimir un array de Strings (lista de tareas)
        String[] tareas = {"Limpiar cabezales", "Revisar toner", "Calibrar papel"};
        miImpresora.imprimir(tareas);

        System.out.println("\n--- PRUEBA 2: Polimorfismo (Documentos Especializados) ---");
        
        // Creamos diferentes tipos de documentos
        // Aunque todos se guardan en variables de tipo 'Documento', se comportan como sus hijos
        Documento docGenerico = new Documento("Manual", "Instrucciones de uso", "TXT");
        Documento pdf = new DocumetnoPDF("Contrato_Final", "Este es un contrato legal.", "pdf"); 
        Documento excel = new DocumetoExel("Presupuesto_2024", "100, 200, 300, 400", "50");

        // Los imprimimos individualmente para ver sus formatos únicos
        miImpresora.imprimir(docGenerico);
        miImpresora.imprimir(pdf);   // Debería mostrar encabezados de PDF
        miImpresora.imprimir(excel); // Debería mostrar formato de celdas/tablas

        System.out.println("\n--- PRUEBA 3: Impresión en Lote (Informe) ---");
        
        // Creamos un array de la clase padre que contiene a todos los hijos
        Documento[] loteDeTrabajo = {
            docGenerico, 
            pdf, 
            excel, 
            new DocumetnoPDF("Factura_001", "Pago de servicios", "hooa")
        };

        // Ejecutamos el método que procesa la lista completa
        miImpresora.imprimirInforme(loteDeTrabajo);
        
        System.out.println("\n--- PRUEBAS FINALIZADAS CON ÉXITO ---");
        
    }
    
}
