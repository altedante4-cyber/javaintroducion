public class practica1 {
    public static void main(String[] args) {
        String name = "hola";
        IO.println(name);

        name = "peredo";
        IO.println(name);

        /// esto se inprime luego de que se imprima el hlola

        int age = 43;

        IO.println(age);

        // OTRA MANERA DE CREAR UNA VARIABLE
        //  la variable var  se puede modificar siempre y cuando  se cumpla con que si es un string  que hemos definido anterior mentes pues si lo cambiamos tiene
        // que volver a  hacer un strin  no podemos modificarlo con  un numero entero

        var email = "MICHAELAGUILARPEREDO@GMAIL.COM";
        //constantes
        //final +> es un modificador  con el le indicamos que es una constante con esto le decimos que ya no puede vairar es decir que ya no lo podemos modificar por
        // que es una constante

        final String EMAIL = "michaelaguilar@gmail.com"; // PONER LA VARIBALE EN MAYUSCULAS ES UNA BUENA PRACTICA PARA INDICAR QUE ES UNA CONSTANTE

        //email = 'michaelperedo@gmail.com';  // no se puede modificar por que con el modifiicador final le indicamos que es una constante
        IO.println(EMAIL);
        // TIPOS DE DATOS PRIMITIVOS

        // LOS TIPOS DE DATOS PRIMNITIVO S OSN LOS TIPOS DE DATOS SOBRE LOS CULAES QUE ESTA CONTURIDOS LOS NUCLEOS Y CORES SON LOS TIPOS DE DATOS QUE NOSOTROS SOMOS DE CAPASES DE CONTRUIR

       int myInt = 35;
       IO.println(myInt);    // sirve para representar datos enteros


        // REPRESENTACION DE DECIMALES tambien tenemos el float, long,byte
        double Double =  1.66;
        IO.println(Double);

        // el char hace referencia a un unico aracter
        char   myChar = 'a';
        IO.println(myChar);

        //tipo de caracter booleanos
        boolean myBoolean = true;
        myBoolean = false;
        IO.println(myBoolean);

        // como saber el tipoo de dato en tiempo de copilacion

    }
}
