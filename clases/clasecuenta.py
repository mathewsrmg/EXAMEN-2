class Cuenta:
    def __init__(self):
        self.__numero=None
        self.__saldo=None

    @property
    def numero(self):
        return self.__numero
    @property
    def saldo(self):
        return self.__saldo

    @numero.setter
    def numero(self,numero):
        self.__numero=int(input("Digite número de cuenta: "))
    @saldo.setter
    def saldo(self,saldo):
        self.__saldo=saldo