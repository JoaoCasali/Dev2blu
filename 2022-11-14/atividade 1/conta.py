class Conta():
    def __init__(self, numero, tipo) -> None:
        self.numero = numero
        self.tipo = tipo
    
    def __str__(self):
        return f'Numero da conta: {self.numero}\nTipo da conta: {self.tipo}'

