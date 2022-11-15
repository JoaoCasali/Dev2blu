class Conta():
    def __init__(self, numero, agencia, tipo) -> None:
        self.numero = numero
        self.agencia = agencia
        self.tipo = tipo
        print("Passando pelo construtor da Conta")
    
    def __str__(self):
        return f'Numero da conta: {self.__numero}\nAgencia: {self.__agencia}\nTipo da conta: {self.__tipo}'

    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def agencia(self):
        return self.__agencia
    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia

    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo