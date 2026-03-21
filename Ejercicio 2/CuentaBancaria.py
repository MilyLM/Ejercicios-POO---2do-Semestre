
class CuentaBancaria:
    #CONSTRUCTOR
    def __init__(self, titular, numeroCuenta, saldo):
        self.titular = titular
        self.numeroCuenta = numeroCuenta
        self.saldo = float(saldo) 

    #MÉTODO PARA AGREGAR DINERO
    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depósito de ${cantidad} realizado con éxito.")

    #MÉTODO PARA RETIRAR DINERO
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de ${cantidad} realizado con éxito.")
        else:
            print("Error: Fondos insuficientes para realizar el retiro.")

    #CONSULTAR SALDO ACTUAL
    def consultarSaldo(self):
        return self.saldo

    #MOSTRAR INFO DE USUARIO
    def mostrarInformacion(self):
        return f"Titular: {self.titular} | Saldo actual: ${self.saldo}"

# CREAR CUENTAS
cuenta1 = CuentaBancaria("Mily", "12345678", 1000.0)
cuenta2 = CuentaBancaria("Lynn", "87654321", 500.0)
cuenta3 = CuentaBancaria("Pedro", "11223344", 0.0)

print(cuenta1.mostrarInformacion())

cuenta1.depositar(500)
cuenta1.retirar(200)
cuenta1.retirar(2000)

print(f"El saldo final de {cuenta1.titular} es: ${cuenta1.consultarSaldo()}")

