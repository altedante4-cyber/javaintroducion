
import javax.swing.*;
public class ej9 extends JFrame {

	private JPanel panel;
	private JTextField texto , n1 , n2 , n3 , n4 ;
	private JLabel title, numero_letras , numero_espacios , numero_vocales , numeros_consonantes ; 
	private int contador = 0;
	public ej9(){
		panel = new JPanel();
		title = new JLabel("Introduce texto");
		texto = new JTextField(12);
		numero_letras = new JLabel ("Numero de letras");
		n1 = new JTextField(5);
		numero_espacios = new JLabel("Numero espacios");
		n2 = new JTextField(5);
		numero_vocales = new JLabel("Numero de vocales");
		n3 = new JTextField(5);
		numeros_consonantes = new JLabel("Numero de consoantes");
		n4 = new JTextField(5);


		setSize(400,400);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	       	
		panel.add(title);
		panel.add(texto);
		panel.add(numero_letras);
		panel.add(n1);
		panel.add(numero_espacios);
		panel.add(n2);
		panel.add(numero_vocales);
		panel.add(n3);
		panel.add(numeros_consonantes);
		panel.add(n4);
		add(panel);
		setVisible(true);
	}
}
