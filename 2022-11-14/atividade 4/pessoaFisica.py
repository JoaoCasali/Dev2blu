from conta import Conta
class PessoaFisica(Conta):
    __segundo_titular = ''
    def __init__(self, numero, agencia,titular, cpf, saldo_inicial) -> None:
        super().__init__(numero, agencia,"Pessoa Fisica")
        self.titular = titular
        self.cpf = cpf
        self.saldo_inicial = saldo_inicial
    
    def __str__(self):
        return f"{super().__str__()}\nTitular: {self.titular}\nCPF: {self.cpf}\nSaldo Inicial: {self.saldo_inicial}\nSegundo titular: {self.segundo_titular}"

    @property
    def segundo_titular(self):
        return self.__segundo_titular
    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular

    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self, titular:str):
        self.__titular = titular.title()

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
    
    @property
    def saldo_inicial(self):
        return self.__saldo_inicial
    @saldo_inicial.setter
    def saldo_inicial(self, saldo_inicial):
        self.__saldo_inicial = saldo_inicial