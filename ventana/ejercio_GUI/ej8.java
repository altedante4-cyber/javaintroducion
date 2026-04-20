import javax.swing.*;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class ej8 extends JFrame implements ActionListener {
	private JPanel panel;
	private JButton botones[];
	private JLabel letra;
	public ej8(){
		panel = new JPanel();
		botones = new JButton[8];
		letra = new JLabel("o");

		setSize(300,300);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		panel.add(letra);
		String posiciones [] = {"arriba","abajo","izquierda","derecha","diagonal1","diagonal2","diagonal3","diagonal4"};
		for(int i = 0 ; i < 8 ; i++){
			botones[i]=new JButton(posiciones[i]);
	}

		for(JButton b : botones){
			panel.add(b);
		}

		for(JButton c : botones){
			c.addActionListener(this);
		}
		add(panel);
		setVisible(true);

	}
	public void actionPerformed(ActionEvent e){

	}
}
