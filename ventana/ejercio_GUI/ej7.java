
import javax.swing.*;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.io.FileReader;
import java.io.FileWriter;
public class ej7 extends JFrame implements ActionListener {
	private JPanel panel;
	private JButton btn1,btn2;
	private JTextField  dia,mes,año;
	private JTextArea texto ;
	private int contador_dia=0  ;

	public  ej7(){
		panel = new JPanel();
		btn1 = new JButton("delante");
		btn2=new JButton("atras");
		texto = new JTextArea(5,20);
		dia = new JTextField(12);
		mes = new JTextField(12);
		año = new JTextField(12);


	// en java swing usamos 
	// JTextField => para una sola linea de texto
	// JTextArea => para varias lineas de texto sintaxis ( JTextArea area = new JTextArea(5,20);

	  // agreagr los botones a action listenes

	 btn1.addActionListener(this);
	 btn2.addActionListener(this);
	//ahora configuramos la pantalla
	setTitle("Mi blog");
	setSize(200,200);
	setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	dia.setEditable(false);
	mes.setEditable(false);
	año.setEditable(false);
	dia.setText("17");
	mes.setText("04");
	año.setText("2026");
	// agregamos al panel todos los elementos 
	panel.add(texto);
	panel.add(dia);
	panel.add(mes);
	panel.add(año);
	panel.add(btn1);
	panel.add(btn2);
	add(panel);
	contador_dia = Integer.parseInt(dia.getText());

	setVisible(true);

}

@Override
public void actionPerformed(ActionEvent e){
	if(e.getSource() == btn1){
		String dia_s = String.valueOf(contador_dia++);
		if(dia_s.length() < 2){
		      dia.setText("0"+dia_s);
	}else{
		dia.setText(dia_s);
	}
	
	String archivo=dia.getText() +mes.getText() + año.getText();
		int caracter;

	try(FileReader leer = new FileReader(archivo)){
		while((caracter=leer.read()) != -1){
			char c = (char) caracter;
		System.out.println(c);
	}
	}catch(Exception ex ){
		System.out.println(ex.getMessage());
	}

	//escribimos el texto si hay contenido en un nuevo archivo
	String obtener_contenido=texto.getText();
	if(!obtener_contenido.isEmpty()){
		String nuevo_archivo= dia.getText() + mes.getText() + año.getText();
		try(FileWriter escribir = new FileWriter(nuevo_archivo)){
    			for(int i = 0 ; i < obtener_contenido.length() ; i++){
                        char c = obtener_contenido.charAt(i);
                        escribir.write(c);
        	}  
	}catch(Exception ep){
			System.out.println(ep.getMessage());
		}
	}
	}else{
		String dia_s = String.valueOf(contador_dia--);
                if(dia_s.length() < 2 ){
                      dia.setText("0"+dia_s);
        }else{
                dia.setText(dia_s);
        }

	}
}
}
