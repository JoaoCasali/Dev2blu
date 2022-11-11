from conta import Conta

def main():
    print("".center(50, '*'))
    print("CABEÇALHO".center(50, ' '))
    print("".center(50, '*'))

    conta1 = Conta(
        input("Digite o número da conta: "),
        input("Digite o nome do titular: "),
        float(input("Digite seu saldo: ")),
        float(input("Digite seu limite: "))
    )

    print("".center(50, '*'))
    print(f"{conta1.titular} - {conta1.numero} - {conta1.saldo}".center(50, ' '))
    print("".center(50, '*'))

    print("".center(50, '*'))
    print(f'{conta1}'.center(50, ' '))
    print("".center(50, '*'))

    conta2 = Conta(
        input("Digite o número da conta: "),
        input("Digite o nome do titular: "),
        float(input("Digite seu saldo: ")),
        float(input("Digite seu limite: "))
    )

    print("".center(50, '*'))
    print(f"{conta2.titular} - {conta2.numero} - {conta2.saldo}".center(50, ' '))
    print("".center(50, '*'))

    print("".center(50, '*'))
    print(f'{conta2}'.center(50, ' '))
    print("".center(50, '*'))

main()