import javax.swing.*;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent ;
public class comercial extends JFrame implements ActionListener {

	private JPanel panel;
	private JButton norte,sur ,este,oeste,alta,media,baja,registrar,limpiar;
	private JLabel nombre_cliente ,variedad_chia, peso_recibido , fecha_procesamiento,dia, mes, año,primera_calidad,segunda_calidad,
	tercera_calidad,chori,basura,terron ;
	private JTextField n1 , n2 , n3 , n4, day,moun , year , primer,segund,terce,chor,basu,tero ;
	public comercial(){
		
		panel = new JPanel();
		registrar = new JButton("REGISTRAR LOTE");
		limpiar= new JButton("LIMPIAR FORMULARIO");
		norte = new JButton("NORTE");
		sur = new JButton("SUR");
		este= new JButton("ESTE");
		oeste= new JButton("OESTE");
		alta = new JButton("ALTA");
		media = new JButton("MEDIA");
		baja = new JButton("BAJA");
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
		setSize(350,600);
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

		panel.add(registrar);
		panel.add(limpiar);
		add(panel);
		setVisible(true);

	}

	public boolean validacionCampo(JTextField p){
		if ( p.getText().isEmpty()){ return true ; }
		return false  ;
	}
	@Override	
	public void actionPerformed(ActionEvent e){


             JButton elemento [] = {sur,norte,este,oeste};
                String texto = "";
		for(JButton el : elemento){
                                
        			if(e.getSource() == el){
					texto  += el.getText() ;
				}

                                }
		

		if(e.getSource() == registrar){

			if(!validacionCampo(n1) && !validacionCampo(n2) && !validacionCampo(n3) && !validacionCampo(n4) && !validacionCampo(day) && !validacionCampo(moun) && !validacionCampo(year) && !validacionCampo(primer) && !validacionCampo(segund) && !validacionCampo(terce) && !validacionCampo(chor)  && !validacionCampo(basu) && !validacionCampo(tero) && !texto.isEmpty() ) {
				System.out.println("correcto");	
			}else{
				System.out.println("incorrecto");
			}
		}
	} 

	
	
	
}
