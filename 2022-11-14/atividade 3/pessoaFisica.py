from conta import Conta
class PessoaFisica(Conta):
    __segundo_titular = ''
    def __init__(self, numero, agencia,titular, cpf, saldo_inicial) -> None:
        super().__init__(numero, agencia,"Pessoa Fisica")
        self.__titular = titular
        self.__cpf = cpf
        self.__saldo_inicial = saldo_inicial
        print("Passando pelo construtor da Pessoa Fisica")

    @property
    def segundo_titular(self):
        return self.__segundo_titular

    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular

    def __str__(self):
        return f"{super().__str__()}\nTitular: {self.__titular}\nCPF: {self.__cpf}\nSaldo Inicial: {self.__saldo_inicial}\nSegundo titular: {self.segundo_titular}"