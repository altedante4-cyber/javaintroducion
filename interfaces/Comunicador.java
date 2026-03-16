package Intefaces;

public interface Comunicador {
    // por defecto los atributos son public fianl static 
    int CTE=10;
    // los metodos son abstractos y publicos 
    
    void enviarMensaje(String destino , String mensaje );
    
}
