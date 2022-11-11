class Conta():
    def __init__(self, numero, titular, saldo, limite) -> None:
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

conta = Conta(123213, 'Joao', 213213.21, 3000)

print(conta)