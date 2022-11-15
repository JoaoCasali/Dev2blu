from conta import Conta
class PessoaJuridica(Conta):
    __segundo_titular = ''
    def __init__(self, numero, agencia,titular, cnpj, saldo_inicial) -> None:
        super().__init__(numero, agencia,'Pessoa Juridica')
        self.__titular = titular
        self.__cnpj = cnpj
        self.__saldo_inicial = saldo_inicial

    @property
    def segundo_titular(self):
        return self.__segundo_titular

    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular

    def __str__(self):
        return f"{super().__str__()}\nTitular: {self.__titular}\nCNPJ: {self.__cnpj}\nSaldo inicial: {self.__saldo_inicial}\nSegundo titular: {self.segundo_titular}"