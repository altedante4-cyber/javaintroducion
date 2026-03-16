class Sucursales:

    def __init__(self,direccion,provincia , codigo_identificativo_sucursal):
        formatead = str(codigo_identificativo_sucursal).zfill(4)
        self.direccion = direccion
        self.provincia = provincia 
        self._codigo_identificativo_sucursal  = formatead


    @property
    def codigo_identificativo_sucursal(self):
         return self._codigo_identificativo_sucursal

    def __str__(self):
         
         return f"direccion {self.direccion} codigo identificativo {self._codigo_identificativo_sucursal}" 
class Cliente :

    def __init__(self,nombre,apellidos,nif,telefono,sucursal):

         self.nombre = nombre
         self.apellidos = apellidos
         self.nif =nif
         self.telefono =telefono    
         self.sucursal = sucursal 



class CuentaCorriente:
    IBAN = []  
    def __init__(self,codigo_identificativo , saldo, *titulares_cuenta , sucursal ):
            #si los primeros digitos son 00 lo convierto a  string luego lo formateo y le quito para hacer las operaciones 

            formateado_digitos_iniciales_ceros = str(codigo_identificativo).zfill(12)
            
            CuentaCorriente.IBAN.append("ES681234"+ " " + sucursal._codigo_identificativo_sucursal+ " " + formateado_digitos_iniciales_ceros) 
            self.saldo = saldo 
            resultado_titular = [x.split(",") for x in titulares_cuenta]
            if len(resultado_titular) <= 2 :
                 self.titulares_cuenta = titulares_cuenta
            else:
                 self.titulares_cuenta = 0 
            self.sucursal = sucursal 

    @property
    def codigo_de_sucursa_asignado(self):
        return self.sucursal._codigo_identificativo_sucursal      
    

    def buscar_iban_cliente(self,cliente):
        #para buscar el iban necesitamos el codigo de sucursal del cliente

        codigo_sucursal_cliente = cliente.sucursal._codigo_identificativo_sucursal
        codigo_de_sucursal_asignado_cliente=self.codigo_de_sucursa_asignado
        
        lista_encontrado = []

        for i in CuentaCorriente.IBAN:
             
# Crear sucursales
sucursal1 = Sucursales("Calle Mayor 10", "Madrid", 1)
sucursal2 = Sucursales("Avenida Libertad 25", "Barcelona", 23)

# Crear clientes
cliente1 = Cliente("Juan", "Pérez", "12345678A", "600123456", sucursal1)
cliente2 = Cliente("Ana", "García", "87654321B", "600654321", sucursal2)
cliente3 = Cliente("Luis", "Martín", "11223344C", "600987654", sucursal1)

# Crear cuentas corrientes
cuenta1 = CuentaCorriente(1, 1000, cliente1.nombre, cliente2.nombre, sucursal=sucursal1)
cuenta2 = CuentaCorriente(23, 500, cliente3.nombre, sucursal=sucursal2)

# Imprimir sucursales
#print(sucursal1)
#print(sucursal2)

# Imprimir clientes
#print(f"{cliente1.nombre} {cliente1.apellidos}, Sucursal: {cliente1.sucursal.codigo_identificativo_sucursal}")
#print(f"{cliente2.nombre} {cliente2.apellidos}, Sucursal: {cliente2.sucursal.codigo_identificativo_sucursal}")
#print(f"{cliente3.nombre} {cliente3.apellidos}, Sucursal: {cliente3.sucursal.codigo_identificativo_sucursal}")

# Buscar IBAN de clientes
cuenta1.buscar_iban_cliente(cliente1)
#cuenta1.buscar_iban_cliente("Ana")
#cuenta2.buscar_iban_cliente("Luis")

# Mostrar IBAN de las cuentas
print("IBAN cuenta1:", CuentaCorriente.IBAN)

#buscar cliente

