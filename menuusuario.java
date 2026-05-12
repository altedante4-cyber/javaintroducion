

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner; 
public class menuusuario {
	

	public static void main(String[] args) {
		String user = "admin";
		 String passwd="1234";
		 String uri="jdbc:mysql://localhost:3306/bd_clientes";
		Scanner sc = new Scanner(System.in );
	
	
		
		try {
			Connection conectar = DriverManager.getConnection(uri,user,passwd);
			Statement estamento  = conectar.createStatement();
			
			int opcion = 0 ; 
			do {
				System.out.println("Ingrese opcion : \n 1.Insertar clientes \n 2.Actualisar por id \n 3.Borrar por id \n 4.Salir ");
				opcion = sc.nextInt();
				
				sc.nextLine();
				switch(opcion){
				case 1 :
					 System.out.println("Ingrese el id del cliente ");
					 String idcl = sc.nextLine();
					 System.out.println("Ingrese el nombre del cliente ");
					 String name = sc.nextLine();
					 System.out.println("Ingrese la edad del cliente ");
					 int edad = sc.nextInt();
					 

					 
					 String validar_exist = "select * from clientes where id = '"+idcl+"'";
					 
					 ResultSet resulta = estamento.executeQuery(validar_exist);
					
					boolean enco=false; 
					 while(resulta.next()) {
							 
							String valido =  resulta.getString("id");
							
							if (valido.equals(idcl)) {
								enco = true ;
							}
					}
						 
					if (!enco) {
						 String insertar = "insert into clientes(id,nombre,edad) values ( '"+idcl+"','"+name+"' , '"+edad+"')";
						 estamento.executeUpdate(insertar);
						 System.out.println(insertar);
							
					}else {
						System.out.println("El usuario esta en la base de datos   ");
					}
					 
					 conectar.close();	
					
					 break ; 
				case 2 :
						System.out.println("Ingrese el id ");
						String idconsulta = sc.nextLine();
						System.out.println("Ingrese el nuevo nombre ");
						String nuevo_nombre = sc.nextLine();
						
						String cons = "update clientes set = '"+nuevo_nombre+"' where id = '"+idconsulta+"'";
						String consulta1 = "select * from clientes where id = '"+idconsulta+"'";
						boolean encoe = false ;
						
						ResultSet es = estamento.executeQuery(consulta1);
						
						while(es.next()) {
							 
							if(idconsulta.equals(es.getString("id"))) {
								  encoe = true ;
							}
						}
						
						if (encoe) {
							estamento.executeUpdate(cons);
							System.out.println("se actuliso correctamente ");
						}else {
							System.out.println("no se encontro al usuario ");
						}
						conectar.close();	
						break;
				
						
				case 3 :
					System.out.println("Ingrse el id a borrar");
					String idborrar =sc.nextLine();
				
					boolean p = false ;
					
					
					String borr = "delete from clientes where id = '"+idborrar+"'";
					
					String consulta = "select * from clientes where id = '"+idborrar+"'";
					ResultSet en = estamento.executeQuery(consulta);
					
					while(en.next()) {
						
						if(idborrar.equals(en.getString("id"))) {
							p = true;
						}
					}
					
					if(p) {
						estamento.executeUpdate(borr);
						System.out.println("Se ha borrado correctamente ");
					}else {
						System.out.println("No se a podido borrar");
					}
					
				
					conectar.close();
					
					break ; 
					
				case 4:
					System.out.println("Ingrese el id a buscar ");
					String buscarid = sc.nextLine();
					
					String consulta2 = "select * from clientes where id = '"+buscarid+"'";
					
					ResultSet ens = estamento.executeQuery(consulta2);
					boolean encontrado = false ; 
					while(ens.next()) {
						 
						if(buscarid.equals(ens.getString("id"))) {
							encontrado = true ; 
						}
					}
					
					if(encontrado) {
						System.out.println("El usuario existe ");
					}else {
						System.out.println("el usuario no existe ");
					}
					
					break;
				default :
					System.out.println("Ingrese los numeros correctamente  ");
					
					break ;
				
				}
				conectar.close();
				
				
			}while(opcion != 5 );
			
			System.out.println("Ha salido del programa ");
			
		}catch(SQLException e ) {
			System.out.println(e.getMessage());
		}
	}


}
