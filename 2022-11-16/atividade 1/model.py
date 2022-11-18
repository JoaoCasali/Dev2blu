class Conta():
    def __init__(self, titular, numero, saldo) -> None:
        self.__titular = titular
        self.__numero = numero
        self.__saldo = saldo

    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    
    def __str__(self) -> str:
        return f"{self.titular}; {self.numero}; {self.saldo}"