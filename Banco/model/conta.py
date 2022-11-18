class Conta():
    def __init__(self, agencia, numero_agencia) -> None:
        self.__agencia = agencia
        self.__numero_agencia = numero_agencia

    @property
    def agencia(self):
        return self.__agencia
    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia
    
    @property
    def numero_agencia(self):
        return self.__numero_agencia
    @numero_agencia.setter
    def numero_agencia(self, numero_agencia):
        self.__numero_agencia = numero_agencia
    
    def __str__(self):
        return f'{self.agencia};{self.numero_agencia}'

