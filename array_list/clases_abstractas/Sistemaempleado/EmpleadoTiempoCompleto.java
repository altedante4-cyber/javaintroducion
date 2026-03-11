package Sistemaempleado;

public class EmpleadoTiempoCompleto extends Empleado  {
    
    private int aniosantiguedad ;
    public EmpleadoTiempoCompleto(String nombre , double salarioBase , int aniosantiguedad){
        super(nombre, salarioBase);
        this.aniosantiguedad = aniosantiguedad;
    }

    @Override
    public double calcularSalario(){
        return salarioBase + (aniosantiguedad * 50);
    }

    
    
}
