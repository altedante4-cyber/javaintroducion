package juego;

import java.util.Scanner;

public class TresEnRaya {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        char[] tablero = new char[9];
        
        
        // iniciamos la partida con un bucle do while para validar la entrada si el usuario introduce el 1 entonces entramos en el bucle else if 
        do {
        	
        	System.out.println("1.Jugar una partida");
        	System.out.println("2.Mostrar estadícas");
        	System.out.println("3.Salir");
            System.out.println("Seleccione una opción ");        
        	int opcion ;
        	
        	opcion = entrada.nextInt();
        	
        	if(opcion == 3) {
        		
        		break;
        	}
        	else if (opcion == 1 ) {
        			System.out.println("-----------");
        		    System.out.println("| 1 | 2 | 3| ");
        	        System.out.println("-----------");
        	        System.out.println("| 4 | 5 | 6| ");
        	        System.out.println("-----------");
        	        System.out.println("| 7 | 8 | 9|");
        	        System.out.println("-----------");
        	        boolean turnoX = true;
                 
             
                int contador = 0 ;
                int posicion ;  
                
                
                 while (contador <= 9 ) {

                 	
                 	
                          // pedimos al usuario que le toque la posicion
                    
                	 
                	 
                	 while (true) {
                		 
                		  
                   	  System.out.print("Jugador " + (turnoX ? "X" : "O") + ", elige posición (1-9): ");

                        posicion = entrada.nextInt()- 1 ;
                       
                     
                         if(posicion >= 1 || posicion <= 9) {
                       	 
                              break;
                         	 
                             }else {
                            	 
                            	  
                               System.out.println("posicion invalida ");
                         }
                       
                	 }
                        	

                          

                	 System.out.println("-------------");
                     for (int i = 0; i < 9; i++) {
                         
                     	System.out.print("| " + tablero[i] + " ");
                         if ((i + 1) % 3 == 0) {   /// mostramos el tablero cada tres lineas 
                             System.out.println("|");
                             System.out.println("-------------");
                         }
                     }
                     
                   	
                    	if (tablero[posicion] == ' ' || tablero[posicion] != 'X' && tablero[posicion] !=  'O'){
                        	
                    		
                    		
                       	 tablero[posicion] = turnoX ? 'X' : 'O';	
                    	   
                     	// cambiamos de turno 
                        	
                    		 turnoX = !turnoX ; 
                 	 
                       		
                       	}
                       
                          
                        
                     
                        	
                         
                         
                  		
                        	   
                        	
                    	  
            
                    	
                    	// esto lo utilizamos para que cuando el usuario introdusca el numero el turno que le toque ponga su signo 
                        
                          
                     
                    	// tablero[posicion] = turnoX ? 'X' : 'O';	
                  	   
                        	// cambiamos de turno 
                           	
                       	//	 turnoX = !turnoX ; 
                    	 
                     
                      // para que no vuelva a seleccionar la misma casilla marcada volvermos a pedir al usuario 
                          
           
                  
                    	
                    	
                    
                    
                    	  
              
                       
                        	
                   		
                     	
                        
                          
                 		
                 	      
                          
                      	
  
                      	// comprobanos si alguien ha ganado 
                  

                        if (tablero[0] == 'X' && tablero[1] == 'X' && tablero[2] == 'X' ) {  // esto es la fila 1  diagonal
                       	     System.out.println("Jugador X ha ganado"); 
                       	    break; 
   
                       	} else  
                        if (tablero[3] == 'X' && tablero[4] == 'X' && tablero[5] == 'X') {  // esto es la fila 2 diagonal
                    	    System.out.println("Jugador X ha ganado"); 
                        	   break;
                       	}else  
                            if (tablero[6] == 'X' && tablero[7] == 'X' && tablero[8] == 'X') {  // esto es la file 3 diagonal
                        	    System.out.println("Jugador X ha ganado"); 
                            	   break;
                           	}
                            else  
                                if (tablero[0] == 'X' && tablero[3] == 'X' && tablero[6] == 'X') {  // primera fila de la primera columana  
                            	    System.out.println("Jugador X ha ganado"); 
                                	   break;
                               	}
                                else  
                                    if (tablero[1] == 'X' && tablero[4] == 'X' && tablero[7] == 'X') {  // 2 columna 
                                	    System.out.println("Jugador X ha ganado"); 
                                    	   break;
                                   	}else  
                                        if (tablero[2] == 'X' && tablero[5] == 'X' && tablero[8] == 'X') {  // 3 columna 
                                     	    System.out.println("Jugador X ha ganado"); 
                                        	   break;
                                       	}else  
                                            if (tablero[0] == 'X' && tablero[4] == 'X' && tablero[8] == 'X') {  // 3 columna 
                                         	    System.out.println("Jugador X ha ganado"); 
                                            	   break;
                                           	}else  
                                                if (tablero[2] == 'X' && tablero[4] == 'X' && tablero[6] == 'X') {  // 3 columna 
                                             	    System.out.println("Jugador X ha ganado"); 
                                                	   break;
                                               	}else {
                                               	  if (tablero[0] == 'O' && tablero[1] == 'O' && tablero[2] == 'O') {  // primera fila 
                                                      System.out.println("Jugador O ha ganado");
                                                  }else
                                                  	if (tablero[3] == 'O' && tablero[4] == 'O' && tablero[5] == 'O') {  // segunda fila 
                                                      System.out.println("Jugador O ha ganado");
                                                  }else
                                                  	if (tablero[6] == 'O' && tablero[7] == 'O' && tablero[8] == 'O') {   // tercera fila 
                                                          System.out.println("Jugador O ha ganado");
                                                      }
                                                  	else
                                                      	if (tablero[0] == 'O' && tablero[3] == 'O' && tablero[6] == 'O') { // primera fila de la pirmera columna
                                                          System.out.println("Jugador O ha ganado");
                                                      }
                                                      	else
                                                          	if (tablero[1] == 'O' && tablero[4] == 'O' && tablero[7] == 'O') {  // segunda columna
                                                              System.out.println("Jugador O ha ganado");
                                                          }else
                                                          	if (tablero[2] == 'O' && tablero[5] == 'O' && tablero[8] == 'O') {  // ultima columna 
                                                                  System.out.println("Jugador O ha ganado");
                                                              }else
                                                              	if (tablero[0] == 'O' && tablero[4] == 'O' && tablero[8] == 'O') {  // diagonal desde la prim
                                                                      System.out.println("Jugador O ha ganado");
                                                                  }else
                                                                  	if (tablero[2] == 'O' && tablero[4] == 'O' && tablero[6] == 'O') {
                                                                          System.out.println("Jugador O ha ganado");
                                                                      }
                    
                                                               	
                                                	}
            	                                  contador += 1;
                 								}
            
                           
                    
                    
                  
        		
        		
        	}else if(opcion == 2) {
        		
        		System.out.println("todavia nada ");
        	}
        	
                    	   
                	   
                
                
                
                
                
                
              
                
                 
              
                
                	 

                    // para asignar la posicion que asigno el usuario en el tablero 

                
                	
                
                    
                
                
                //cambiamos el turno
                
                
                
        
   
            
            
                
        	}while(true);
        
        System.out.println("partida terminada ");
          
            
        }
        
    }




