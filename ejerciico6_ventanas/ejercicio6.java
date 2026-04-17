import javax.swing.*;
import  java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JFrame;
import java.io.FileReader;
import java.util.HashMap;
import java.util.ArrayList;
public class ejercicio6 extends JFrame implements ActionListener {

    private JPanel panel ;
    private JTextField texto_español;
    private JTextField texto_ingles;
    private JButton btn_español , btn_ingles;
    private HashMap<String,String> letras = new HashMap<>();
   private ArrayList<Character>temp = new ArrayList<>();

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

	// agregamos los botones
	btn_español.addActionListener(this);
	btn_ingles.addActionListener(this);
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
	
   try(FileReader c1 = new FileReader("palabras.txt")){
	String clave ="";
	String valor ="";
	for(int c = c1.read() ; c != -1 ; c= c1.read()){
		char p = (char) c ;

		temp.add(p);
	}
	boolean esValor = false;
	for(Character c : temp){
	  if ( c == ','){
		esValor = true; // cambia al modo no agregar
	}else if ( c == '\n'){
		letras.put(clave,valor);
		clave ="";
		valor ="";
		esValor= false;
	}else{
		 if ( esValor == false){
			clave += c;  //modo clave	
		}else{
		valor += c ; // modo valor 
	}
	}
	

	}
	for(String cl : letras.keySet()){
		System.out.print(cl);
	}
	}catch(Exception e){
	System.out.println(e.getMessage());
}
}


// clave => español
// valor => ingles
public  void actionPerformed(ActionEvent e){
      if(e.getSource() == btn_español){
		String texto = texto_español.getText(); // tenemos la palabra en ingles ahora hay que buscar en español que es una clave
		// el usuario introduce la palabra en ingles y pulsa español entonces necesitamos la clave
		
	ArrayList <String> valor = new ArrayList<>(letras.values()); // tiene los valores en ingles
	Integer posicion = null ;
	for(int i = 0 ; i < valor.size() ; i++){
		String val = valor.get(i);
		if(texto.equalsIgnoreCase(val.trim())){
			posicion = i ;
	}
	}
	// la posicion nos da la clave
	if (posicion == null){
		texto_ingles.setText("No se encontro");
   }else{

	
	 ArrayList <String> clave = new ArrayList<>(letras.keySet());
	for(int i = 0 ; i < clave.size() ; i++){
		if ( i == posicion){
		    texto_ingles.setText(clave.get(i));
		}
	}

   }
	
  }else{
	// ahora el usuario va introducir una palabra en español y tenemos que pasar a ingles

	String texto_s = texto_español.getText();
	if(texto_s.isEmpty() || letras.get(texto_s) == null  ){
		texto_ingles.setText("ERROR");
	}else{
	texto_ingles.setText(letras.get(texto_s));

}

	}
}
}
