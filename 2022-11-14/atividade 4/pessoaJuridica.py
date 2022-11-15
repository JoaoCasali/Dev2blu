from conta import Conta
class PessoaJuridica(Conta):
    __segundo_titular = ''
    def __init__(self, numero, agencia,titular, cnpj, saldo_inicial) -> None:
        super().__init__(numero, agencia,'Pessoa Juridica')
        self.titular = titular
        self.cnpj = cnpj
        self.saldo_inicial = saldo_inicial

    def __str__(self):
        return f"{super().__str__()}\nTitular: {self.titular}\nCNPJ: {self.cnpj}\nSaldo inicial: {self.saldo_inicial}\nSegundo titular: {self.segundo_titular}"

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
    def titular(self, titular):
        self.__titular = titular.title()

    @property
    def cnpj(self):
        return self.__cnpj
    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj
    
    @property
    def saldo_inicial(self):
        return self.__saldo_inicial
    @saldo_inicial.setter
    def saldo_inicial(self, saldo_inicial):
        self.__saldo_inicial = saldo_inicial