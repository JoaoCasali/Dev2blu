class Conta():
    numero = ''
    titular = ''
    saldo = 0
    limite = 0
    def __str__(self) -> str:
        return f'{self.numero} - {self.titular} - {self.saldo} - {self.limite}'

conta = Conta()
conta.numero = '12321'
conta.titular = 'joao'
conta.saldo = 12321
conta.limite = 500

print(conta)