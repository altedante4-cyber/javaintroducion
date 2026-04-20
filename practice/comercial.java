import javax.swing.*;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent ;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.ArrayList;
public class comercial extends JFrame implements ActionListener {

	private JPanel panel;
	private JButton norte,sur ,este,oeste,alta,media,baja,registrar,limpiar;
	private JLabel nombre_cliente ,variedad_chia, peso_recibido , fecha_procesamiento,dia, mes, año,primera_calidad,segunda_calidad,
	tercera_calidad,chori,basura,terron ;
	private JTextField n1 , n2 , n3 , n4, day,moun , year , primer,segund,terce,chor,basu,tero ;
	private JButton selecionado = null ;
	private JButton nivel_prioridad = null ;
	private ArrayList<String> lista_registros = new ArrayList<>();

public comercial(){
		
		panel = new JPanel();
		registrar = new JButton("REGISTRAR LOTE");
		limpiar= new JButton("LIMPIAR FORMULARIO");
		norte = new JButton("NORTE");
		sur = new JButton("SUR");
		este= new JButton("ESTE");
		oeste= new JButton("OESTE");
		alta = new JButton("1");
		media = new JButton("2");
		baja = new JButton("3");
		registrar.addActionListener(this);
		limpiar.addActionListener(this);
		norte.addActionListener(this);
		sur.addActionListener(this);
		este.addActionListener(this);
		oeste.addActionListener(this);
		alta.addActionListener(this);
		media.addActionListener(this);
		baja.addActionListener(this);
		nombre_cliente= new JLabel("Nombre cliente");
		n1 = new JTextField(12);
		variedad_chia = new JLabel("variedad chia");
		n2 = new JTextField(12);
		peso_recibido = new JLabel("PESO");
		n3 = new JTextField(12);
		fecha_procesamiento= new JLabel("FECHA PROCESAMIENTO");
		n4 = new JTextField(12);
		dia = new JLabel ("DIA");
		day = new JTextField(12);
		mes = new JLabel("MES");
		moun = new JTextField(12);
		año = new JLabel("AÑO");
		year = new JTextField(12);
		primera_calidad= new JLabel("PRIMERA");
		primer = new JTextField(12);
		segunda_calidad= new JLabel("SEGUNDA");
		segund = new JTextField(12);
		tercera_calidad= new JLabel("TERCERA");
		terce = new JTextField(12);
		chori=new JLabel("CHORI");
		chor = new JTextField(12);
		basura = new JLabel("BASURA");
		basu= new JTextField(12);
		terron= new JLabel("TERRON");
		tero= new JTextField(12);
		setSize(1200,1200);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLocationRelativeTo(null);
		
 		 panel.add(nombre_cliente);
                panel.add(n1);
                panel.add(variedad_chia);
                panel.add(n2);
                panel.add(peso_recibido);
                panel.add(n3);
                panel.add(fecha_procesamiento);
                panel.add(n4);
		panel.add(dia);
		panel.add(day);
		panel.add(mes);
		panel.add(moun);
		panel.add(año);
		panel.add(year);
		panel.add(primera_calidad);
		panel.add(primer);
		panel.add(segunda_calidad);
		panel.add(segund);
		panel.add(tercera_calidad);
		panel.add(terce);
		panel.add(chori);
		panel.add(chor);
		panel.add(basura);
		panel.add(basu);
		panel.add(terron);
		panel.add(tero);
                panel.add(norte);
                panel.add(sur);
		panel.add(este);
		panel.add(oeste);
		panel.add(alta);
		panel.add(media);
		panel.add(baja);		

		panel.add(registrar);
		panel.add(limpiar);
		add(panel);
		setVisible(true);

	}
	public boolean validar_peso_recibido(){
		int total = 0 ;
		String  cantidades [] = {primer.getText()  ,segund.getText()   ,terce.getText() };

		for(String  c : cantidades){
			try{
			int k = Integer.valueOf(c);
                        total += k ;
		}catch(NumberFormatException e ){
			System.out.println("Tiene que ser un numero");
		}
		}

		return total == Integer.valueOf(n3.getText()) ;
	}

	public boolean validacionCampo(JTextField p){
		if ( p.getText().isEmpty()){ return true ; }
		return false  ;
	}

	public Integer  valida_peso(JTextField p){
		try{

		String a =  p.getText();
		Integer valor = Integer.valueOf(a);
		if( valor  < 0 ) {
			return null;
		}

		return valor ;

	 }catch(NumberFormatException e){
		System.out.println(e.getMessage());
		return null ; 
	}
	}
	


	public  boolean  validar_fecha(){
		String d = day.getText();
		String m = moun.getText();
		String y= year.getText();
				boolean valido = true;
	try{
		
		Integer valor_d= Integer.valueOf(d);
                Integer valor_m =Integer.valueOf(m);
                Integer valor_y =Integer.valueOf(y);
		if(valor_d < 1 || valor_d > 21 ) { valido = false ;}
                if(valor_m < 1 || valor_m > 12 ) {valido = false ; }
                if(valor_y< 2000){ valido = false ;}

                return valido ;


     }catch(NumberFormatException e){
		System.out.println("tiene que ser un numero");
		return valido = false ;
	}
		
	}
	@Override	
	public void actionPerformed(ActionEvent e){

	     JButton elemento_prioridad [] = {alta,media,baja };

	     for(JButton l : elemento_prioridad ){
			if( e.getSource() == l){
				nivel_prioridad = l ; 
			}
		}
             JButton elemento [] = {sur,norte,este,oeste};

			for(JButton l : elemento){
				if(e.getSource() == l ){
					selecionado = l ; 
			 	}
			}

		

		if(e.getSource() == registrar){


			if(!validacionCampo(n1) && !validacionCampo(n2) && !validacionCampo(n3) && !validacionCampo(n4) && !validacionCampo(day) && !validacionCampo(moun) && !validacionCampo(year) && !validacionCampo(primer) && !validacionCampo(segund) && !validacionCampo(terce) && !validacionCampo(chor)  && !validacionCampo(basu) && !validacionCampo(tero) && selecionado != null && nivel_prioridad != null && valida_peso(n3) != null  && validar_fecha()  && validar_peso_recibido()  ) {
			String  valor_guardar []  = {n1.getText() , n2.getText(),n3.getText() , n4.getText() , day.getText() , moun.getText() , year.getText() , primer.getText(), segund.getText(), terce.getText(), chor.getText() , basu.getText() , tero.getText()};

			  FileWriter escribir = null ;
			 try{
			    escribir = new FileWriter("basedatos.txt",true);
			    for(int i = 0 ; i < valor_guardar.length ; i++){
					
					 
						escribir.write(valor_guardar[i] + "\n");
				}
				escribir.write("\n");			}catch(Exception p ){
				System.out.println("No se pudo copiar correctmaente en el archivos");
			}finally{
				if(escribir != null){
					try{
						escribir.close();
					}catch(Exception k){
						System.out.println("NO SE PUEDO CERRRAR");
				}
				}
			}
				
			try(FileReader leer = new FileReader("basedatos.txt")){
				int caracter;
				String palabra = "";
				
				while((caracter = leer.read()) != -1){
					char c = (char) caracter;
					if( c!= '\n'){
						palabra += c;
					}else{
						lista_registros.add(palabra);
						palabra= "";
					}

				}

			for(String v : lista_registros){
				System.out.println(v);
			}
			}catch(Exception u){
				System.out.println("no se pudo leer el archivo");
			}

						
			}else{
				System.out.println("incorrecto");
			}
		}
	} 

	
	
	
}
