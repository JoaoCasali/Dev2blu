from conta import Conta
class PessoaFisica(Conta):
    __segundo_titular = ''
    def __init__(self, numero, titular, cpf, saldo_inicial) -> None:
        super().__init__(numero, "Pessoa Fisica")
        self.titular = titular
        self.cpf = cpf
        self.saldo_inicial = saldo_inicial

    @property
    def segundo_titular(self):
        return self.__segundo_titular

    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular

    def __str__(self):
        return f"{super().__str__()}\nTitular: {self.titular}\nCPF: {self.cpf}\nSaldo Inicial: {self.saldo_inicial}\nSegundo titular: {self.segundo_titular}"