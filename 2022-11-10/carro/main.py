from carro import Carro

print("".center(50, '*'))
print("CABEÇALHO".center(50, ' '))
print("".center(50, '*'))

carro1 = Carro(
    input("Digite a marca: "),
    input("Digite o modelo: "),
    float(input("Digite o valor: "))
)

print("".center(50, '*'))
print(f"{carro1.GetMarca()} - {carro1.GetModelo()} - {carro1.GetValor()}".center(50, ' '))
print("".center(50, '*'))

print("".center(50, '*'))
print(f'{carro1}'.center(50, ' '))
print("".center(50, '*'))

carro2 = Carro(
    input("Digite a marca: "),
    input("Digite o modelo: "),
    float(input("Digite o valor: "))
)

print("".center(50, '*'))
print(f"{carro2.GetMarca()} - {carro2.GetModelo()} - {carro2.GetValor()}".center(50, ' '))
print("".center(50, '*'))

print("".center(50, '*'))
print(f'{carro2}'.center(50, ' '))
print("".center(50, '*'))