public class ej1{
	public static void main(String [] args){


	}
public static void registrar_usuario(String nombre, int edad, String email) 
        throws NombreInvalidoException, EdadInvalidaException, EmailInvalidoException {
    
    boolean valido = true;
    
    // Validar nombre
    if (nombre == null || nombre.isEmpty()) {
        valido = false;
        throw new NombreInvalidoException("nombre vacio");
    }
    
    // Validar edad
    if (edad < 18 || edad > 120) {
        valido = false;
        throw new EdadInvalidaException("edad no correcta (debe estar entre 18 y 120)");
    }
    
    // Validar email
    int posicion_arroba = email.indexOf("@");
    if (posicion_arroba == -1 || email.indexOf(".", posicion_arroba + 1) == -1) {
        valido = false;
        throw new EmailInvalidoException("email invalido (debe tener @ y un punto después)");
    }
    
    // Si llegamos aquí, todo es válido
    System.out.println("Usuario registrado correctamente");
}


}
