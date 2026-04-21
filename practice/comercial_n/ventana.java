import javax.swing.*;
import java.awt.event.*;
import java.io.*;
import java.io.FileReader;
public class ventana extends JFrame implements ActionListener {
	private JPanel panel;
	private JTextArea resultados;
	private JButton calcular_salario , limpiar;

	public ventana(){
		panel = new JPanel() ;
		resultados = new JTextArea(12,12);
		limpiar = new JButton("Limpiar");
		calcular_salario = new JButton("CALCULAR SALARIO"); 

		limpiar.addActionListener(this);        
                calcular_salario.addActionListener(this);
		setSize(400,400);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		panel.add(resultados);
		panel.add(calcular_salario);
		panel.add(limpiar);
		

		add(panel);
		setVisible(true);
	}
	@Override

	public void actionPerformed(ActionEvent e ){
		
		if(e.getSource() == calcular_salario){
			String cad = "";
			try(FileReader leer = new FileReader("jornada.txt")){

				int caracter;
				while ((caracter = leer.read()) != -1){
					cad += (char) caracter;
				
				}
			}catch(IOException p){
				System.out.println("no se pudo leer el archivo");
			}

			String [] separar = cad.split("\n");
		boolean valido = false;
		for(int i = 0 ; i  < separar.length ; i++){
				String separar_coma [] = separar[i].split(",");
				String nombre_trabajador = separar_coma[0];
				String toneladas_pro = separar_coma[1];
				String quintales = separar_coma[2];
	
				if(nombre_trabajador != "" && toneladas_pro != "" && quintales != ""){
					 // ahora una vez aqui dentro validamos lo siguiente que toneladas y quintales senan enteros
					 try{
						double tone = Double.valueOf(toneladas_pro);
						double quint = Double.valueOf(quintales);
						Trabajador n1 = new Trabajador(nombre_trabajador,tone,quint);
						
						resultados.append(n1.toString() + "\n" + "Pago por toneladas " +   tone * 100  + "\n" + "Pago por quintales " +   quint * 2 + "\n" + "TOTAL  " + n1.calcularPago()  + "\n"  );
						}catch(NumberFormatException k ){
						System.out.println("No son numeros algunos campos del archivo ");
					}
				}

			}

		}
		
	}
}
