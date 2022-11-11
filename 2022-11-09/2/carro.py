class Carro():
    marca = ''
    modelo = ''
    valor = 0
    def __str__(self) -> str:
        return f'{self.marca} - {self.modelo} - {self.valor}'

carro = Carro()
carro.marca = 'ferrari'
carro.modelo = 'Xj10'
carro.valor = 12321

print(carro)