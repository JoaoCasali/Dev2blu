from pessoa import Pessoa

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
print(f"{pessoa1.GetNome()} - {pessoa1.GetSobrenome()} - {pessoa1.GetIdade()}".center(50, ' '))
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
print(f"{pessoa2.GetNome()} - {pessoa2.GetSobrenome()} - {pessoa2.GetIdade()}".center(50, ' '))
print("".center(50, '*'))

print("".center(50, '*'))
print(f'{pessoa2}'.center(50, ' '))
print("".center(50, '*'))