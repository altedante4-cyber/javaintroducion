package UD11;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class insertarbasedatos {

    public static void main(String[] args) {
        // Datos de conexión
        String user = "admin";
        String contraseña = "1234";
        String uri = "jdbc:mysql://localhost:3306/bd_clientes";
        
        // El bloque try-with-resources asegura que la conexión se cierre sola
        try{
           Connection connection = DriverManager.getConnection(uri, user, contraseña);
            System.out.println("Conexión establecida con éxito.");
                   
            
        } catch (SQLException e) {
            System.out.println("Error de SQL: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("Error general: " + e.getMessage());
        }
    }
}
