public class operadores_aritmeticos {
    public  static  void main(String [] args) {

        //Operadores aritemeticos ==>  suma , resta , division , multiplicacion

        var a = 4;
        var b = 3;
        IO.println(a + b);
        IO.println(a - b);
        IO.println(a * b);
        IO.println(a / b);
        IO.println(a % b);  // esto es el modulo es decir el resto de la division

        //  OPERADORES DE ASIGNACION =>  asignar valores a las variables
        a = b;
        IO.println(a);
        a = b * 2;
        IO.println(a);

        //Operadores de comparacion o relacionales -> que te devuelven falso o verdadero

        IO.println(a == b); //esto te devuleve true o false
        IO.println(a != b); // AQUI LE ESTAMOS SI ES DIFERENTE A A

        //OPERADORES LOGICOS

        IO.println(true && true);
        IO.println(true && false);
        IO.println(false && true);
        IO.println(false && false);

        IO.println(3 > 2 && 5 == 2);

        // OR
        IO.println(true || true );
        IO.println(true || false );
        IO.println(false || true );
        IO.println(false || false );

        IO.println( 3 > 2  || 5 == 2 );  // conque una sea erdadera te devuelve true

        //NO (NOT) le da la vuelta al  resultado



        IO.println( !true ); // esto da falso

        IO.println( !(3 > 2) || 5 == 2 );


        //Operadores unarios
        IO.println(+b);
        IO.println(-b);
        IO.println( ++b); //incrementa antes de usar el valor
        IO.println(b++);  // usa el valor luego incrementa
        IO.println(--b); // decrementa antes de usar el valor
        IO.println(b--); //usa el valor y luego decrementa

    }
}
