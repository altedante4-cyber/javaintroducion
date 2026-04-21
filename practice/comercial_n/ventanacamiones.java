import javax.swing.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.io.FileWriter;
import java.io.*;
public class ventanacamiones extends JFrame implements ActionListener {

	private JPanel panel;
	private JTextField Producto , Toneladas , Maleza;
	private JButton registrar_camion , mostrar_camiones , finalizar_compra ;
	private JTextArea listar_camiones_registrados;
	private JLabel enun1 , enun2 , enun3;
	private ArrayList<Camion> listar_camiones = new ArrayList<>();
	private Camion n ;
	public ventanacamiones(){
		panel = new JPanel();
		enun1 = new JLabel("Producto");
		Producto = new JTextField(12);
		enun2 = new JLabel("Toneladas");
		Toneladas = new JTextField(12);
		enun3 = new JLabel("Maleza");
		Maleza= new JTextField(12);
		finalizar_compra = new JButton("Finalizar Compra");
		registrar_camion = new JButton("Registrar camion");
		mostrar_camiones = new JButton ("Mostrar camiones");
		listar_camiones_registrados = new JTextArea(12,12);

		finalizar_compra.addActionListener(this);
		registrar_camion.addActionListener(this);
		mostrar_camiones.addActionListener(this);
		setSize(400,400);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		panel.add(enun1);
		panel.add(Producto);
		panel.add(enun2);
		panel.add(Toneladas);
		panel.add(enun3);
		panel.add(Maleza);
		panel.add(registrar_camion);
		panel.add(mostrar_camiones);
		panel.add(listar_camiones_registrados);	       
		panel.add(finalizar_compra);
		add(panel);
		setVisible(true);
		
	}

	@Override

	public void actionPerformed(ActionEvent e){
		boolean valido = true;

		if(e.getSource() == registrar_camion){
					String campos []= {Producto.getText() , Toneladas.getText() , Maleza.getText()};

			for(String c : campos){  if ( c.isEmpty()) { valido = false ; } }
			try{
				valido=Double.valueOf(Toneladas.getText()) > 0;
				valido =Double.valueOf(Maleza.getText()) >= 0 && Double.valueOf(Maleza.getText()) <= 100 ;
			}catch(NumberFormatException p ){
				System.out.println("tiene que ser un numero");
			}
			
			String p = Producto.getText();
			for(int i = 0 ; i < p.length() ; i++){
				char c = p.charAt(i);
				if ( c >= '0' && c <= '9'){
					valido = false ;
				}
			}


			if(valido){
				 n = new Camion(p , Double.valueOf(Toneladas.getText()) , Double.valueOf(Maleza.getText()));
				listar_camiones.add(n);
			 
				JTextField limpiar [] = { Producto , Toneladas , Maleza };
                        	for(JTextField  c : limpiar){
                                        c.setText("");
                                }

			}
		}else if ( e.getSource() == mostrar_camiones){
			listar_camiones_registrados.setText("");
			for(Camion c : listar_camiones){
				listar_camiones_registrados.append(c.toString() + "\n" );
			}
		}else if ( e.getSource() == finalizar_compra){

			try(FileWriter escribir = new FileWriter("compras.txt")){
				for(int i = 0 ; i < listar_camiones.size() ; i++){
						Camion  n = listar_camiones.get(i) ;
						String p = n.toString();
						escribir.write(p + "\n" );
						
					 
				}
			}catch(IOException p){
				System.out.println("No se puedo escribir correctamente " ) ; 
			}
		}

	}
}
