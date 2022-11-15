class Conta():
    def __init__(self, numero, agencia, tipo) -> None:
        self.__numero = numero
        self.__agencia = agencia
        self.__tipo = tipo
        print("Passando pelo construtor da Conta")
    
    def __str__(self):
        return f'Numero da conta: {self.__numero}\nAgencia: {self.__agencia}\nTipo da conta: {self.__tipo}'

