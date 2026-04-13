import javax.swing.*;
import  java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JFrame;
import java.io.FileReader;
import java.util.HashMap;
public class ejercicio6 extends JFrame  {
    private JPanel panel ;
    private JTextField texto_español;
    private JTextField texto_ingles;
    private JButton btn_español , btn_ingles;
    public ejercicio6(){
        setTitle("TRADUCTOR");
	setSize(300,300);
	setLocation(100,100);
	setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	panel = new JPanel();
	texto_español = new JTextField(12);
	texto_ingles = new JTextField(12);
	btn_español = new JButton("Español");
	btn_ingles = new JButton("Ingles");

	//añadimos componente alpanel 
	panel.add(texto_español);
	panel.add(texto_ingles);
	panel.add(btn_español);
	panel.add(btn_ingles);

	//vinculamos  el panel a la ventana
	this.setContentPane(panel);
	//hacemos visible
	this.setVisible(true);
    }

   public void leerarchivo(){
	
   try{
   FileReader c1 = new FileReader("palabras.txt");
        
	int caracter;
        while((caracter = c1.read()) != -1){
                System.out.println((char)caracter );
}
c1.close();
	}catch(Exception e){
	System.out.println(e.getMessage());
}
}
}
