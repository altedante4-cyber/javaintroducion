class Sucursales:
    __banco = "ES681234"
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
         self.__cuenta=[]kl
    def listar_cuentas(self):
         pass

class CuentaCorriente:
    IBAN = []  
    def __init__(self,codigo_identificativo , saldo, *titulares_cuenta , sucursal ):
            #si los primeros digitos son 00 lo convierto a  string luego lo formateo y le quito para hacer las operaciones 

            formateado_digitos_iniciales_ceros = str(codigo_identificativo).zfill(12)
            
            CuentaCorriente.IBAN.append( + " " + sucursal._codigo_identificativo_sucursal+ " " + formateado_digitos_iniciales_ceros) 
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
             


