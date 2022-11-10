class Conta():
    def __init__(self, numero, titular, saldo, limite) -> None:
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def __str__(self):
        return f'{self.__numero} - {self.__titular} - {self.__saldo} - {self.__limite}'

    def GetNumero(self):
        return self.__numero
    def SetNumero(self, numero):
        self.__numero = numero

    def GetTitular(self):
        return self.__titular
    def SetTitular(self, titular):
        self.__titular = titular
    
    def GetSaldo(self):
        return self.__saldo
    def SetSaldo(self, saldo):
        self.__saldo = saldo

    def GetLimite(self):
        return self.__limite
    def SetLimite(self, limite):
        self.__limite = limite
