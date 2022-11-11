from carro import Carro

def main():
    print("".center(50, '*'))
    print("CABEÇALHO".center(50, ' '))
    print("".center(50, '*'))

    carro1 = Carro(
        input("Digite a marca: "),
        input("Digite o modelo: "),
        float(input("Digite o valor: "))
    )

    print("".center(50, '*'))
    print(f"{carro1.marca} - {carro1.modelo} - {carro1.valor}".center(50, ' '))
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
    print(f"{carro2.marca} - {carro2.modelo} - {carro2.valor}".center(50, ' '))
    print("".center(50, '*'))

    print("".center(50, '*'))
    print(f'{carro2}'.center(50, ' '))
    print("".center(50, '*'))

main()