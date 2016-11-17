from unittest import TestCase
from Cuenta import Cuenta


class TestCuenta(TestCase):
    def test_depositar(self):
        nombre = 'Carlos'
        numero = 67
        saldo = 1000
        obj = Cuenta(nombre, numero, saldo)
        self.assertEqual(obj.depositar(500), 1500)


    def test_retirar(self):
        nombre='Carlos'
        numero=67
        saldo=1000
        obj = Cuenta(nombre, numero, saldo)
        self.assertEqual(obj.retirar(500), 500)
