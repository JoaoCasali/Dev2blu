class Conta():
    def __init__(self, numero, titular, saldo, limite) -> None:
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def gerarExtrato(self):
        return f'{self.numero} - {self.titular} - {self.saldo} - {self.limite}'

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
    
    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
    

conta = Conta(123213, 'Joao', 213213.21, 3000)

print(conta)