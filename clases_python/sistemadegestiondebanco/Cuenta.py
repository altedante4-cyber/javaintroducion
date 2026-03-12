class Cuenta:

    def __init__(self,titular, saldo , numero_cuenta):

        self.__titular = titular 
        self.__saldo = saldo 
        self.__numero_cuenta = numero_cuenta 

    
    def depositar(self, cantidad):

        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito de {cantidad} realizado. Nuevo saldo: {self.__saldo}")
         
    
    def retirar(self, cantidad):

        if cantidad > 0 and self.__saldo >= cantidad:
            self.__saldo -= cantidad
            print(f"Retiro de {cantidad} realizado. Nuevo saldo: {self.__saldo}")
        else:
            print("Saldo insuficiente o cantidad inválida")


        
#tener cuidado con los atribuitos privartdos ypubkliuc so 

    def verInfoCuenta(self):

        return f"EL TITULAR ES {self.__titular} EL SALDO {self.__saldo} Y EL NUMEOR DE CUENTA {self.__numero_cuenta}"
    

    def getSaldo(self):

        return self.__saldo 
    

    @property
    def saldo(self):
        return self.__saldo 

    @property # lo que indica es que vamos a definir un get 
    def saldo(self,valor):
        if valor > 0 : 
            self.__saldo = valor 

    @property
    def titular(self,valor):
        self.__titular = valor 




cuenta1 = Cuenta("Juan", 1000, "ES123456")
cuenta1.depositar(500)
cuenta1.verInfoCuenta()
print(cuenta1.saldo)  # Usando property
cuenta1.retirar(200)
    
    

     