from pessoa import Pessoa

def main():
    print("".center(50, '*'))
    print("CABEÇALHO".center(50, ' '))
    print("".center(50, '*'))

    pessoa1 = Pessoa(
        input("Digite o nome da pessoa: "),
        input("Digite o sobrenome: "),
        int(input("Digite sua idade: ")),
        input("Digite seu cpf: ")
    )

    print("".center(50, '*'))
    print(f"{pessoa1.nome} - {pessoa1.sobrenome} - {pessoa1.idade}".center(50, ' '))
    print("".center(50, '*'))

    print("".center(50, '*'))
    print(f'{pessoa1}'.center(50, ' '))
    print("".center(50, '*'))

    pessoa2 = Pessoa(
        input("Digite o nome da pessoa: "),
        input("Digite o sobrenome: "),
        int(input("Digite sua idade: ")),
        input("Digite seu cpf: ")
    )

    print("".center(50, '*'))
    print(f"{pessoa2.nome} - {pessoa2.sobrenome} - {pessoa2.idade}".center(50, ' '))
    print("".center(50, '*'))

    print("".center(50, '*'))
    print(f'{pessoa2}'.center(50, ' '))
    print("".center(50, '*'))

main()