package EjerciciosP1;

public abstract class Empleado {
    
    protected  int id ;
    protected String nombre  ; 
    protected String departamento;
    protected double salarioBase ; 

    public Empleado(int id , String nombre , String departamento , double salarioBase ){
        this.id = id ;
        this.nombre = nombre ;
        this.departamento = departamento;
        this.salarioBase = salarioBase ; 
     }

    
    public abstract double calcularSalarioFinal();
  public void mostrarInfo(){
     System.out.println("El" + id + " el nombre " + nombre + "el DEpartamento " + departamento + "SALARIO BASE "  + calcularSalarioFinal()  );
  }

  public int getId() { return id; }
    public String getNombre() { return nombre; }
    public String getDepartamento() { return departamento; }
    public double getSalarioBase() { return salarioBase; }
     


}   
