package EjerciciosP1;

import java.util.ArrayList;
import java.util.HashSet;

public class SistemaEmpleados {
    
    private ArrayList<Empleado> empleados;
    private HashSet<String> departamentos;
    
    public SistemaEmpleados() {
        empleados = new ArrayList<>();
        departamentos = new HashSet<>();
    }
    
    public void agregarEmpleado(Empleado emp) {
        empleados.add(emp);
        departamentos.add(emp.getDepartamento());
    }
    
    public void mostrarTodosEmpleados() {
        System.out.println("\n=== LISTA DE EMPLEADOS ===");
        for (Empleado emp : empleados) {
            emp.mostrarInfo();
        }
    }
    
    public void mostrarDepartamentos() {
        System.out.println("\n=== DEPARTAMENTOS ===");
        for (String depto : departamentos) {
            System.out.println("- " + depto);
        }
    }
    
    public double calcularSalarioPromedioPorDepartamento(String depto) {
        double suma = 0;
        int contador = 0;
        for (Empleado emp : empleados) {
            if (emp.getDepartamento().equals(depto)) {
                suma += emp.calcularSalarioFinal();
                contador++;
            }
        }
        return contador > 0 ? suma / contador : 0;
    }
    
    public void mostrarPromediosPorDepartamento() {
        System.out.println("\n=== SALARIOS PROMEDIO POR DEPARTAMENTO ===");
        for (String depto : departamentos) {
            double promedio = calcularSalarioPromedioPorDepartamento(depto);
            System.out.println(depto + ": $" + String.format("%.2f", promedio));
        }
    }
    
    public static void main(String[] args) {
        SistemaEmpleados sistema = new SistemaEmpleados();
        
        // Agregar empleados
        sistema.agregarEmpleado(new EmpleadoTiempoCompleto(1, "Juan", "IT", 3000));
        sistema.agregarEmpleado(new EmpleadoTiempoCompleto(2, "María", "IT", 3500));
        sistema.agregarEmpleado(new EmpleadoTiempoPartial(3, "Carlos", "Ventas", 2000));
        sistema.agregarEmpleado(new Gerente(4, "Ana", "IT", 5000));
        sistema.agregarEmpleado(new EmpleadoTiempoPartial(5, "Luis", "RH", 1800));
        sistema.agregarEmpleado(new Gerente(6, "Pedro", "Ventas", 4500));
        
        // Mostrar información
        sistema.mostrarTodosEmpleados();
        sistema.mostrarDepartamentos();
        sistema.mostrarPromediosPorDepartamento();
    }
}
