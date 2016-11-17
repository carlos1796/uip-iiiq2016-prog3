class Cuenta:
    def __init__(self, nombre, numero, saldo):
        self.nombre = nombre
        self.numero= numero
        self.saldo = saldo
    def depositar(self, a):
        self.saldo=self.saldo+a
        return self.saldo

    def retirar(self, a):
        self.saldo=self.saldo-a
        return self.saldo





